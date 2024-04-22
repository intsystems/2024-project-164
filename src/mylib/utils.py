import torch
import numpy as np

def collate_fn(data: tuple):
  samples, labels = zip(*data)
  anchors = torch.stack(list(map(lambda x: x[0], samples)))
  positives = torch.stack(list(map(lambda x: x[1], samples)))

  return (anchors, positives), labels


def complete_with_negatives(anchor_embeds: torch.Tensor, positives_embeds: torch.Tensor, labels: torch.Tensor):
  dist_func = torch.cdist

  distances = dist_func(anchor_embeds.unsqueeze(0), positives_embeds.unsqueeze(0))[0]

  negatives = [None for _ in range(len(labels))]
  neg_distances = [float('-inf') for _ in range(len(labels))]


  for i in range(len(labels)):
    for j in range(len(labels)):
      if distances[i][j].item() > neg_distances[i] and labels[i] != labels[j]:
        negatives[i] = positives_embeds[j]
        neg_distances[i] = distances[i][j].item()

  neg_distances_idx = np.where(np.array(neg_distances) != float('-inf'))[0]

  negatives_embeds = torch.stack(negatives)[neg_distances_idx]
  anchor_embeds = anchor_embeds[neg_distances_idx]
  positives_embeds = positives_embeds[neg_distances_idx]

  return anchor_embeds, positives_embeds, negatives_embeds