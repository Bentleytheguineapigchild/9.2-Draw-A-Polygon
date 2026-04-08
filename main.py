from turtle import *
def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(50)
        turtle.left(360/ sides)
    turtle.end_fill()



screen = Screen()
screen.title("POLYGONS!!!")
screen.bgcolor("gold")
screen.setup(width = 800, height = 800)

pen = Turtle()
pen.hideturtle()
pen.speed(0)
while True:
    number_of_sides = int(input("enter the number of sides that the polygons have "))
    
    pen.clear()
    if number_of_sides <3:
        pen.write("error polygons have more than 3 sides")
    elif number_of_sides != 4:
        regular_polygon(pen,number_of_sides)
    else:
        # Code for a quadrilateral
        number_of_points = int(input("how many sides are parallel"))
    if number_of_points <= 1:
        print("this is an unknown quadrilateral")
    elif number_of_points == 2 and number_of_sides !=4:
        print("this is a trapezoid")
    elif number_of_points == 4 and number_of_sides != 4:
        print("this is a parallelogram")
    elif number_of_points == 4 and number_of_sides ==4:
        print("this is a rectangle")
    else: print("this is a square")
        



    
    
    
    
    
    
    
    
    
    
    
screen.exitonclick()