import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.colormode(255)

n = 36  # लेयर्स की संख्या
hue = 0.0

for i in range(145):
    # डायनामिक कलर जनरेशन (HSV to RGB)
    rgb = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    color = tuple(int(c * 255) for c in rgb)
    t.pencolor(color)
    
    # शेप लॉजिक: आगे बढ़कर एक अनोखा कर्व बनाना
    t.circle(i * 1.5, 90)
    t.left(98)
    t.circle(i * 0.8, -90)
    t.right(45)
    
    hue += 0.008

t.hideturtle()
turtle.done()
