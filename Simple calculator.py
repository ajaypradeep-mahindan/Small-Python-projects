from tkinter import *
#package for creating the GUI
win=Tk()
win.title('Simple Calculator');
def f1():
    x=e1.get(); y=e2.get();
    z=int(x)+int(y)
    l3.configure(text=z)
def f2():
    x=e1.get(); y=e2.get();
    z=int(x)-int(y)
    l3.configure(text=z)
def f3():
    x=e1.get(); y=e2.get();
    z=int(x)*int(y)
    l3.configure(text=z)
def f4():
    x=e1.get(); y=e2.get();
    z=int(x)/int(y)
    l3.configure(text=z)
l1=Label(win, text='Number1')
e1=Entry(width=8)
l2=Label(win, text='Number2')
e2=Entry(width=8)
l3=Label(win, text='Result')
b1=Button(win, text=' Add ', command=f1)
b2=Button(win, text='Substract', command=f2)
b3=Button(win, text=' Multiply', command=f3)
b4=Button(win, text='Divide', command=f4)
l1.pack(); e1.pack();l2.pack(); e2.pack(); b1.pack(); b2.pack(); b3.pack(); b4.pack();l3.pack();


