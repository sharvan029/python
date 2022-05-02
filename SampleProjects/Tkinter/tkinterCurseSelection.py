from tkinter import *

root = Tk()
root.title('Python Guides')
root.geometry('400x300')
root.config(bg='#446644')


def showselected():
    itm = lb.get(lb.curselection())
    var.set(itm)


var = StringVar()
lb = Listbox(root)
lb.pack()

lb.insert(0, 'Iceland')
lb.insert(1, 'USA')
lb.insert(2, 'China')
lb.insert(3, 'Europe')

display = Label(root, textvariable=var)
display.pack(pady=20)
Button(root, text='Show Selected', command=showselected).pack()

root.mainloop()
