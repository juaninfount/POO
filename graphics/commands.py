import turtle

"""
Polymorphism: call the right behaviour when a sequence of commands
"""
class GoToCommand:
    def __init__(self,x,y,width=1.0,color="black"):
        self._x = x
        self._y = y        
        self._width = width
        self._color = color

    def draw(self,turtle):
        turtle.width(self._width) 
        turtle.pencolor(self._color)
        turtle.goto(self._x, self._y)

class CircleCommand:
    def __init__(self, radius, width=1.0,color="black"):
        self._radius = radius
        self._width = width
        self._color = color

    def draw(self, turtle):
        print("width: %s, color: %s, radius: %s" %(str(self._width),str(self._color),str(self._radius)) )
        turtle.width(self._width)
        turtle.pencolor(self._color)
        turtle.circle(self._radius)

class BeginFillCommand:
    def __init__(self,color):
        self._color = color
    
    def draw(self, turtle):
        turtle.fillcolor(self._color)
        turtle.begin_fill()

class EndFillCommand:
    def __init__(self):
        pass    

    def draw(self, turtle):
        turtle.end_fill()

class PenUpCommand:
    def __init__(self):
        pass        

    def draw(self, turtle):
        turtle.penup()

class PenDownCommand:
    def __init__(self):
        pass        

    def draw(self, turtle):
        turtle.pendown()

if __name__ == "__main__":
    pass        