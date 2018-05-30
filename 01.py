import torch as th
import torch.nn.functional as F

def v(data, requires_grad=False):
    return torch.autograd.Variable(data, requires_grad=requires_grad)
