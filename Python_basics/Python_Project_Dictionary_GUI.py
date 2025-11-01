from cProfile import label
from cgitb import text
from operator import truediv
from textwrap import fill
from tkinter import *
root =  Tk()
head = Label(root,text="Python Dictionary",bg="red",fg="white")
label1  =Label(root,text="Entry Text:")
head.pack(fill=X)
label1.pack(fill=Y)
ent = StringVar()
ent =Entry(root,textvariable=ent)
ent.pack()
t=Text(root)
t.pack(fill=X)

root.mainloop()