from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk

from tkinter import *
from tkinter import messagebox
import tkinter as tk

from tkinter import *
from tkinter.filedialog import askopenfilename
import webbrowser


def dealerVerify(dealercode, phoneno, otp):
	print("Dealer code entered :", dealercode.get())
	print("Phone Number entered :", phoneno.get())
	return

global tkVerify
tkVerify = Tk()
tkVerify.geometry('700x500')
tkVerify.config(bg="#F3DFCA")
tkVerify.iconbitmap(r'C:/Users/PRITESH/Desktop/imgpy/favicon.ico') 
tkVerify.title('HPCL Dealer Login - designed by pritish')
tkVerify.resizable(0,0)

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/HPCL Register.png')
background_label = tk.Label(tkVerify, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

dealercode = StringVar()
dealerLabel = Label(tkVerify, text="Destributor Code  ",font=('Rockwell bold', 12, 'bold'),
                    bg="#F3DFCA", fg='BLACK', width=15)
dealerLabel.place(x=340, y=75)
dealercodeEntry = Entry(tkVerify, textvariable=dealercode)  
dealercodeEntry.place(x=500, y=75)

phoneno = StringVar()
phonenoLabel = Label(tkVerify,text=" Phone Number",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=15)
phonenoLabel.place(x=340, y=120)
phonenoEntry = Entry(tkVerify, textvariable=phoneno, show='*') 
phonenoEntry.place(x=500, y=120)

otp = StringVar()
otpLabel = Label(tkVerify,text=" Enter OTP",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=10)
otpLabel.place(x=380, y=200)
otpEntry = Entry(tkVerify, textvariable=otp) 
otpEntry.place(x=500, y=200)

dealerVerify = partial(dealerVerify, dealercode, phoneno, otp)


otpButton = Button(tkVerify, text="Get OTP", font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=10, command=dealerVerify)
otpButton.place(x=500, y=160)

def conformNew():
    global conformNew
    newpass = StringVar()
    newpassLabel = Label(tkVerify,text="     Enter New Password",font=('Rockwell bold', 12, 'bold'),
                bg="#F3DFCA", fg='BLACK', width=20).place(x=280, y=300)
    #newpass.place(x=320, y=250)
    
    newpass = Entry(tkVerify, textvariable=newpass).place(x=500, y=300) 
    #newpass.place(x=400, y=250)

    confpass = StringVar()
    confLabel = Label(tkVerify,text="Re-Enter New Password",font=('Rockwell bold', 12, 'bold'),
                bg="#F3DFCA", fg='BLACK', width=20).place(x=280, y=360)

    confpass = StringVar()
    #confpass.place(x=360, y=330)
    confpass = Entry(tkVerify, textvariable=confpass).place(x=500, y=360) 
    #confpass.place(x=400, y=330)

    
    
    saveButton = Button(tkVerify, text="Save", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE',
                          width=15,  command=conformNew).place(x=500, y=400)

verifyButton = Button(tkVerify, text="Verify OTP", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE',
                          width=15,  command = lambda:conformNew()).place(x=500, y=240)
#verifyButton.place(x=300, y=220)
#verifyButton.pack()


dealerVerify()
    
'''
tkVerify.mainloop()

def conformNew(newpass,confpass):
    print("Password Entered :", newpass.get())
    print("Confirm Password :", confpass.get())
    
    
    newpass = StringVar()
    newpassLabel = Label(tkVerify,text="Enter New Password",font=('Rockwell bold', 12, 'bold'),
                bg="#F3DFCA", fg='BLACK', width=15).pack(ipadx=5, padx=0, pady=0)
    #newpass.place(x=320, y=250)
    
    newpass = Entry(tkVerify, textvariable=newpass).pack(ipadx=5, padx=0, pady=0) 
    #newpass.place(x=400, y=250)

    confpass = StringVar()
    confLabel = Label(tkVerify,text="Re-Enter New Password",font=('Rockwell bold', 12, 'bold'),
                bg="#F3DFCA", fg='BLACK', width=20).pack(ipadx=5, padx=0, pady=0)

    confpass = StringVar()
    #confpass.place(x=360, y=330)
    confpass = Entry(tkVerify, textvariable=confpass).pack(ipadx=5, padx=0, pady=0) 
    #confpass.place(x=400, y=330)

    
    
    saveButton = Button(tkVerify, text="Save", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE',
                          width=15,  command=conformNew(newpass.get(), confpass.get())).pack(ipadx=5, padx=0, pady=20)

    verifyButton = Button(tkVerify, text="Verify OTP", font=('arial', 8, 'bold'),bg="#022D66", fg='WHITE',
        width=15,  command = lambda:conformNew(newpass.get(), confpass.get()).pack(ipadx=5, padx=190, pady=50)
    #verifyButton.place(x=300, y=220)
    #verifyButton.pack()


dealerVerify()
    
tkVerify.mainloop()
