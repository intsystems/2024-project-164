#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gc

from torchvision import transforms
import torch
from torch.utils.tensorboard import SummaryWriter
import numpy as np

from dataset import Dataset
from model import EmbeddingModel
from utils import collate_fn, complete_with_negatives

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def train(dataset: torch.Tensor):
    transformations = transforms.Compose([
        transforms.ToPILImage(),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.Resize(288),
        transforms.ToTensor()
    ])


    train_dataset = Dataset(dataset=dataset, transform=transformations)
    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)

    model = EmbeddingModel().to(DEVICE)
    model.train()

    optimiser = torch.optim.Adam(model.parameters())

    triplet_loss_margin = 1000

    losses = []
    num_unique_labels = []
    num_embeds = []
    iterations = []

    writer = SummaryWriter()


    for i, (X, y) in enumerate(train_dataloader):
        torch.cuda.empty_cache()

        anchors, positives = X
        optimiser.zero_grad()

        anchors_embeds = model(anchors.to(DEVICE))
        anchors = None
        gc.collect()

        positives_embeds = model(positives.to(DEVICE))
        positives = None
        gc.collect()

        anchors_embeds, positives_embeds, negatives_embeds = complete_with_negatives(anchors_embeds, positives_embeds, y)

        pos_dist = torch.linalg.vector_norm(anchors_embeds - positives_embeds, dim=1)
        neg_dist = torch.linalg.vector_norm(anchors_embeds - negatives_embeds, dim=1)
        batch_loss = torch.maximum(
                pos_dist - neg_dist + triplet_loss_margin,
                torch.zeros(anchors_embeds.shape[0], device=DEVICE))

        pos_dist = None
        neg_dist = None
        gc.collect()

        loss = torch.mean(batch_loss)
        batch_loss = None
        gc.collect()

        if i % 5 == 0:
            iterations.append(i)
            losses.append(loss.item())
            num_unique_labels.append(np.unique(np.array(y)).shape[0])
            num_embeds.append(len(anchors_embeds))


            for plot_data, name in zip(
                (losses, num_unique_labels, num_embeds),
                ("lossses", "unique_labels", "embeds")):
                writer.add_scalar(name, plot_data[-1], iterations[-1])
            writer.flush()


        loss.backward()
        optimiser.step()
    
    return model
