import math

origin_point = (0, 0)

moveVerticle = 0
moveHorizonal = 0

up = 5    
down = 3
left = 3
right = 2

moveHorizonal = moveHorizonal - left + right    #on a graph, left on the x-axis results in a negative number and right results in a positive

moveVerticle = moveVerticle - down + up  #on a graph, down on the y-axis results in a negative number and up results in a positive

moves = (moveHorizonal, moveVerticle)

x_distance = abs(origin_point[0] + moves[0])
y_distance = abs(origin_point[1] + moves[1])

distance = round(math.sqrt((x_distance**x_distance) + (y_distance**y_distance)))

print(distance)
