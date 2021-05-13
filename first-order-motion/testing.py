# To test if your local machine has a supported cuda device

import torch
import sys
import pycuda.driver as cuda
cuda.init()
## Get Id of default device
print(torch.cuda.current_device())
# 0
print(cuda.Device(0).name()) # '0' is the id of your GPU