import turtle
t = turtle.Turtle()
def square(t,length):
    print(t)
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
square(t,200)
turtle.mainloop()

