import turtle as tom
import random
L = tom.Turtle()
tom.colormode(255)
tom.width(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

L.speed("fastest")
def draw_spirograpf(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        L.color(random_color())
        L.circle(180)
        L.setheading(L.heading() + size_of_gap)

draw_spirograpf(5)


screen = tom.screen()
screen.exitonclick()
