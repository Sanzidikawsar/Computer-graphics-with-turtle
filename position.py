import turtle as tt
import tkinter as ti

#see present position
tp = tt.pos()
print(tp)

#set custom position by x-y axis
tt.setpos(60, 100)

#go to custom position by x-y axis
tt.setx(100)
tt.sety(-100)

#go to the place from where was started
tt.home()
print(tt.pos())

ti.mainloop()