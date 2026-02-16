#TurtleGraphics.py
#Name: Addy Duering
#Date: 2/15/26
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)



def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)
    
def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100)
    
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle,50)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle,50)
        myTurtle.end_fill()
    elif corner == 3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle,50)
        myTurtle.end_fill()
    elif corner == 4:
        myTurtle.forward(50)
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle,50)
        myTurtle.end_fill()
        

def squaresInSquares(myTurtle, num):
    size = 250
    change = 25
    for i in range(num):
        myTurtle.penup()
        myTurtle.goto((-size/2), (size/2))
        myTurtle.setheading(0)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        myTurtle.penup()
        myTurtle.forward(change)
        myTurtle.left(90)
        myTurtle.pendown()
        size = size - (2 * change)
        
def main():
    myTurtle = turtle.Turtle()

    # drawPolygon(myTurtle, 5) #draws a pentagon
    drawPolygon(myTurtle, 5)
    # drawPolygon(myTurtle, 8) #draws an octogon
    drawPolygon(myTurtle, 8)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    fillCorner(myTurtle, 2)
    fillCorner(myTurtle, 3)
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 5)
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    squaresInSquares(myTurtle, 3)

main()

