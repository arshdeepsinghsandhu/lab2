import turtle
t = turtle.Turtle()
def polygon(t,length,n):
    print(t)
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    
polygon(t,50,6)
turtle.mainloop()
