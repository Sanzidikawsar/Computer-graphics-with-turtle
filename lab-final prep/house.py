import turtle as tt
import tkinter as ti
tt.speed(10)

tt.begin_fill()
for i in range(2):
    tt.fd(200)
    tt.rt(135)
    tt.fd(80)
    tt.rt(45)

tt.color("black")
tt.end_fill()

tt.penup()
tt.fd(200)
tt.pendown()

tt.begin_fill()
tt.rt(45)
tt.fd(80)
tt.rt(135)

tt.penup()
tt.fd(115)
tt.pendown()

tt.color("yellow")
tt.end_fill()

tt.begin_fill()
for i in range(2):
    tt.fd(200)
    tt.lt(90)
    tt.fd(170)
    tt.lt(90)

tt.color("green")
tt.end_fill()

tt.begin_fill()
tt.bk(115)
tt.lt(90)
tt.fd(150)
tt.rt(80)
tt.fd(118)

tt.color("red")
tt.end_fill()

ti.mainloop()