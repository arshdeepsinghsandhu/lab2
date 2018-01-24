import turtle
bob = turtle.Turtle()
def call(t):
    print(t)
    for i in range(4):
        t.fd(100)
        t.lt(90)
    
call(bob)
turtle.mainloop()
