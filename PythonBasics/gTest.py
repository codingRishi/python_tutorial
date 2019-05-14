import tkinter

from numpy.ma import column_stack

m = tkinter.Tk(className="rishi" )
m.title("Simple Calculator")
button = tkinter.Button(m,text="Add", width=20)
button.grid(row=0)
ckbutton = tkinter.Checkbutton(m,text="MAle")
ckbutton.grid(row=0, column=1)
tkinter.Entry(m,text="FN").grid(row=0, column=2)
tkinter.Label(m, text="FN").grid(row=6, column=3)


m.mainloop()