import turtle
shelly = turtle.Turtle()
##shelly.begin_fill()
##shelly.color('red')
##
##
##for repeat in range(4):
##    shelly.forward(100)
##    shelly.right(90)
##
##shelly.end_fill()

##for n in range(6):
##    for i in range(4):
##        shelly.forward(100)
##        shelly.left(90)
##    shelly.right(60

##colors = ['red','blue','green','yellow','white','orange']
##turtle.bgcolor('black')
##
##for big_repeat in range(36):
##    for lines_in_hexagon in range(6):
##        print('hexagono numero',big_repeat,'. linea numero',lines_in_hexagon)
##        print('color',colors[lines_in_hexagon])
##        shelly.color(colors[lines_in_hexagon])
##        shelly.forward(100)
##        shelly.left(60)
##    shelly.right(10)
##    
##shelly.penup()
##shelly.color('white')
##for i in range(36):
##    shelly.forward(220)
##    shelly.pendown()
##    shelly.circle(5)
##    shelly.penup()
##    shelly.backward(220)
##    shelly.right(10)
##shelly.hideturtle()

turtle.bgcolor('black')
shelly.color('red')


line_length = 2
for line in range(200):
    line_length = line_length + 5
    shelly.forward(line_length)
    shelly.right(90)

    
    
    





