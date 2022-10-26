import turtle as tl

tl.setup(900, 800)
tl.setpos(0, 0)
tl.speed(20)
size = 200



def draw_triangle(size):
    for i in range(3):
        tl.lt(120)
        tl.fd(size)

def draw_fractal(size):
    if size > 10:
        for i in range(3):
            draw_triangle(size)
            tl.penup()
            tl.lt(120)
            tl.fd(size * 2)
            tl.pendown()
        draw_fractal(size / 2)
            

for i in range(6):
    tl.seth(-120 + 60 * (i))
    draw_fractal(size)

tl.exitonclick()