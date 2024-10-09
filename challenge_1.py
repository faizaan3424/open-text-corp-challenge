import sys, turtle

def displayTriangle(m, n):
    # Assumption: Right triangle with base = m units, height = n units.
    t = turtle.Turtle()

    # Scale factor to make the triangle visible
    scale = 50

    # Start at bottom left corner
    t.penup()           # Lift the pen so it doesn't draw
    t.goto(-200, -200)  # Move to bottom left corner
    t.pendown()         # Lower the pen to start drawing

    # Drawing the triangle
    t.forward(m * scale)    # Draw the base (m units)
    t.left(90)              # Turn left to draw the height
    t.forward(n * scale)    # Draw the height (n units)
    t.goto(-200, -200)            # Draw the hypotenuse back to the start

    turtle.done()

if __name__ == "__main__":
    assert len(sys.argv) == 3, "Usage: python challenge_1.py <base> <height>"
    displayTriangle(int(sys.argv[1]), int(sys.argv[2]))
