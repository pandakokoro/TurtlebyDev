import turtle
import colorsys
import math

# 1. स्क्रीन सेटअप (9:16 Reel Ratio)
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=720, height=1280)
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. ठीक 20 राउंड्स का प्रिसिजन कॉस्मिक मंडला
rounds = 12
for i in range(rounds):
    # डायनामिक ग्रेडिएंट कलर्स
    rgb = colorsys.hsv_to_rgb((i * 0.05) % 1.0, 1.0, 1.0)
    t.pencolor(tuple(int(c * 255) for c in rgb))
    t.pensize(2)
    
    angle = i * (360 / rounds)
    rad = math.radians(angle)
    
    distance = i * 1
    x = math.cos(rad) * distance
    y = math.sin(rad) * distance
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # 20 राउंड्स के लिए क्लीन और शार्प ज्योमेट्रिक पेटल्स
    t.circle(90, 180)
    t.left(150)
    t.circle(90, 180)

s.update()
turtle.done()
