from tkinter import *
root = Tk()
root.title('Python Guides')
root.geometry('400x300')
root.config(bg='#446644')


def showselected():
    show.config(text=lb.get(ANCHOR))


lb = Listbox(root)
lb.pack()
lb.insert(0, 'red')
lb.insert(1, 'green')
lb.insert(2, 'yellow')
lb.insert(3, 'blue')

Button(root, text='Show Selected', command=showselected).pack(pady=20)

show = Label(root)
show.pack()
root.mainloop()