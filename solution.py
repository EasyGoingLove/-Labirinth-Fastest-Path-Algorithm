def Solution (rows,cols,start_node,end_node,full_labirint):
    correct_path = []
    cost_matrix = {}
    obstecles = []

    estimated_best_cost = abs((start_node[0] + start_node[1]) - (end_node[0] + end_node[1]))
    cost_steps = 0

    for x in range(0, rows):
        for y in range(0, cols):
            if full_labirint[x][y] == "#":
                obstecles.append((x, y))

    cost_calculator(obstecles, start_node, end_node, full_labirint, cost_matrix)
    print(cost_matrix)


    while cost_steps != estimated_best_cost:
        for x in cost_matrix.values():






    return correct_path




def cost_calculator(obstecles,start_node,end_node,full_labirint,cost_matrix):
  total_Elements = len(full_labirint)
  for x in range(0, total_Elements):
    for y in range(0, total_Elements):
        current_node = (x,y)
        start_total = int(start_node[1] + start_node[0])
        difference = int((current_node[0]+current_node[1]) - start_total)
        if end_node < start_node:
            difference *= -1

        cost = abs(difference)

        if cost == 0:
            cost = 2
        if current_node not in obstecles:
            cost_matrix[current_node] = cost












           # if end_node > start_node:
           #     if start_y != end_y and full_labirint[start_x][start_y + 1] != "#":
           #        start_y += 1
           #        correct_path.append((start_x, start_y))
           #
           #     elif start_x != end_x and full_labirint[start_x+1][start_y] != "#":
           #         start_x +=1
           #         correct_path.append((start_x,start_y))
           #     elif full_labirint[start_x+1][start_y] == "#" and full_labirint[start_x][start_y + 1] == "#":
           #         start_y -= 1
           #
           # else:
           #     if start_y != end_y and full_labirint[start_x][start_y - 1] != "#":
           #         start_y -= 1
           #         correct_path.append((start_x, start_y))
           #     elif start_x != end_x and full_labirint[start_x - 1][start_y] != "#":
           #         start_x -= 1
           #         correct_path.append((start_x, start_y))
