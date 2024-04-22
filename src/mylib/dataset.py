import torch
import numpy as np


class Dataset(torch.utils.data.Dataset):
    def __init__(self, dataset, transform):
        super().__init__()
        self.dataset = dataset
        self.transform = transform

    def __len__(self):
        return np.prod(self.dataset.shape[:2])

    def __getitem__(self, idx):
        alphabet_idx = idx // len(self.dataset[1])
        image_idx = idx % len(self.dataset[1])

        image, label = self.dataset[alphabet_idx][image_idx], alphabet_idx
        image = self.transform(image)
        positive_image = self.dataset[alphabet_idx][np.random.randint(0, len(self.dataset[1]))]
        positive_image = self.transform(image)

        return (image, positive_image), label