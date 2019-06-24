from tkinter import *
#from playsound import playsound
import os
from datetime import datetime;
root=Tk()

root.configure(background='white')

def capRec():
    os.system('C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe captureRecord.py')

def train():
    os.system('C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe training.py')

def det():
    os.system('C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe Detect.py')

def exit():
    root.destroy()

root.title('Face Recognizer')
Label(root,text='Face Recognizer',font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root, text='Capture Record',bg="#0D47A1",fg="white",command=capRec).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root, text='Train Model',bg="#0D47A1",fg="white",command=train).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root, text='Recognizer',bg="#0D47A1",fg="white",command=det).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)
Button(root, text='Exit',bg="#0D47A1",fg="white",command=exit).grid(row=6,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


root.mainloop()
