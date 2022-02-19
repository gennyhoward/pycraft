# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]


# SetBlock((x,y,z), blocks[y%4])
# for y in range(10):

from math import *


X, Y, Z = Position()

X, Y, Z = -5,-1,-5


# East and West Wall
for x in range(10):
  for y in range(10):
    SetBlock((X+x,Y+y,Z),BRICK)
    SetBlock((X+x,Y+y,Z+9),GRASS)

# North and South Wall
for x in range(10):
  for y in range(10):
    SetBlock((X,   Y+y,Z+x),SAND)
    SetBlock((X+9,Y+y,Z+x),STONE)

# Roof
for x in range(10):
  for z in range(10):
     SetBlock((X+x,9,Z+z),STONE)

ClearBlock((0,9,0))

# Table
SetBlock((0,-1,0),SAND)
SetBlock((0,0,0),SAND)
for x in range(3):
  for z in range(3):
    SetBlock((x-1,1,z-1),STONE)


# size = 11
# for y in range(size):  
  # for x in range(size):  
    # SetBlock((x,-1+y,0), STONE)
    # SetBlock((x,-1+y,9), STONE)
  # for z in range(size):  
    # SetBlock((0,-1+y,z), STONE)
    # SetBlock((9,-1+y,z), STONE)
  

# y=size
# for x in range(0, size, 2):  
  # SetBlock((x,-1+y,0), SAND)
  # SetBlock((x,-1+y,size-2), SAND)
# for z in range(0, size, 2):  
  # SetBlock((0,-1+y,z), SAND)
  # SetBlock((size-2,-1+y,z), SAND)
  


# for m in range(10):
  # for i in range(100):
    # n = 10
    # r = m * 5
    # x = r * cos(i/n)
    # z = r * sin(i/n)
    # SetBlock((x, i-1, z), blocks[int(i/10)%4])


