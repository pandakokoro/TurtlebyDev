import turtle
import colorsys

# 1. स्क्रीन सेटअप
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=720, height=1280)
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. बैकग्राउंड: फेस्टिव ऑरा स्पाइरल (Red & Gold Glow)
for i in range(160):
    rgb = colorsys.hsv_to_rgb((0.08 + i * 0.001) % 1.0, 1.0, 1.0)
    t.pencolor(tuple(int(c * 255) for c in rgb))
    t.pensize(1)
    t.penup()
    t.goto(0, 30)
    t.pendown()
    t.forward(i * 1.3)
    t.circle(i * 0.3, 75)
    t.left(89)

# 3. वेवी रेशमी धागा + मोती (Left & Right Silk Threads)
def draw_wavy_thread(start_x, start_y, direction):
    t.pensize(4)
    # रेड धागा
    t.pencolor("#FF1E27")
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.setheading(0 if direction == 1 else 180)
    for i in range(14):
        t.circle(direction * 18, 90)
        t.circle(-direction * 18, 90)

    # गोल्डन बीड्स (मोती) धागे के ऊपर
    t.pencolor("#FFD700")
    t.pensize(2)
    for step in range(1, 6):
        bx = start_x + (direction * step * 48)
        by = start_y + (12 if step % 2 == 0 else -12)
        t.penup()
        t.goto(bx, by)
        t.pendown()
        t.fillcolor("#FFD700")
        t.begin_fill()
        t.circle(5)
        t.end_fill()

# बायाँ और दायाँ धागा
draw_wavy_thread(-90, 30, -1)
draw_wavy_thread(90, 30, 1)

# 4. सेंटर आर्ट: गोल्डन कॉइन (पैसा राखी डायल)
t.penup()
t.goto(0, -60)
t.pendown()
t.pensize(5)
t.pencolor("#FF8C00")
t.fillcolor("#FFD700")
t.begin_fill()
t.circle(90)
t.end_fill()

# कॉइन की इनर रिम और डिजाइन
t.penup()
t.goto(0, -48)
t.pendown()
t.pensize(3)
t.pencolor("#B8860B")
t.circle(78)

# कॉइन के चारों तरफ फ्लोरल पेटल्स
for k in range(16):
    t.penup()
    t.goto(0, 30)
    t.setheading(k * (360 / 16))
    t.forward(88)
    t.pendown()
    t.fillcolor("#FF2200")
    t.pencolor("#FFD700")
    t.begin_fill()
    t.circle(7)
    t.end_fill()

# 5. कॉइन के अंदर टेक्स्ट
t.penup()
t.goto(0, 0)
t.pencolor("#8B0000")
t.write("बहना", align="center", font=("Arial", 18, "bold"))

# 6. बॉटम हेडर
t.penup()
t.goto(0, -360)
t.pencolor("#FFDF00")
t.write("|| Happy Raksha Bandhan ||", align="center", font=("Arial", 8, "bold"))

s.update()
turtle.done()
