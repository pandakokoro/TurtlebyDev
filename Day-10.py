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

# 2. फूल की पंखुड़ियां और नेचुरल पैटर्न (Sunflower Logic)
num_petals = 60
t.penup()
t.goto(0, 50)  # थोड़ा ऊपर सेंटर सेट करने के लिए
t.pendown()

for i in range(num_petals):
    # नेचुरल गोल्डन शेड (पीला और नारंगी रंग)
    rgb = colorsys.hsv_to_rgb(0.12 + (i * 0.003), 1.0, 1.0)
    t.pencolor(tuple(int(c * 255) for c in rgb))
    t.pensize(2)
    
    t.circle(150, 60)
    t.left(120)
    t.circle(150, 60)
    t.left(360 / num_petals)

# 3. फूल का सेंटर कोर (Dark Center)
t.penup()
t.goto(0, 35)
t.pendown()
t.pencolor("#8B4513") # भूरा रंग
t.pensize(3)
for r in range(10, 50, 5):
    t.penup()
    t.goto(0, 50- r)
    t.pendown()
    t.circle(r)

# 4. नीचे फूल का नाम प्रिंट करना (Only Flower Name)
t.penup()
t.goto(0, -350)
t.pencolor("#FFD700")  # गोल्डन टेक्स्ट कलर
t.write("SUNFLOWER", align="center", font=("Arial", 28, "bold"))

s.update()
turtle.done()
