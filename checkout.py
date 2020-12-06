import os
import pickle

details_list=[]
l2=[]
G = []
def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
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



class New_Toplevel:

    def __init__(self):
        def check_room():
            self.rom = str(self.data.get())
            print(self.rom)
            print("\n")
            if self.rom.isdigit() == True and len(self.rom) != 0:
                self.Text1.insert(INSERT, "Valid room number ""\n")
                v = int(self.rom)
                f = open("hotel.dat", "rb")
                f1 = open("hote.dat", "ab")
                n = 0
                try:
                    while True:
                        s = pickle.load(f)
                        if s.room_no == v:
                            n = 1
                            name1 = s.name

                            print(" ")
                        else:
                            pickle.dump(s, f1)
                except EOFError:
                    if n == 0:
                        self.Text1.insert(INSERT, "NO GUEST FOUND""\n")

                    elif n == 1:

                        self.Text1.insert(INSERT, "THANK YOU  " + name1.upper() + " FOR VISTING US""\n")
                    pass
                f.close()
                f1.close()
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")

            else:
                self.Text1.insert(INSERT, "Invalid input please input a valid ROOM NO.""\n")



        root = Tk()
        root.geometry("1011x750")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="white")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="mint cream")
        self.Frame1.configure(width=925)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(background="mint cream",font=("arial",20,"bold"),fg="black")
        self.Label1.configure(text="ENTER THE ROOM NO.   :")

        self.Entry1 = Entry(self.Frame1)
        self.data=StringVar()
        self.Entry1.place(relx=0.67, rely=0.12,height=44, relwidth=0.07)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font=("alako",15,"bold"))
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(textvariable=self.data)




        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="light yellow")
        self.Text1.configure(font=("Calibri",15,"bold"))
        self.Text1.configure(foreground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.4, rely=0.35, height=50, width=200)
        self.Button1.configure(activebackground="maroon")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(background="red")
        self.Button1.configure(font=("arial"))
        self.Button1.configure(foreground="white")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="CHECK OUT")
        self.Button1.configure(command=check_room)
        root.mainloop()



if __name__ == '__main__':
    out = New_Toplevel()
