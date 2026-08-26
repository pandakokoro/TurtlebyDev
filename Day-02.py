import turtle
import colorsys

# 1. स्क्रीन सेटअप
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=800, height=800)
s.tracer(3)  # स्मूथ और फास्ट रेंडरिंग
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. बैकग्राउंड: बुधवार की ग्रीन-गोल्डन कॉस्मिक ऑरा (Divine Spiral Mandala)
hue = 0.25  # ग्रीन-येलो टोन
for i in range(180):
    rgb = colorsys.hsv_to_rgb((hue + i * 0.0015) % 1.0, 1.0, 1.0)
    t.pencolor(tuple(int(c * 255) for c in rgb))
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(i * 1.8)
    t.circle(i * 0.35, 90)
    t.left(89)

# 3. सेंटर आर्ट: पवित्र 'ॐ' / गणेश सिंबल (Golden Glow)
t.pensize(5)
t.pencolor("#FFD700")  # शुद्ध स्वर्ण रंग

# ॐ का ऊपरी कर्व
t.penup()
t.goto(-35, 30)
t.pendown()
t.setheading(90)
t.circle(-40, 200)

# ॐ का निचला लूप
t.setheading(-70)
t.circle(-45, 230)
t.circle(-20, 110)

# ॐ की दाहिनी पूँछ (Side Trunk Curve)
t.penup()
t.goto(-10, 5)
t.pendown()
t.setheading(10)
t.circle(-45, 110)
t.circle(35, 100)

# ॐ का अर्धचंद्र (Chandra)
t.penup()
t.goto(25, 95)
t.pendown()
t.setheading(-60)
t.circle(30, 120)

# ॐ का बिंदु (Bindu)
t.penup()
t.goto(40, 120)
t.pendown()
t.fillcolor("#FFD700")
t.begin_fill()
t.circle(6)
t.end_fill()

# 4. टाइटल
t.penup()
t.goto(0, -320)
t.pencolor("#FFDF00")
t.write("|| बुधवार : श्री गणेशाय नमः ||", align="center", font=("Arial", 16, "bold"))

turtle.update()
turtle.done()
