import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchsummary import summary

import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.transforms import ToTensor

import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split

print(f"Torch Version: {torch.__version__}\nTorchvision Version: {torchvision.__version__}\nNumpy Version: {np.__version__}\nScikit-Learn Version: {sklearn.__version__}")