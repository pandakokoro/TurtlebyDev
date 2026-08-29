import turtle
import colorsys

# 1. स्क्रीन सेटअप (9:16 Reel Ratio)
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=720, height=1280)
# tracer(10, 1) का मतलब है कि यह बहुत सारे स्टेप्स को बहुत ही स्मूथ और धीमी गति से रेंडर करेगा
s.tracer(100, 1)
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 2. महा-ऑर्गेनाइज्ड कॉस्मिक मंडला (5 से 10 मिनट तक चलने वाला डीप लेयर स्ट्रक्चर)
total_layers = 1
shapes_per_layer = 455

for layer in range(total_layers):
    hue_offset = layer * 0.15
    
    for i in range(shapes_per_layer):
        # हर लेयर के साथ शानदार कलर शिफ्ट
        rgb = colorsys.hsv_to_rgb((hue_offset + (i * 0.001)) % 1.0, 1.0, 1.0)
        t.pencolor(tuple(int(c * 255) for c in rgb))
        
        # लेयर के हिसाब से लाइन की मोटाई सेट करना ताकि डिजाइन साफ दिखे
        t.pensize(0.001 if layer % 2 == 0 else 1.0)
        
        # सिमेट्रिकल ज्योमेट्रिक रोटेशन
        t.penup()
        t.goto(0, 0)
        t.setheading(i * (360 / shapes_per_layer) + (layer * 1.1))
        t.pendown()
        
        # लंबा और ऑर्गेनाइज्ड पाथ जो धीरे-धीरे ड्रा होगा
        forward_dist = 80 + (layer * 45) + (i * 0.4)
        t.forward(forward_dist)
        
        # जटिल और सुव्यवस्थित आर्च्स
        t.circle(40 + (layer * 15), 90)
        t.left(121)
        t.forward(forward_dist * 0.4)
        t.circle(-30, 60)
        t.right(45)

s.update()
turtle.done()
