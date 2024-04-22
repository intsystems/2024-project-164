from torch import nn
import torchvision


class EmbeddingModel(nn.Module):
  def __init__(self):
    super().__init__()
    self._backbone = torchvision.models.efficientnet_b2()
    self._backbone.classifier = nn.Identity()
    self._backbone.features[0][0] = nn.Conv2d(
        1, 32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
    self._projection = nn.Linear(1408, 96)

    self.net = nn.Sequential(
        self._backbone,
        self._projection
    )

  def forward(self, input):
    embeds = self.net(input)

    return embeds