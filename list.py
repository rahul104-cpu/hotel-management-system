import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    NAME= details_list[0]
    ADDRESS = details_list[1]
    MOBILE_NO = details_list[2]
    ROOM_NO = details_list[3]
    PRICE = details_list[4]
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


class HOTEL_MANGMENT_checkin:
    def __init__(self):
        root = Tk()

        root.geometry("780x541+504+123")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="white")



        self.Labelframe1 = LabelFrame(root)
        self.Labelframe1.place(relx=0.01, rely=0.04, relheight=0.95, relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=("Bahnschrift Condensed",15,"bold"))
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text="LIST OF ALL GUEST")
        self.Labelframe1.configure(background="white")
        self.Labelframe1.configure(width=760)

        self.Frame1 = Frame(self.Labelframe1)
        self.Frame1.place(relx=0.03, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="gray85")
        self.Frame1.configure(width=355)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.28, rely=0.02, height=37, width=117)
        self.Label1.configure(activebackground="white")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="gray85",font=("Bahnschrift Condensed",15,"bold"))
        self.Label1.configure(foreground="black")
        self.Label1.configure(text="NAMES")

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text1.configure(background="white",font=("arial",15,"bold"))
        self.Text1.configure(foreground="black")
        self.Text1.configure(width=314)
        self.Text1.configure(wrap=WORD)



        self.Frame2 = Frame(self.Labelframe1)
        self.Frame2.place(relx=0.51, rely=0.1, relheight=0.86, relwidth=0.47, y=-31, h=15)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="gray85")
        self.Frame2.configure(width=355)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.37, rely=0.02, height=44, width=152)
        self.Label2.configure(activebackground="white")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="gray85",font=("Bahnschrift Condensed",15,"bold"))
        self.Label2.configure(foreground="black")
        self.Label2.configure(text='''ROOM NO.''')

        self.Text2 = Text(self.Frame2)
        self.Text2.place(relx=0.06, rely=0.16, relheight=0.8, relwidth=0.88)
        self.Text2.configure(background="white",font=("Bahnschrift Condensed",15,"bold"))
        self.Text2.configure(foreground="black")
        self.Text2.configure(width=314)
        self.Text2.configure(wrap=WORD)
        for i in range(0,len(G)):
            s=str(l2[i])
            h=str(G[i])
            self.Text1.insert(INSERT,s+"\n")
            self.Text2.insert(INSERT,h+"\n")


        root.mainloop()


if __name__ == '__main__':
    f2 = open("hotel.dat", "rb")
    try:
        while True:
            s = pickle.load(f2)
            k = s.room_no
            o = s.name.upper()
            l2.append(o)

            G.append(k)
            continue

    except EOFError:
        pass
    f2.close()
    hotel=HOTEL_MANGMENT_checkin()
