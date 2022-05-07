import tkinter as tk
import tkinter.messagebox as tkm
m = tk.Tk()
m.title('Counting Seconds')
button = tk.Button(m, text='Stop', width=25, command=m.destroy)
button.pack()


def hellocallback():
    tkm.showinfo("Hello Python", "Hello World")


B = tk.Button(m, text="Click here", bg="Red", activebackground="Blue", command= hellocallback)

B.pack()
m.mainloop()

'''
widgets will be added here
'''
