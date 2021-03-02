import turtle

def main():
    filename = input('Please enter drawing filename:')
    t=turtle.Turtle()
    screen = t.getscreen()
    file = open(filename,'r')

    command = file.readline().strip() # first line

    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command=="circle":
            radius = float(file.readline())
            width  = float(file.readline())
            color  = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command=="beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command=="penup":
            t.penup()
        elif command=="pendown":
            t.pendown()
        else:
            print('Unknown command found in file:',command)
        command=file.readline().strip()

    file.close()
    t.ht() # hide turtle
    screen.exitonclick()
    print('Program execution completed')


if __name__ == "__main__":
    main()