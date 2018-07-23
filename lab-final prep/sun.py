import turtle as tt
import tkinter as ti
tt.speed(10)

tt.begin_fill()

tt.circle(100)

tt.color("yellow")
tt.end_fill()

tt.penup()
tt.setpos(0, 100)
tt.pendown()

tt.pencolor("black")
for i in range(8):
    tt.penup()
    tt.fd(100)
    tt.pendown()
    tt.fd(100)

    tt.penup()
    tt.setpos(0, 100)
    tt.pendown()
    tt.rt(45)

ti.mainloop()