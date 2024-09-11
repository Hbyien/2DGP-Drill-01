import turtle


def move_forward():
    turtle.forward(50)
    turtle.stamp()
    
def move_up():
    turtle.setheading(90)  
    move_forward()

def move_down():
    turtle.setheading(270)  
    move_forward()

def move_left():
    turtle.setheading(180)  
    move_forward()

def move_right():
    turtle.setheading(0)  
    move_forward()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(move_up, 'w')    
turtle.onkey(move_down, 's')  
turtle.onkey(move_left, 'a')  
turtle.onkey(move_right, 'd') 
turtle.onkey(restart, 'Escape') 
turtle.listen()

