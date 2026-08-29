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

# 2. अल्ट्रा-डेंस कॉस्मिक मल्टी-लेयर कोर (500-Iteration Hyper-Matrix)
# यह डिज़ाइन स्क्रीन के छोटे से हिस्से (1/3 area) में सिमटकर भयंकर ऑप्टिकल इल्यूज़न बनाएगा।
layers = 5
for l in range(layers):
    hue_offset = l * 0.2
    steps = 100  # कुल मिलाकर लगभग 500 से ज्यादा इंटरनल ट्रैकिंग लूप्स
    
    for i in range(steps):
        # डायनामिक कलर्स और हाई-इम्पैक्ट ग्रेडिएंट्स
        rgb = colorsys.hsv_to_rgb((hue_offset + (i * 0.005)) % 1.0, 1.0, 1.0)
        t.pencolor(tuple(int(c * 255) for c in rgb))
        
        # लाइन की मोटाई और डिजाइन को कॉम्पैक्ट रखने के लिए माइक्रो-स्केलिंग
        t.pensize(1.2 if l % 2 == 0 else 0.8)
        
        # सेंटर से शुरू होकर स्क्रीन के 1/3 हिस्से में घूमने वाला भयंकर ज्योमेट्रिक पैटर्न
        angle = i * (360 / steps) + (l * 15)
        rad = math.radians(angle)
        
        # जटिल कोऑर्डिनेट और स्पाइरल मैस का गणितीय जाल
        x = math.cos(rad) * (i * 0.8)
        y = math.sin(rad) * (i * 0.8)
        
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        # माइक्रो-आर्क और स्पाइरल विजुअल्स जो आंखें चौंधिया दें
        t.forward(i * 0.5)
        t.circle(i * 0.2, 75)
        t.left(123)
        t.circle(-i * 0.3, 45)
        t.backward(i * 0.3)

s.update()
turtle.done()
