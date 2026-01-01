import turtle
turtle.penup()
for i in range(1, 200, 15):
    turtle.right(90)    # Face South
    turtle.forward(i)   # Move one radius
    turtle.right(270)   # Back to start heading
    turtle.pendown()    # Put the pen back down
    turtle.circle(i)    # Draw a circle
    turtle.penup()      # Pen up while we go home
    turtle.home()       # Head back to the start pos