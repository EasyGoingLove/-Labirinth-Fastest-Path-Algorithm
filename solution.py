import time

def Solution (rows,cols,start_node,end_node,full_labirint):
    correct_path = []
    obstecles = []

    start_x = start_node[0]
    start_y = start_node[1]

    end_x = end_node[0]
    end_y = end_node[1]

    estimated_best_cost = abs((start_x + start_y) - (end_x + end_y))
    total_cost = 0
    for x in range(0, rows):
        for y in range(0, cols):
           if full_labirint[x][y] == "#":
               obstecles.append((x,y))

    #time.sleep(3)
    while (start_x,start_y) != (end_x,end_y):
           if end_node > start_node:
               if start_y != end_y and full_labirint[start_x][start_y + 1] != "#":
                  start_y += 1
                  correct_path.append((start_x, start_y))
               if start_x != end_x and full_labirint[start_x+1][start_y] != "#":
                   start_x +=1
                   correct_path.append((start_x,start_y))
               elif full_labirint[start_x+1][start_y] == "#" and full_labirint[start_x][start_y + 1] == "#":
                   start_y -= 1

           else:
               if start_y != end_y and full_labirint[start_x][start_y - 1] != "#":
                   start_y -= 1
                   correct_path.append((start_x, start_y))
               elif start_x != end_x and full_labirint[start_x - 1][start_y] != "#":
                   start_x -= 1
                   correct_path.append((start_x, start_y))


    return correct_path