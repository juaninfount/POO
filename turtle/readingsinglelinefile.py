# module turtle
import turtle

def main():
    # input from the user
    filename = input("Please enter drawing filename:")

    # 
    t = turtle.Turtle() # create a turtle graphics window    
    screen = t.getscreen()
    file = open(filename, 'r') # in text mode

    for line in file:
        text = line.strip() # eliminar caracteres espacio al inicio o fin de la linea
        commandList = text.split(",") # separar por comas
        command = commandList[0] # la primera palabra tiene el comando de trazado turtle

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])

            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width  = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:", command)

    file.close() # closing file
    t.ht() # hiding turtle
    screen.exitonclick()
    print('Program execution completed')


if __name__ == "__main__":
    main()