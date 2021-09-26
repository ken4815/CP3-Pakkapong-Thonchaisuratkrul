from tkinter import *
import math

def leftClickButton(event):
    text = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(text)
    if text >=30:
        labelResult.configure(text='Very fat')
    elif text <=29.9 and text >=25:
        labelResult.configure(text='Fat')
    elif text<=24.9and text >=23.0:
        labelResult.configure(text='Over weight')
    elif text <=22.9 and text >=18.6:
        labelResult.configure(text='Normal')
    elif text <=18.5:
        labelResult.configure(text='Under weight')


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)


MainWindow.mainloop()