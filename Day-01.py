import turtle
import colorsys

# स्क्रीन सेटअप
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=700, height=700)
s.tracer(2)  # स्मूथ और फास्ट रेंडरिंग

t = turtle.Turtle()
t.speed(0)
t.width(1.5)
turtle.colormode(255)

hue = 0.0
wings = 4  # 4-विंग्ड सिमिट्री

for i in range(150):
    # रेनबो ग्रेडिएंट फ्लो
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    color = tuple(int(c * 255) for c in rgb)
    t.pencolor(color)
    
    # 4 विंग्स का डायनामिक मूवमेंट
    for _ in range(wings):
        t.forward(i * 0.8)
        t.circle(i * 0.4, 60)      # रिबन का कर्व
        t.left(120)
        t.circle(i * 0.2, 9)     # रिवर्स हुक (नया ट्विस्ट)
        t.left(360 / wings)        # अगले विंग का एंगल
    
    t.right(2)  # पूरे पैटर्न को धीरे-धीरे रोटेट करने के लिए
    hue += 0.04

t.hideturtle()
turtle.done()
