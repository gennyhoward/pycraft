# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]


X, Y, Z = Position()
from math import *


for m in range(10):
  for i in range(100):
    n = 10
    r = m * 5
    x = r * cos(i/n)
    z = r * sin(i/n)
    SetBlock((x, i-1, z), blocks[int(i/10)%4])


