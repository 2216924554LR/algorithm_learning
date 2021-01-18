import turtle

def drawSpiral(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen - 5)


# t = turtle.Turtle()
# drawSpiral(t, 100)
# turtle.done

def fractalTree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        fractalTree(branch_len - 15)
        t.left(40)
        fractalTree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

# t = turtle.Turtle()
# t.left(90)
# t.penup()
# t.backward(100)
# t.pendown()
# t.pencolor('green')
# t.pensize(2)
# fractalTree(75)
# t.hideturtle()
# turtle.done




