from random import seed
from random import randint



def main_labirint (quantity,rows,cols,start_node,end_node):

    labirint_dimensions = [[0 for x in range(rows)] for y in range(cols)]
    seed(1)

    for n in range(0, quantity):
        x = randint(0, rows-1)
        y = randint(0, cols-1)
        labirint_dimensions[x][y] = 1


    for x in range(0 ,rows) :
       for y in range(0 ,cols) :
           if labirint_dimensions[x][y] == 0:
               labirint_dimensions[x][y] = "."
           if labirint_dimensions[x][y] == 1:
               labirint_dimensions[x][y] = "#"
           if (x,y) == start_node:
               labirint_dimensions[x][y] = "S"
           if (x,y) == end_node:
               labirint_dimensions[x][y] = "E"


           print(labirint_dimensions[x][y], end=" ")
       print()
    return labirint_dimensions









