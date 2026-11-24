import numpy as np
import torch

torch.manual_seed(0)
np.random.seed(0)

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print(f"Using device: {device}")