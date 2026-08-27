import turtle
import colorsys

# 1. स्क्रीन सेटअप
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=720, height=1280)
s.tracer(0)
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. विशाल गरुड़ विंग्स (Wide Feather Expansion)
hue_start = 0.08  # गोल्डन-ऑरेंज स्पेक्ट्रम

for i in range(180):
    rgb = colorsys.hsv_to_rgb((hue_start + (i * 0.0008)) % 1.0, 1.0, 1.0)
    t.pencolor(tuple(int(c * 255) for c in rgb))
    t.pensize(1)
    
    # राइट विंग आर्क
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(60 + (i * 0.2))
    t.circle(i * 2.2, 75)
    t.left(120)
    t.circle(i * 0.8, 60)
    
    # लेफ्ट विंग आर्क
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(120 - (i * 0.2))
    t.circle(-i * 2.2, 75)
    t.right(120)
    t.circle(-i * 0.8, 60)

# 3. सेंटर वैष्णव तिलक (Sacred Center)
t.pensize(5)
t.pencolor("#FFD700")

# U-Shape
t.penup()
t.goto(-22, 20)
t.pendown()
t.setheading(-90)
t.circle(22, 180)
t.forward(55)
t.penup()
t.goto(-22, 20)
t.pendown()
t.forward(55)

# सेंटर रेड तिलक लाइन
t.pensize(6)
t.pencolor("#FF2200")
t.penup()
t.goto(0, -10)
t.pendown()
t.goto(0, 85)

# 4. बॉटम टेक्स्ट
t.penup()
t.goto(0, -360)
t.pencolor("#FFDF00")
t.write("|| गुरुवार : ॐ नमो भगवते वासुदेवाय ||", align="center", font=("Arial", 18, "bold"))

s.update()
turtle.done()
