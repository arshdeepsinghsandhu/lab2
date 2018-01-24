import turtle
t = turtle.Turtle()
def circle(t,r,):
    n=100
    print(t)
    for i in range(n):
        t.fd((2*3.14*r)/n)
        t.lt(360/n)
    
circle(t,50)
turtle.mainloop()

