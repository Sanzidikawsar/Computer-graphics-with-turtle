import turtle as tt
import tkinter as ti
# tt.speed(10)

tt.penup()
tt.setpos(-300, 200)
tt.pendown()

tt.begin_fill()
for i in range(2):
    tt.fd(400)
    tt.rt(90)
    tt.fd(240)
    tt.rt(90)

tt.color("green")
tt.end_fill()

tt.penup()
tt.setpos(-100, 15)
tt.pendown()

tt.begin_fill()

tt.circle(70)

tt.color("red")
tt.end_fill()

tt.penup()
tt.setpos(0, 0)
tt.setpos(-300, 200)
tt.pendown()

tt.begin_fill()

for i in range(2):
    tt.rt(90)
    tt.fd(600)
    tt.rt(90)
    tt.fd(15)

tt.color("black")
tt.end_fill()

ti.mainloop()