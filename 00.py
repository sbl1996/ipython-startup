import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy.linalg as lg
import tensorflow as tf
import matplotlib
plt.style.use('seaborn')

from io import StringIO

def dm(s, **kwargs):
  if isinstance(s, list):
      return np.array(s)
  f = StringIO(s.replace(';', '\n'))
  return np.genfromtxt(f, **kwargs)

matplotlib.rcParams['font.sans-serif'] = 'SimHei'
