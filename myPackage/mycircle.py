
import turtle

def draw_circle(t, x, y, radius=50):

    t.penup()

    t.goto(x, y - radius)
    t.pendown()
    t.setheading(0)

    t.circle(radius)