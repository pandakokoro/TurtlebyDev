import turtle as t
import colorsys 
s = t.Screen()
s.bgcolor("grey")



for i in range(10):
    
    t.circle(5)
    t.left(115)
    t.forward(100)
    t.circle(5)
    t.right(25)
    t.backward(50)
    for i in range(2):
        t.circle(30)
        t.left(115)
        t.forward(100)
        t.circle(15)
        t.right(25)
        t.backward(50)
    
t.done()
