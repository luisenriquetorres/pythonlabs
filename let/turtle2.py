import turtle
shelly = turtle.Turtle()
turtle.bgcolor('black')
shelly.color('orange')
line_length = 5

for i in range(80):
    shelly.forward(line_length)
    shelly.right(90)
    line_length = line_length + 5
    
