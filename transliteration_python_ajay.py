#pip install indic_transliteration
import tkinter #package for creating the GUI
from indic_transliteration import sanscript #package for transliteration
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from tkinter import *
 # 
win=Tk() #function for creating the Windo
win.geometry('400x250')
# dimensions of the window 
win.configure(bg='#ADD8E6')

win.title('Transliterator');
def f1(): # function for Malayalam transliteration
    x=e1.get(); 
    z=(transliterate(x, sanscript.HK, sanscript.MALAYALAM))
    l3.configure(text=z)
def f2():
    x=e1.get(); 
    z=(transliterate(x, sanscript.HK, sanscript.TAMIL))
    l3.configure(text=z)
def f3():
    x=e1.get(); 
    z=(transliterate(x, sanscript.HK, sanscript.KANNADA))
    l3.configure(text=z)
def f4():
    x=e1.get(); 
    z=(transliterate(x, sanscript.HK, sanscript.TELUGU))
    l3.configure(text=z)
l1=Label(win, text='Enter the text ',bg='#E5E482')#textbox ,color lavender
e1=Entry(width=12,bg='#EBF4FA')
l2=Label(win, text='Translated Text ')
l3=Label(win, text='',bg='#ADD8E6')
b1=Button(win, text=' English to Malayalam  ', command=f1,bg='#95B967')#BABYBLUE BUTTON COLOR
b2=Button(win, text=' English to Tamil  ', command=f2,bg='#CECECE')#BUTTON.PLATINUM SILVER COLOR
b3=Button(win, text=' English to Kannada', command=f3,bg='#AAF0D1')#BUTTON.lightyellow
b4=Button(win, text=' English to Telugu ',command=f4,bg='#CCCCFF')#BUTTON.coral blue
l1.pack(); e1.pack();  b1.pack();b2.pack();b3.pack();b4.pack();l2.pack();l3.pack();
win.mainloop()




