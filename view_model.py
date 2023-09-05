from rich import print as rprint
import torch

model = torch.load('model.pth')
rprint(model)

