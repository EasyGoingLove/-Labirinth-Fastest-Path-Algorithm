from utils import *
from solution import Solution


def draw_final_product (full_labirint,full_solution,rows,cols,end_node):
  for x in range(0, rows):
    for y in range(0, cols):
      if full_solution[a]==(x,y) and (x,y)!= end_node:
        print(full_solution[x])
        print((x,y))
        full_labirint[x][y] = "*"

  for x in range(0, rows):
    for y in range(0, cols):
      print(full_labirint[x][y],"",end=" ")
    print()






print("Enter the x and y cordinates for the variables 'rows' and 'cols':")
print("For x :")
rows = int(input())
print("For y :")
cols = int(input())

print("Enter the x and y cordinates for the variable 'start_node':")
print("For x :")
x = int(input())
print("For y :")
y = int(input())
start_node = (x, y)

print("Enter the x and y cordinates for the variable 'end_node':")
print("For x :")
x = int(input())
print("For y :")
y = int(input())
end_node = (x, y)

print("Enter the number of obstacles for the labirint:")
max_quantity = ((rows*cols)/3)
quantity = int(input())
while quantity > max_quantity:
  print(" INCORRECT INPUT -> Enter the number of obstacles for the labirint:")
  quantity = int(input())



full_labirint = main_labirint (quantity,rows,cols,start_node,end_node)
full_solution = Solution (rows,cols,start_node,end_node,full_labirint)
print(full_solution)
print()
draw_final_product (full_labirint,full_solution,rows,cols,end_node)

