import os
import pickle

list1=[]
l2=[]
G = []
def file_save():
    NAME = list1[0]
    ADDRESS = list1[1]
    MOBILE_NO = list1[2]
    ROOM_NO = list1[3]
    PRICE = list1[4]
    f = open("hotel.dat", "ab")
    a=save(NAME,ADDRESS,MOBILE_NO,ROOM_NO,PRICE)
    pickle.dump(a,f,protocol=2)
    f.close()
    restart_program()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)






class save:
    def __init__(self, NAME, ADDRESS, MOBILE_NO, ROOM_NO, PRICE):
        self.name=NAME
        self.address=ADDRESS
        self.mobile_no=MOBILE_NO
        self.room_no=ROOM_NO
        self.price=PRICE
        print(self.name,self.address,self.mobile_no,self.room_no,self.price)

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


class HOTEL_MANAGEMENT:
    def __init__(self):
        def gotinfo():
            self.gettininfo = str(self.gather.get())
            print(self.gettininfo)
            print("\n")
            if self.gettininfo.isdigit() == True and len(self.gettininfo) != 0:
                self.Text1.insert(INSERT, "Valid room number ""\n")
            else :
                self.Text1.insert(INSERT,"Invalid room number""\n")

            try:
                n = 0
                f2 = open("hotel.dat", "rb")
                while True:
                    s = pickle.load(f2)
                    a = str(s.room_no)
                    print (a)
                    if self.gettininfo == a:
                        n = 1
                        print("\t""NAME -  ", s.name)
                        print("\t""ADDRESS -  ", s.address)
                        print("\t""MOBILE NO. -  ", s.mobile_no)
                        print("\t""HIS TOTAL BILL IS Rs. ", s.price)
                    elif EOFError:
                        if n == 0:
                            print("NO GUEST IN ROOM ", self.gettininfo)
                        else:
                            n = 0
                            continue
            except EOFError:
                pass
                f2.close()


        root = Tk()
        root.geometry("881x582+249+104")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="gray85")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="gray85")
        self.Frame1.configure(width=825)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.Text1.configure(background="white",font=("Bahnschrift Condensed",15),fg="red")
        self.Text1.configure(highlightbackground="yellow")
        self.Text1.configure(width=764)
        self.Text1.configure(wrap=WORD)



        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.22, rely=0.15, height=48, width=377)
        self.Label1.configure(background="gray85",font=("Bahnschrift Condensed",15,"bold"),fg="black")
        self.Label1.configure(text="ENTER ROOM NO.     : ")

        self.Entry1 = Entry(self.Frame1)
        self.gather=StringVar()
        self.Entry1.place(relx=0.60, rely=0.17,height=40, relwidth=0.1)
        self.Entry1.configure(background="light yellow")
        self.Entry1.configure(font="arial")
        self.Entry1.configure(foreground="red")
        self.Entry1.configure(width=84)
        self.Entry1.configure(textvariable=self.gather)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.39, rely=0.29, height=54, width=197)
        self.Button1.configure(activebackground="light green")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="green",cursor="hand2",border=0)
        self.Button1.configure(font=("Calibri"))
        self.Button1.configure(foreground="gray85")
        self.Button1.configure(text="SUBMIT")
        self.Button1.configure(command=gotinfo)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=("arial",20,"underline"))
        self.Message1.configure(foreground="black")
        self.Message1.configure(text="GET INFO HERE")
        self.Message1.configure(width=460)

        
        root.mainloop()



if __name__ == '__main__':
    GETINFO = HOTEL_MANAGEMENT()
