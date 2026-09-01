import turtle
import colorsys
import math

# 1. स्क्रीन सेटअप (9:16 Reel Ratio)
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=720, height=1280)
s.tracer(10, 1)  # स्मूथ और डेंस रेंडरिंग के लिए
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. हाइपर-डेंस कॉस्मिक वोर्टेक्स मैट्रिक्स (Masterpiece Turtle Art)
total_layers = 5
steps_per_layer = 150

for layer in range(total_layers):
    hue_offset = layer * 0.2
    
    for i in range(steps_per_layer):
        # डायनामिक ग्रेडिएंट कलर्स (रेत, नियोन और गोल्ड का कॉम्बिनेशन)
        rgb = colorsys.hsv_to_rgb((hue_offset + (i * 0.004)) % 1.0, 1.0, 1.0)
        t.pencolor(tuple(int(c * 255) for c in rgb))
        
        t.pensize(1.2 if layer % 2 == 0 else 0.8)
        
        # मैथमेटिकल कॉर्डिनेट्स फॉर सेंटर-फोक्स्ड कॉम्पैक्ट डिज़ाइन
        angle = i * (360 / steps_per_layer) + (layer * 12)
        rad = math.radians(angle)
        
        distance = i * 0.7 + (layer * 15)
        x = math.cos(rad) * distance
        y = math.sin(rad) * distance
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        # जटिल और सेटिस्फाइंग टर्टल कर्व्स
        t.forward(i * 0.9)
        t.circle(i * 0.69, 1)
        t.left(25)
        t.circle(-i * 0.15, 50)
        t.backward(i * 0.2)
        t.right(125)
        t.forward(i * 0.3)
        t.circle(i * 0.69, 1)
        t.left(125)
        t.circle(-i * 50, 0.15)
        t.backward(i * 0.1)
        t.right(25)

s.update()
turtle.done()
