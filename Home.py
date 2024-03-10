#!usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('220x200')
window.resizable(False, False)
window.title('Home')
'''for i in range(6):
    time.sleep(1)
    print(f'加载中......{5 - i}秒')
'''
title = tkinter.Label(window, text='Home', fg='red', anchor='center', bd=2)
title.pack()

def quit():
    exit()

q = tkinter.Button(window, text='Quit', fg='black', bg='yellow', command=quit)
q.pack()

str_ = tkinter.StringVar()

on_str_ = False
l = tkinter.Label(window, textvariable=str_)
l.pack()
def dstr_():
    global on_str_
    if on_str_ == False:
        on_str_ = True
        str_.set('↑')
    else:
        on_str_ = False
        str_.set('')

bstr = tkinter.Button(window, text='Hint', fg='black', bg='yellow', command=dstr_)
bstr.pack()

#学习
entry = tkinter.Entry(window, font=("宋体", 25), fg='red')
entry.pack()


window.mainloop()