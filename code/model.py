import torch
import torch.nn as nn

class Card2CodeModel(nn.Module):
  def __init__(self):
    self.linear = nn.Linear(5,5)
    
  def forward(self, inputs=None):
    return self.linear(inputs)
