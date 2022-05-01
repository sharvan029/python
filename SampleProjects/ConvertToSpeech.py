from tkinter import *
from gtts import gTTS
from playsound import playsound
import pyttsx3
import os

root = Tk()
root.geometry("350x300")
root.configure(bg='ghost white')
root.title('Text To Speech')
Label(root, text='Text to speech', font='arial 20 bold', bg='yellow').pack()
Label(text='May 2022', font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')
Msg = StringVar()
Label(root, text='Enter text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)
entry_field = Entry(root, textvariable=Msg, width=50)
entry_field.place(x=20, y=100)

'''
def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save(f'{message}.mp3')
    playsound(f'{message}.mp3')
    os.remove(f'{message}.mp3')
'''


def text_to_speech():
    message = entry_field.get()
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


def exit():
    root.destroy()


def reset():
    Msg.set("")


Button(root, text='PLAY', font='arial 15 bold', command=text_to_speech, width='4').place(x=25, y=140)
Button(root, font='arial 15 bold', text='EXIT', width='4', command=exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, font='arial 15 bold', text='RESET', width='6', command=reset).place(x=175, y=140)
root.mainloop()