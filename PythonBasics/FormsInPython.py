import tkinter
from tkinter import *



def on_Button_click():
    print(editbox1.get())


m = tkinter.Tk()
m.title("Simple Calculator")
button = tkinter.Button(m,text="Add",command=on_Button_click)
button.grid(row=2, column=0)
label1 = tkinter.Label(m, text="UserName")
label1.grid(row=0, column=0)
editbox1 = tkinter.Entry(m, width=5)
editbox1.grid(row=0, column=1)
tkinter.Label(m, text="Password").grid(row=1, column=0)
editbox2 = tkinter.Entry(m)
editbox2.grid(row=1,column = 1)




m.mainloop()



