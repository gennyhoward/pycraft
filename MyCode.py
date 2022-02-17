# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]

X, Y, Z = Position()

for x in range(5):
    for i in range(5):
        SetBlock((X - x, Y - 1 + i, Z), blocks[i%4])
