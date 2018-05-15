import turtle as tt
import tkinter as ti

#initially position is like- ->

#go forward
tt.fd(100)

#go backward
tt.bk(50)

#make angle in left
tt.lt(90)

#then again forward
tt.fd(100)

#make angle in right
tt.rt(135)

#then again forward
tt.fd(100)

#to see position in x-y axis
print(tt.pos())

ti.mainloop()   #tkinter for staying the window untill exit