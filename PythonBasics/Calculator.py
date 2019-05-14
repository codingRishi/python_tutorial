import tkinter
import math

def on_click_add():
    x = int(add_Num1.get())
    y = int(add_Num2.get())
    print("Addition : " , (x+y))



def put_result():

    #my_panel.setvar("6", result_value)
    x = int(add_Num1.get())
    y = int(add_Num2.get())
    print("Addition : ", (x + y))
    result_value.delete(0,str(x+y))
    result_value.insert(0,str(x+y))



my_panel = tkinter.Tk()
my_panel.title("Simple Calculator")
add_label1 = tkinter.Label(my_panel,text="Number 1 : ").grid(row=0, column=0)
add_Num1 = tkinter.Entry(my_panel)
add_Num1.grid(row=0, column=1)
add_label2 = tkinter.Label(my_panel,text="Number 2 : ").grid(row=1, column=0)
add_Num2 = tkinter.Entry(my_panel)
add_Num2.grid(row=1, column=1)
add_button = tkinter.Button(my_panel, text="Add", command=put_result).grid(row=2, column=1)
#add_button = tkinter.Button(my_panel, text="Result", command=put_result).grid(row=3, column=1)
result_label1 = tkinter.Label(my_panel,text="Result : ").grid(row=3, column=0)
result_value = tkinter.Entry(my_panel)
result_value.grid(row=3, column=1)

my_panel.mainloop()


