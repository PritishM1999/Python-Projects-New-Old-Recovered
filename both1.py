#To Import image in background
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter.filedialog import askopenfilename
import webbrowser


def dealerLogin(dealercode, password):
	print("dealer code entered :", dealercode.get())
	print("password entered :", password.get())
	return

tkDealer = Tk()
tkDealer.title("HP")
tkDealer.geometry('700x500')
tkDealer.config(bg="#F3DFCA")
tkDealer.iconbitmap(r'C:/Users/PRITESH/Desktop/imgpy/favicon.ico') 
tkDealer.title('HPCL Dealer Login - designed by pritish')
tkDealer.resizable(0,0)

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/fiHPCLfin.png')
background_label = tk.Label(tkDealer, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

dealercode = StringVar()
dealerLabel = Label(tkDealer, text=" Dealer Code   ",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12)
dealerLabel.place(x=340, y=125)
dealercodeEntry = Entry(tkDealer, textvariable=dealercode)
dealercodeEntry.insert(0, '54321')
dealercodeEntry.place(x=460, y=125)

password = StringVar()
passwordLabel = Label(tkDealer,text=" Password",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12)
passwordLabel.place(x=340, y=205)
passwordEntry = Entry(tkDealer, textvariable=password, show='*')
passwordEntry.insert(0, '54321')
passwordEntry.place(x=460, y=205)


dealerLogin = partial(dealerLogin, dealercode, password)


loginButton = Button(tkDealer, text="Login", font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=10, command=dealerLogin)
loginButton.place(x=360, y=315)

forgotButton = Button(tkDealer, text="Forgot Password", font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=15, command=password)
forgotButton.place(x=460, y=315)

newdealer=Button(tkDealer, text="Click here to register new dealer!",relief="sunken",bg="#F3DFCA", width=30,command=lambda:dealerLogin(1))
newdealer.place(x=360,y=350)


tkDealer.mainloop()



def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
class Window2:
    def _init_(self, master):
        self.master= master
        self.master.title("HPCL2")
        self.master.geometry("1300x1100")
        self.master.config(bg='ivory')
        self.frame = Frame(self.master, bg = "ivory")
        self.frame.pack()

        root = Tk()
        root.geometry('600x500')
        root.config(bg="ivory")
        root.title("HPCL DCMS CASH MEMO Translator [designed by:Pritish]")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)

        def NewFile():
            print("New File!")
    
        def OpenFile():
            print("Open Fine")
    
        def About():
            print("This is a simple example of a menu")

        def CashMemo():
            print("Cash Memo")

        def LanguageConverter():
            print("Language Converter")

        def Records():
            print("Records Found")

        def Settings():
            print("Settings")

        def UpdateLib():
            print("Update Library")
    

        file = ""
        defaultText = "\n Pritish mendhekar.\n \t  designed this application "

        appName = Label(root, text="HPCL DCMS CASH MEMO TRANSLATOR ", font=('arial', 20, 'bold'),bg="ivory", fg='maroon')
        appName.place(x=40, y=10)

        appName = Label(root, text="CONTROL PANEL ", font=('arial', 10, 'bold'),bg="ivory", fg='maroon')
        appName.place(x=40, y=50)

        filemenu.add_command(label="New", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=About)

        CashMemo = Button(root, text="Cash Memo", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20, command=CashMemo)
        CashMemo.place(x=30, y=80)

        LanguageConverter = Button(root, text="Language Converter", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20, command=LanguageConverter)
        LanguageConverter.place(x=30, y=130)

        OpenFiles = Button(root, text="Open Files", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20, command=Records)
        OpenFiles.place(x=30, y=180)

        Settings = Button(root, text="Settings", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20, command=Settings)
        Settings.place(x=30, y=230)

        UpdateLib = Button(root, text="Update Library", font=('arial', 8, 'bold'),
                      bg="RED", fg='WHITE', width=20, command=UpdateLib)
        UpdateLib.place(x=30, y=280)


mainloop()
