# -------------------------------------------------------------------------------
# Name:        App.py
# Project:     CA_Lab1
#
# Author:      Vitaliy Baseckas
#
# Created:     11.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

from tkinter import *
root=Tk()

def print_message():
    c=Label(root,text="Hi DevOps",font=("Courier", 35))
    c.place(x=10,y=10)

root.title('Hello DevOps')
root.geometry("300x200+10+20")

a=Button(root,text="Press Me",command=print_message)
a.place(relx=0.38,rely=0.4,)
b=Button(root,text="Close me",command=root.destroy)
b.place(relx=0.38,rely=0.7,)

root.mainloop()