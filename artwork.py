#The program draw a pattern in Chinese "Yinyang" culture, a chinese national flag
#and a repetitive circle pattern in different colors, also two squares in differnt colors
#Ziwei Hu 
import turtle
import random


def yinyang_pattern():
    """ (NoneType) -> turtle
    Draw an pattern in Chinese "Yinyang" culture using turtle.
    >>> Yinyang_pattern()
    """
    #creat a turtle called nadal, change the speed of the turtle
    nadal = turtle.Turtle()
    nadal.speed("fastest")
    nadal.hideturtle()
    
    #move the turtle to upleft of the canvas
    nadal.penup()
    nadal.goto(-150,90)
    nadal.pendown()
    
    #draw the right half of the pattern which is black
    nadal.fillcolor("black")
    nadal.begin_fill()
    nadal.circle(100,180)
    nadal.circle(50,-180)
    nadal.circle(-50,-180)
    nadal.end_fill()
    
    #draw a small white circle in the right half of the pattern
    nadal.penup()
    nadal.goto(-140,150)
    nadal.pendown()
    nadal.fillcolor("white")
    nadal.begin_fill()
    nadal.circle(10)
    nadal.end_fill()
    
    #draw a small black cirle in the left half of the pattern
    nadal.penup()
    nadal.goto(-160,250)
    nadal.pendown()
    nadal.fillcolor("black")
    nadal.begin_fill()
    nadal.circle(10)
    nadal.end_fill()
    
    #draw the left half of the pattern
    nadal.penup()
    nadal.goto(-150,290)
    nadal.pendown()
    nadal.circle(100,180)
    
    

def repetitive_circle(x,y):
    """ (NoneType) -> turtle
    Draw an purple repetitive circle pattern at x and y coordinate.
    >>> repetitive_circle()
    """
    #creat a turtle called nadal, change the color and speed of the turtle
    roger = turtle.Turtle()
    roger.color("mediumpurple")
    roger.speed("fastest")
    roger.hideturtle()
    
    #move the turtle to x and y coordinate
    roger.penup()
    roger.goto(x,y)
    roger.pendown()
    
    #draw a repetive circle pattern
    for i in range(40):
        roger.circle(50)
        roger.left(360/40)
        
        
        
def yellow_star(x,y,size):
    """ (int,int) -> turtle
    Draw a small yellow star starting at x and y coordinate, in given size.
    >>> yellow_star(-10,-15,5)
    >>> yellow_star(0,0,2)
    >>> yellow_star(50,50,10)
    """
    #creat a turtle called novak, change the color and speed of the turtle
    novak = turtle.Turtle()
    novak.color("yellow")
    novak.speed("fastest")
    novak.hideturtle()

    #move turtle to x and y coordinate
    novak.penup()
    novak.goto(x,y)
    novak.pendown()

    #draw a small yellow star in given size
    novak.fillcolor("yellow")
    novak.begin_fill()
    for i in range(5):
        novak.forward(size)
        novak.left(72)
        novak.forward(size)
        novak.right(144)
    novak.end_fill()
     
     

def red_flag():
    """ (NoneType) -> turtle
    Draw a Chinese national flag, a red rectangle with five yellow start at upleft.
    >>> red_flag()
    """
    #creat a turtle called rose and change its speed and color
    rose = turtle.Turtle()
    rose.color("red")
    rose.speed("fastest")
    rose.hideturtle()
    
    #move turtle to downleft of the canvas.
    rose.penup()
    rose.goto(-250,-10)
    rose.pendown()
     
    #draw a red triangle
    rose.fillcolor("red")
    rose.begin_fill()
    for i in range(2):
        rose.forward(230)
        rose.right(90)
        rose.forward(150)
        rose.right(90)
    rose.end_fill()
    
    #draw five little yellow stars inside left top of the red rectangle
    yellow_star(-230,-45,10)
    yellow_star(-200,-30,2)
    yellow_star(-190,-40,2)
    yellow_star(-190,-53,2)
    yellow_star(-200,-63,2)



def colored_squares():
    """ (NoneType) -> turtle
    Draw a four squares in pink,orange,green,or blue colors.
    >>> squares()
    """
    #create a turtle called jennie and change its speed
    jennie = turtle.Turtle()
    jennie.speed("fastest")
    jennie.hideturtle()
    
    #move turtle to down right of the canvas
    jennie.penup()
    jennie.goto(50,0)
    jennie.pendown()
    
    #draw four squares in color
    for i in range(4):
        #generate a random integer between 1 to 4, indicating which color to filled
        number = random.randint(1,4)
        if number == 1:
            color = "PaleGreen"
        elif number == 2:
            color = "LightSalmon"
        elif number == 3:
            color = "Pink"
        elif number == 4:
            color = "LightCyan"
            
        #change the color filling the square 
        jennie.color(color)
        jennie.fillcolor(color)
        jennie.begin_fill()
        
        #draw a square
        for j in range(4):
            jennie.forward(50)
            jennie.right(90)
            
        jennie.end_fill()
            
        #move the turtle to right side of the drawn square   
        jennie.forward(50)
    


def my_letter(x,y):
    """ (int,int) -> turtle
    Draw the first letter of my first name Z starting at x and y coordinate.
    >>> my_letter(0,0)
    >>> my_letter(10,10)
    >>> my_letter(-10,-10)
    """
    #create a turtle called lisa and change its speed
    lisa = turtle.Turtle()
    lisa.speed("fastest")
    lisa.hideturtle()
    
    #move the turtle to x and y coordinate
    lisa.penup()
    lisa.goto(x,y)
    lisa.pendown()
    
    #Draw letter "Z"
    lisa.forward(50)
    lisa.right(130)
    lisa.forward(75)
    lisa.left(130)
    lisa.forward(50)
    

    
def my_artwork():
    """ (NoneType) -> turtle
    Draw three shapes, one pattern in Chinese culture, a star, and a circular pattern.
    >>> my_artwork():
    """
    #draw shapes by calling functions
    yinyang_pattern()
    repetitive_circle(130,150)
    red_flag()
    colored_squares()
    my_letter(100,-100)




    