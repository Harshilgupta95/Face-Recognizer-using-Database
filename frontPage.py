from tkinter import *
from playsound import playsound
import os
root=Tk()

root.title('Face Recognizer')
root.configure(background='white')

def capRec():
    os.system('python captureRecord.py')

def train():
    os.system('python training.py')

def det():
    os.system('python Detect.py')

button = Button(root, text='Capture Record', width=25, command=capRec())
button = Button(root, text='Capture Record', width=25, command=capRec())
button = Button(root, text='Capture Record', width=25, command=capRec())

root.mainloop()
