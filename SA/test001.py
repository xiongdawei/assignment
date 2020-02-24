import turtle
t = turtle.Turtle()
t.speed(5)

def climb(length,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x-length/2,y)
    t.goto(x-length/2,y+length)
    t.goto(x-length/2,y-length)
    t.goto(x-length/2,y)
    t.goto(x+length/2,y)
    t.goto(x+length/2,y+length)
    t.goto(x+length/2,y-length)
    t.goto(x+length/2,y)
    t.goto(x,y)

    lu,ld,ru,rd = (x-length/2,y+length), (x-length/2,y-length),(x+length/2,y+length),(x+length/2,y-length)
    if length>=25:
        climb(length/2,lu[0],lu[1])
        climb(length/2,ld[0],ld[1])
        climb(length/2,ru[0],ru[1])
        climb(length/2,rd[0],rd[1])

climb(100,0,0)






