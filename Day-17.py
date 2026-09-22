import turtle as t
import colorsys 
s = t.Screen()
s.bgcolor("grey")



for i in range(100):
    t.speed(100)
    
    
    t.left(115)
    t.forward(100)
    
    t.right(25)
    t.backward(20)
    t.right(25)
    t.backward(50)
    for i in range(1):
        
        t.left(35)
        t.forward(100)
        
        t.right(125)
        t.backward(50)
        
        
        t.left(105)
        t.forward(100)
        
        t.right(15)
        t.backward(50)
    
t.done()
