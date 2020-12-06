
import os
import pickle
import sys
from subprocess import call

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

list1=[]

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
    listq=[str(NAME),str(ADDRESS),str(MOBILE_NO),str(ROOM_NO),str(PRICE)]
    myVars = {'A':NAME,"B":ADDRESS,"C":MOBILE_NO,"D":ROOM_NO,"E":PRICE}

    fo=open("recipt.txt","w+")
    for h in range(0,5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])
    restart_program()


u = list()
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
General = (21,22,23,24,25,26, 27, 28, 29, 30, 31, 32)
Joint_Room = (33,34,35,36,37,38,39,40,41,42,43,44,45)
m = [9]
G = []
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


class save:
    def __init__(self,NAME,ADDRESS,MOBILE_NO,ROOM_NO,PRICE):
        self.name=NAME
        self.address=ADDRESS
        self.mobile_no=MOBILE_NO
        self.room_no=ROOM_NO
        self.price=PRICE

class checkin:
    def __init__(self):
        self.NAME=""
        self.ADDERESS=""
        self.MOBILE=""
        self.DAYS=0
        self.price=0
        self.room=0


        def chk_name():
            while True:
                self.k = str(self.name.get())

                a = self.k.isdigit()
                if len(self.k) != 0 and a != True:
                    self.NAME=self.k
                    self.Text1.insert(INSERT, "Name has been inputed successfully""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input!!""\n""Please input a valid name""\n")
                    break

        def chk_add():
            while True:
                self.g = str(self.addr.get())


                ak = self.g.isdigit()
                if len(self.g)!= 0 and ak!=True:
                    self.ADDERESS=self.g
                    self.Text1.insert(INSERT, "Address has been inputed successfully""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input!!""\n""Please input a valid address""\n")
                    break

        def chk_mob():
            while True:

                self.h = str(self.mobile.get())
                if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                    self.MOBILE = self.h
                    self.Text1.insert(INSERT, "Mobile number has been inputed successfully""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input!!""\n""Please input a valid mobile number""\n")
                break

        def chk_day():
            while True:

                self.l = str(self.days.get())

                if self.l.isdigit() == True and len(self.l) != 0:
                    self.DAYS = int(self.l)
                    self.Text1.insert(INSERT, "Days has been inputed successfully""\n")
                    break
                else:
                    self.Text1.insert(INSERT, "Invalid input ""\n")
                    break

        def enter(self):
            self.name = self.NAME
            self.address = self.ADDERESS
            self.mobile_no = self.MOBILE
            self.no_of_days = int(self.DAYS)

        def tor(self):

            if self.ch == 1:
                self.price = self.price + (2000 * self.no_of_days)
                m[0] = 1
            elif self.ch == 2:
                self.price = self.price + (1500 * self.no_of_days)
                m[0] = 2
            elif self.ch == 3:
                self.price = self.price + (1000 * self.no_of_days)
                m[0] = 3
            elif self.ch == 4:
                self.price = self.price + (1700 * self.no_of_days)
                m[0] = 4

        def payment_option(self):
            op = self.p
            if op == 1:
                self.Text1.insert(INSERT, "No discount""\n")
            elif op == 2:
                self.price = self.price - ((self.price * 10) / 100)
                self.Text1.insert(INSERT, "10% discount""\n")

        def bill(self):

            if m[0] == 1:
                a = Delux
            elif m[0] == 2:
                a = Semi_Delux
            elif m[0] == 3:
                a = General
            elif m[0] == 4:
                a = Joint_Room

            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)
                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a:
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            list1.append(self.name)
            list1.append(self.address)
            list1.append(self.mobile_no)
            list1.append(self.room)
            list1.append(self.price)

            file_save()



        def submit_clicked():
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and self.var4.get()==0 and self.var5.get()==1 and self.var6.get()==0:
                self.ch=1
                self.p=2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)


            elif self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 1
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 2
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 1 and self.var3.get() == 0 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() ==0 :
                self.ch = 2
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 3
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 1 and self.var4.get() == 0 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 3
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 0 and self.var6.get() == 1:
                self.ch = 4
                self.p = 1

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)
            elif self.var1.get() == 0 and self.var2.get() == 0 and self.var3.get() == 0 and self.var4.get() == 1 and self.var5.get() == 1 and self.var6.get() == 0:
                self.ch = 4
                self.p = 2

                enter(self)
                tor(self)
                payment_option(self)
                bill(self)

            else:
                self.Text1.insert(INSERT, "invalid choice please input a valid choice""\n")





        root = Tk()
        root.geometry("1000x700+90+50")
        root.title("CHECK IN (Lovely Resort)")

        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(bg="light yellow")
        self.Text1.configure(font=("Alako",17,"bold"),fg="black",width=994,wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(bg="light green",width=995)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.04, rely=0.11, relheight=0.84, relwidth=0.5)
        self.Message1.configure(bg="light green",font=("arial",15,"bold"),width = 496)
        self.Message1.configure(text="YOU CLICKED ON")



        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.57, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(bg="light green",font=("arial",15,"bold"),fg="black",width=347)
        self.Message3.configure(text="CHECK INN")

        self.menubar = Menu(root,font=("arial",15,"bold"),fg="black")
        root.configure(menu = self.menubar)

        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(bg="purple",width=995)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label3.configure(bg="purple",font=("arial",15,"bold"),fg="white")
        self.Label3.configure(text="ENTER GUEST NAME")

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.045, rely=0.29, height=47, width=329)
        self.Label4.configure(bg="purple",font=("arial",15,"bold"),fg="white")
        self.Label4.configure(text="ENTER GUEST NUMBER")



        self.Entry3 = Entry(self.Frame2)
        self.name=StringVar()
        self.Entry3.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry3.configure(background="white",font=("ink free",15,"bold"),fg="black")
        self.Entry3.configure(textvariable=self.name)


        self.Entry4 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry4.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry4.configure(bg="white",font=("ink free",15,"bold"),fg="black")
        self.Entry4.configure(textvariable=self.mobile)


        self.Entry5 = Entry(self.Frame2)
        self.addr = StringVar()
        self.Entry5.place(relx=0.47, rely=0.18,height=34, relwidth=0.43)
        self.Entry5.configure(bg="white",font=("ink free",15,"bold"),fg="black")
        self.Entry5.configure(textvariable=self.addr)

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.045, rely=0.16, height=47, width=334)
        self.Label5.configure(bg="purple",font=("arial",15,"bold"),fg="white")
        self.Label5.configure(text="ENTER GUEST ADDRESS")

        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.32, rely=0.6, height=48, width=296)
        self.Label6.configure(bg="purple",font=("arial",15,"bold","underline"),fg="white")
        self.Label6.configure(text="CHOOSE YOUR ROOM TYPE")

        self.Label7 = Label(self.Frame2)
        self.Label7.place(relx=0.3, rely=0.79, height=48, width=300)
        self.Label7.configure(activebackground="white")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(bg="purple",font=("arial",15,"bold","underline"),fg="white")
        self.Label7.configure(text="CHOOSE PAYMENT METHOD")

        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
        self.Message4.configure(bg="purple",font=("arial",15,"bold"),fg="white",width=46)
        self.Message4.configure(text=":")

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
        self.Message5.configure(bg="purple",font=("arial",15,"bold"),fg="white",width=26)
        self.Message5.configure(text=":")

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(bg="purple",font=("arial",15,"bold"),fg="white",width=36)
        self.Message6.configure(text=":")

        self.Checkbutton1 = Checkbutton(self.Frame2)
        self.var1 = IntVar()
        self.Checkbutton1.place(relx=0.10, rely=0.68, relheight=0.17, relwidth=0.14)
        self.Checkbutton1.configure(activebackground="purple")
        self.Checkbutton1.configure(activeforeground="yellow")
        self.Checkbutton1.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var1)
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text="DELUXE")


        self.Checkbutton2 = Checkbutton(self.Frame2)
        self.var2 = IntVar()
        self.Checkbutton2.place(relx=0.3, rely=0.71, relheight=0.11, relwidth=0.21)
        self.Checkbutton2.configure(activebackground="purple")
        self.Checkbutton2.configure(activeforeground="yellow")
        self.Checkbutton2.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var2)
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text="FULL DELUXE")

        self.Checkbutton3 = Checkbutton(self.Frame2)
        self.var3 = IntVar()
        self.Checkbutton3.place(relx=0.52, rely=0.71, relheight=0.11, relwidth=0.16)
        self.Checkbutton3.configure(activebackground="purple")
        self.Checkbutton3.configure(activeforeground="yellow")
        self.Checkbutton3.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var3)
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text="GENERAL")

        self.Checkbutton4 = Checkbutton(self.Frame2)
        self.var4 = IntVar()
        self.Checkbutton4.place(relx=0.7, rely=0.71, relheight=0.11, relwidth=0.12)
        self.Checkbutton4.configure(activebackground="purple")
        self.Checkbutton4.configure(activeforeground="yellow")
        self.Checkbutton4.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var4)
        self.Checkbutton4.configure(justify=LEFT)
        self.Checkbutton4.configure(text="JOINT")

        self.Checkbutton5 = Checkbutton(self.Frame2)
        self.var5 = IntVar()
        self.Checkbutton5.place(relx=0.485, rely=0.9, relheight=0.1, relwidth=0.3)
        self.Checkbutton5.configure(activebackground="purple")
        self.Checkbutton5.configure(activeforeground="red")
        self.Checkbutton5.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var5)
        self.Checkbutton5.configure(justify=LEFT)
        self.Checkbutton5.configure(text="By credit/debit card")

        self.Checkbutton6 = Checkbutton(self.Frame2)
        self.var6 = IntVar()
        self.Checkbutton6.place(relx=0.153, rely=0.89, relheight=0.1, relwidth=0.15)
        self.Checkbutton6.configure(activebackground="purple")
        self.Checkbutton6.configure(activeforeground="red")
        self.Checkbutton6.configure(bg="purple",font=("arial",15,"bold"),fg="yellow",cursor="hand2",variable=self.var6)
        self.Checkbutton6.configure(justify=LEFT)
        self.Checkbutton6.configure(text="By cash")

        self.Message7 = Message(self.Frame2)
        self.Message7.place(relx=0.28, rely=0.46, relheight=0.11, relwidth=0.04)
        self.Message7.configure(bg="purple",font=("arial",15,"bold"),fg="white",width=41)
        self.Message7.configure(text="-")

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="light green")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(bg="red",font=("alako",18,"bold"),fg="white",cursor="hand2")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="OK")
        self.Button1.configure(command=chk_name)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.18, height=33, width=43)
        self.Button2.configure(activebackground="light green")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(bg="red",font=("alako",18,"bold"),fg="white",cursor="hand2")
        self.Button2.configure(pady="0")
        self.Button2.configure(text="OK")
        self.Button2.configure(command=chk_add)
        
        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.91, rely=0.31, height=33, width=43)
        self.Button3.configure(activebackground="light green")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(bg="red",font=("alako",18,"bold"),fg="white",cursor="hand2")
        self.Button3.configure(pady="0")
        self.Button3.configure(text="OK")
        self.Button3.configure(command=chk_mob)
        
        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.81, rely=0.82, height=50, width=156)
        self.Button4.configure(activebackground="light green")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(background="green",font=("arial",15,"bold"),fg="white",cursor="hand2",border=1)
        self.Button4.configure(pady="0")
        self.Button4.configure(text="SUBMIT")
        self.Button4.configure(command=submit_clicked)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.43, height=44, width=260)
        self.Label1.configure(background="purple",font=("arial",15,"bold"),fg="white")
        self.Label1.configure(text="NUMBER OF DAYS")


        self.Entry1 = Entry(self.Frame2)
        self.days=StringVar()
        self.Entry1.place(relx=0.47, rely=0.43, height=34, relwidth=0.43)
        self.Entry1.configure(background="white",font=("ink free",15,"bold"),fg="black",width=424)
        self.Entry1.configure(textvariable=self.days)

        self.Message8 = Message(self.Frame2)
        self.Message8.place(relx=0.42, rely=0.42, relheight=0.11, relwidth=0.03)
        self.Message8.configure(background="purple",font=("arial",15,"bold"),fg="white",width=26)
        self.Message8.configure(text=":")

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.91, rely=0.43, height=33, width=43)
        self.Button5.configure(activebackground="light green")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(background="red",font=("alako",18,"bold"),cursor="hand2",fg="white")
        self.Button5.configure(pady="0")
        self.Button5.configure(text="OK")
        self.Button5.configure(command=chk_day)


        root.mainloop()


if __name__ == '__main__':
    hotel = checkin()
