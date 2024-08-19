import turtle
t = turtle.Pen()

def estrella(tam):
    t.reset()
    for i in range(8):
        t.forward(tam)
        t.right(135)

estrella(100)

def estrella2(tam):
    t.reset()
    for i in range (37):
        t.forward(tam)
        t.left(175)

estrella2(100)

def estrella3(tam):
    t.reset()
    for i in range (19):
        t.forward(tam)
        t.left(95)

estrella3(100)

def estrella4(tam):
    t.reset()
    for i in range(9):
        t.forward(tam)
        t.left(175)
        t.forward(tam)
        t.right(135)
estrella4(100)