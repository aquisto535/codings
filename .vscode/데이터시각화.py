from cProfile import label
import gc
from turtle import color
from matplotlib import patheffects
import matplotlib.pyplot as plt
import numpy as np
import os


plt.title('rating')
plt.plot([40, 30, 35, 30, 25], label='right', color='pink')  # x축, y축
plt.plot([30, 35, 30, 35, 40], label='left', color='skyblue')  # x축, y축
plt.legend()
plt.show()
