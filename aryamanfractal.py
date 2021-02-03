import turtle

points = [[0,75],[-125,-175], [125,-175]]

x = turtle.Turtle()
def triangle(points):
    x.penup()
    x.goto(points[0][0],points[0][1])
    x.pendown()
    x.goto(points[1][0],points[1][1])
    x.goto(points[2][0],points[2][1])
    x.goto(points[0][0],points[0][1])
        
triangle(points)
           
turtle.done()


