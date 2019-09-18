#fronted.py
#import backend
#from backend import phepcong
#phepcong(1,2)
from tkinter import * # thu vien lam giao dien
import backend
window=Tk() #Tao doi tuong cua thu vien tkinter
window.wm_title("Auto nuoi Fage")

def love():
	print('love')
#	backend.love(my_entry.get())

def hello():
	print(my_entry.get())
	# backend.hello(my_entry.get())
	# print('hello')
#	backend.hello(my_entry.get())

def haha():
	print('haha')
#	backend.haha(my_entry.get())
my_label = Label(window, text = "Nhap ten:")
my_label.grid(row = 0, column = 0)

my_entry = Entry(window)
my_entry.grid(row = 0, column = 1)

b1=Button(window,text="   love", width=25, height=10, command=love)
b1.grid(row=1, column=1)
b2=Button(window,text="   hello", width=25, height=10, command=hello)
b2.grid(row=1, column=2)
b3=Button(window,text="   haha", width=25, height=10, command=haha)
b3.grid(row=2, column=1)

window.mainloop()