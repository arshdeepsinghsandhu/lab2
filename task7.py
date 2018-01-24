import turtle
t = turtle.Turtle()
def circle(t,r,angle):
    n=100
    print(t)
    for i in range(n):
        t.fd((2*3.14*r*angle)/(n*360))
        t.lt(angle/n)
    
circle(t,150,270)
turtle.mainloop()



#r=radius of circle
#angle=detemines what fraction of circle to draw
#in this case 3/4 circle(270/360) is drawn with radius 150


