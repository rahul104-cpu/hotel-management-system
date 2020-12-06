import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "checkin.py"])
def click_list():
    call(["python", "list.py"])
def click_checkout():
    call(["python", "checkout.py"])
def click_getinfo():
    call(["python","get_info.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()


        root.geometry("1190x700+100+50")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="gray15")
        root.resizable(False,False)



        self.menubar = Menu(root)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="dark slate gray")
        self.Frame1.configure(width=925)


        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.05, rely=0.02, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="dark slate gray",font=("arial",25,"underline","bold"))
        self.Message6.configure(foreground="white")
        self.Message6.configure(text="WELCOME TO LOVELY RESORT")
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.28, rely=0.25, height=73, width=456)
        self.Button2.configure(activebackground="dark red")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(background="red",font=("arial",18,"bold"),cursor="hand2",fg="white")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="1. CHECK INN")
        self.Button2.configure(width=456)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.28, rely=0.37, height=73, width=456)
        self.Button3.configure(activebackground="orange")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(background="yellow",font=("arial",18,"bold"),cursor="hand2",fg="white")
        self.Button3.configure(pady="0")
        self.Button3.configure(text="2. SHOW GUEST LIST")
        self.Button3.configure(width=456)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.28, rely=0.49, height=73, width=456)
        self.Button4.configure(activebackground="light green")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(background="green",font=("arial",18,"bold"),cursor="hand2",fg="white")
        self.Button4.configure(pady="0")
        self.Button4.configure(text="3. CHECK OUT")
        self.Button4.configure(width=456)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.28, rely=0.61, height=73, width=456)
        self.Button5.configure(activebackground="mediumblue")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(background="blue4",font=("arial",18,"bold"),cursor="hand2",fg="white")
        self.Button5.configure(pady="0")
        self.Button5.configure(text="4. GET INFO OF ANY GUEST")
        self.Button5.configure(width=456)
        self.Button5.configure(command=click_getinfo)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.28, rely=0.73, height=73, width=456)
        self.Button6.configure(activebackground="red")
        self.Button6.configure(activeforeground="white")
        self.Button6.configure(background="maroon",font=("arial",18,"bold"),cursor="hand2",fg="white")
        self.Button6.configure(pady="0")
        self.Button6.configure(text="5. EXIT")
        self.Button6.configure(width=456)
        self.Button6.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUEST=HOTEL_MANAGEMENT()


