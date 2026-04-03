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
number_of_sides = int(input("how many sides are there?"))
while True:
    sides = int(input("enter the number of sides that the polygons have "))
    pen.clear()
    if sides <3:
        pen.write("error polygons have more than 3 sides")
    elif sides != 4:
       regular_polygon(pen,sides)
    else: 
        number_of_sides = int(input("how many sides are there?"))
        if number_of_sides <3:
            print("this is unknown")
        elif number_of_sides == 3:
            print("this is a triangle")
        elif number_of_sides == 4:
            print("this is a Quadrilateral")
        elif number_of_sides == 5:
            print("this is a Pentagon")
        elif number_of_sides == 6:
            print("this is a Hexagon")
        else:   print("this is unknown")
        if number_of_sides == 4:



    
    
    
    
    
    
    
    
    
    
    
screen.exitonclick()