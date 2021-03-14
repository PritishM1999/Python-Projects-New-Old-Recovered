from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
global tkDealer

temp = 0
def dealerVerify(dealercode, phoneno):
    print("Dealer code entered :", dealercode.get())
    print("Phone Number entered :", phoneno.get())
    dealercodeEntry.configure(state=tk.NORMAL)
    phonenoEntry.configure(state=tk.NORMAL)    
    #global count
    #count += 1
    temp=str()
    #dealercodeEntry.delete(0, tk.END)
    #phonenoEntry.delete(0, tk.END)
    text = str()
    dealercodeEntry.insert(0, text)
    phonenoEntry.insert(0, text)
    dealercodeEntry.configure(state=tk.DISABLED)
    phonenoEntry.configure(state=tk.DISABLED)
    dealercodeEntry.configure(state=tk.DISABLED)
    otpButton.configure(state=tk.DISABLED)
    #count=int(count)
    get_otp()

def otpverify(otp):
    print("OTP entered :", otp.get())
    otpEntry.configure(state=tk.NORMAL)
    temp=str()
    text = str()
    otpEntry.configure(0, text)
    otpEntry = Entry(tkDealer, textvariable=otp)
    verifyButton.configure(state=tk.DISABLED)
    conformNew()
    
def update(newpass):
    print("New Password", newpass.get())
    
def previous_window():
    tkDealer.destroy()
    from Login import Data
    #exec(open("./login.py").read())
    
        
tkDealer = Tk()
tkDealer.geometry('700x500')
tkDealer.config(bg="#F3DFCA")
tkDealer.iconbitmap(r'C:/Users/PRITESH/Downloads/ARCS logo.ico') 
tkDealer.title('HPCL Reset Password - Translator')
tkDealer.resizable(0,0)

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/HPCL5.png')
background_label = tk.Label(tkDealer, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

appName = Label(tkDealer, text="Reset Password", font=('Rockwell bold', 15),bg="#F3DFCA", fg="#022D66")
appName.place(x=270, y=0)

photo = PhotoImage(file = r"C:/Users/PRITESH/Desktop/imgpy/HPCL5.png")
previous_window1 = partial(previous_window)
Back = Button(tkDealer, relief = "flat", text="Back", image=photo,bg="#022D66", fg='WHITE', width=32, height=18, command = previous_window1).place(x=13, y=15)

dealercode = StringVar()
dealerLabel = Label(tkDealer, text="Destributor Code  ",font=('Rockwell bold', 10, 'bold'), bg="#F3DFCA",  fg="#022D66", width=15)
dealerLabel.place(x=365, y=75)
dealercodeEntry = Entry(tkDealer, textvariable=dealercode)  
dealercodeEntry.place(x=500, y=75)

phoneno = StringVar()
phonenoLabel = Label(tkDealer,text=" Phone Number",font=('Rockwell bold', 10, 'bold'), bg="#F3DFCA", fg="#022D66", width=15)
phonenoLabel.place(x=365, y=125)
phonenoEntry = Entry(tkDealer, textvariable=phoneno) 
phonenoEntry.place(x=500, y=125)

dealerVerify1 = partial(dealerVerify, dealercode, phoneno)
otpButton = tk.Button(tkDealer, text="Get OTP", font=('arial', 8, 'bold'), bg="#022D66", fg='WHITE', width=10,
                      command=lambda: dealerVerify(dealercode,phoneno), state=tk.NORMAL)
otpButton.pack()
otpButton.place(x=500, y=160)
#otpButton.config(state = DISABLED)
#otpButton.bind("<Button-1>")
#state=tk.DISABLED

def get_otp():
    otp = StringVar()
    otpLabel = Label(tkDealer,text=" Enter OTP",font=('Rockwell bold', 10, 'bold'), bg="#F3DFCA", fg="#022D66", width=10)
    otpLabel.place(x=400, y=215)
    
    otpEntry = Entry(tkDealer, textvariable=otp, show= '*') 
    otpEntry.place(x=500, y=215)
    
    otpverify1 = partial(otpverify, otp)
    verifyButton = tk.Button(tkDealer, text="Verify OTP", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE',
                          width=15, command=lambda: otpverify1 , state=tk.NORMAL)
    verifyButton.place(x=500, y=255)
    
def conformNew():
    global conformNew
    newpass = StringVar()
    newpassLabel = Label(tkDealer,text="     Enter New Password",font=('Rockwell bold', 10, 'bold'), bg="#F3DFCA", fg="#022D66", width=20)
    newpassLabel.place(x=320, y=310)
    newpassEntry = Entry(tkDealer, textvariable=newpass, show = '*') 
    newpassEntry.place(x=500, y=310)

    confpass = StringVar()
    confpassLabel = Label(tkDealer,text="Re-Enter New Password",font=('Rockwell bold', 10, 'bold'), bg="#F3DFCA", fg="#022D66", width=20)

    confpassLabel.place(x=320, y=360)
    confpassEntry = Entry(tkDealer, textvariable=confpass, show = '*')
    confpassEntry.place(x=500, y=360) 

    update1 = partial(update, newpass)
    saveButton = Button(tkDealer, text="Save", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE', width=15,  command=update1)
    saveButton.place(x=500, y=400)

#verifyButton.place(x=300, y=220)
#verifyButton.pack()
tkDealer.mainloop()

#dealerVerify()
