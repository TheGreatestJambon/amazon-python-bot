import tkinter
import Globals, Store
import tkinter.messagebox
from tkinter import Tk
from tkinter import *
import time
from sys import exit


top = Tk()
top.geometry("350x200")
top.title('Amazon Bot')

Item_ID = Label(top, text = "Item_ID").place(x = 20, y = 40)
Price_ID = Label(top, text = "Max Price").place(x = 20, y = 70)
User_ID = Label(top, text = "User_ID").place(x = 20, y = 100)
Password = Label(top, text = "Password").place(x = 20, y = 130)

x = tkinter.StringVar()
Item_Entry = tkinter.Entry(top, textvariable=x)
Item_Entry.place(x=80, y=40)
p = tkinter.StringVar()
Price_Entry = tkinter.Entry(top, textvariable=p)
Price_Entry.place(x=80, y=70)
y = tkinter.StringVar()
User_Entry = tkinter.Entry(top, textvariable=y)
User_Entry.place(x=80, y=100)
z = tkinter.StringVar()
Pass_Entry = tkinter.Entry(top, textvariable=z)
Pass_Entry.place(x=80, y=130)

labelResult = tkinter.Label(top)
labelResult.place(x=140, y=160)
labelResult.config(text="Please enter your details.")


# Verify and submit user information
def Submit_info():
    User_Fmt = f'{User_Entry=}'.split('=')[0]
    User_Get = User_Entry.get()
    Price_Fmt = f'{Price_Entry=}'.split('=')[0]
    Price_Get = Price_Entry.get()
    Pass_Fmt = f'{Pass_Entry=}'.split('=')[0]
    Pass_Get = Pass_Entry.get()
    URL_Fmt = f'{Item_Entry=}'.split('=')[0]
    URL_Get = Item_Entry.get()

    Arr_Test = [User_Fmt, User_Get, Price_Fmt, Price_Get, Pass_Fmt, Pass_Get, URL_Fmt, URL_Get]
    final = []

    if User_Get == "" or Price_Get == "" or Pass_Get == "" or URL_Get == "":
        for i in Arr_Test:
            if not i == "":
                temp = i
            else:
                final.append(temp)
                labelResult.config(bg='red')
                top.geometry("440x200")
        change = ', '.join(final)
        labelResult.config(text="Please fill out: " + change)

    elif not Price_Get.isdigit():
        labelResult.config(bg='red')
        labelResult.config(text="Max price in numerical form only")
    else:
        Globals.USER = User_Get
        Globals.PRICE_LIMIT = float(Price_Get)
        Globals.PASS = Pass_Get
        Globals.URL = URL_Get
        Item_Entry.delete(0, END)
        Price_Entry.delete(0, END)
        User_Entry.delete(0, END)
        Pass_Entry.delete(0, END)
        top.destroy()


# Kill the program if the X button is clicked
def doSomething():
    top.destroy()
    exit()


Submit = tkinter.Button(top, text="Submit", command= Submit_info)
Submit.place(x=80, y=160)
top.protocol('WM_DELETE_WINDOW', doSomething)


top.mainloop()
