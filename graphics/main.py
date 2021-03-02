import turtle
import commands

# accumulator pattern
class PyList:
    
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c # producir item c en items

def main():
    line = 1
    filename = input('Please enter drawing filename:')
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, 'r')

    graphicsCommands = PyList()
    command = file.readline().strip()
    print('line %i - command: %s' % (line,command))
    line +=1

    while command != "":        
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()                  
            print('line %i - command: %s' % (line,command))
            line +=1
            command = commands.GoToCommand(x,y,width,color)            
        elif command == "circle":
            radius = float(file.readline())
            width  = float(file.readline())
            color  = file.readline().strip()
            print('line %i - command: %s' % (line,command))
            line +=1
            command = commands.CircleCommand(radius, width, color)  
        elif command=="beginfill":
            color = file.readline().strip()
            print('line %i - command: %s' % (line,command))
            line +=1
            command = commands.BeginFillCommand(color)
        elif command=="endfill":            
            command = commands.EndFillCommand()            
        elif command=="penup":
            command = commands.PenUpCommand()
        elif command=="pendown":
            command = commands.PenDownCommand()
        else:
            raise RuntimeError('Unknown command found in file:',command)
        graphicsCommands.append(command)
        command=file.readline().strip()
        print('line %i - command: %s' % (line,command))
        line +=1

    for cmd in graphicsCommands:        
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print('Program Execution Completed')

if __name__ == "__main__":
    main()    