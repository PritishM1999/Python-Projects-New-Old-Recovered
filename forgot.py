'''
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def loginok(dealercode,phoneno):
    global storedPhoneno
    if dealercode == "Pritish":
        if phoneno == storedPhoneno:
            messagebox.showinfo("Login Successful!","Welcome Admin")
        else:
            messagebox.showerror("Login Failed!","Wrong Password")
    else:
        messagebox.showerror("Login Failed!","Wrong Username")

window = Tk()
window.title("HP")
window.geometry('700x500')
window.config(bg="ivory")
window.iconbitmap(r'C:/Users/PRITESH/Desktop/imgpy/favicon.ico') 
window.title('HPCL Dealer Login - designed by pritish')
window.resizable(0,0)

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/fiHPCLfin.png')
background_label = tk.Label(window, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

storedPassword = '123456'


def cpass():
    global window
    window.destroy()
    
    Label(window,text="Enter new password:").pack()
    passn = Entry(window,width=150)
    passn.pack()
    Button(window,text="OK",command=lambda:chgpass(passn.get())).pack()
    window.mainloop()

def chgpass(newpass):
    global window
    global storedPhoneno
    storedPhoneno = newpass
    window.destroy()
    login()

def login():
    global window

    Label(window,text="Dealer Code:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack()
    dealer = Entry(window,width=30)
    dealer.pack()
    Label(window,text="Phone Number:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack()
    phone = Entry(window,width=30)
    phone.pack()
    Button(window,text="Login",font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=10,command=lambda:loginok(usern.get(),passw.get())).pack()
    Button(window,text="Forgot",font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=10,command=cpass).pack()
    window.mainloop()

login()
window()


def login():
    global window

    Label(window,text="Dealer Code:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).place(x=250,y=20)
    usern = Entry(window,width=15)
    usern.pack(x=30,y=20)
    
    Label(window,text="Phone Number:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).place(x=450,y=40)
    passw = Entry(window,width=30)
    passw.place(x=250,y=215)

    
    Button(window,text="Verify",font=('arial', 8, 'bold'),
            bg="#022D66", fg='WHITE', width=10,command=lambda:loginok(usern.get(),passw.get())).place(x=350,y=315)

    Label(window,text="Enter OTP:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).place(x=450,y=415)
    usern = Entry(window,width=15)
    usern.place(x=550,y=415)

    def myClick():
            myLabel = Label(window, text="OTP Verified !", bg="#F3DFCA")
            myLabel.place(x=400,y=300)

    myButton = Button(window, text="Verify OTP", bg="#022D66",fg ="white", command = lambda:myClick())
    myButton.place(x=320,y=420)
    
    myButton.pack()
    Button(window,text="Enter and save New Password",font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=20,command=cpass).pack(ipadx=20, pady=10, padx=30)
    #Label(window,text="Enter OTP:",font=('Rockwell bold', 12, 'bold'),
     #                 bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    Newpass = Entry(window,width=10)
    Newpass.pack(ipadx=50, pady=10, padx=50)
    
    #label1 = label(window, text="Enter OTP",width=20,font=("Rockwell bold",10))
    #entry1.place(x=350,y=250)
    window.mainloop()
    
'''

from tkinter import *
from tkinter import messagebox
import tkinter as tk


def loginok(username,password):
    global storedPassword
    if username == "Pawan":
        if password == storedPassword:
            messagebox.showinfo("Login Successful!","Welcome to HPCL converter")
        else:
            messagebox.showerror("Login Failed!","Wrong Password")
    else:
        messagebox.showerror("Login Failed!","Wrong Dealer Code")
        

window = Tk()
window.title("HP")
window.geometry('700x500')
window.config(bg="ivory")
window.iconbitmap(r'C:/Users/PRITESH/Desktop/imgpy/favicon.ico') 
window.title('HPCL Dealer Login - designed by pritish')
window.resizable(0,0)

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/fiHPCLfin.png')
background_label = tk.Label(window, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

storedPassword = '123456'

def otp():
    global window
    window.destroy()
    window = Tk()
    Label(window,text="Enter OTP :").pack()
    passn = Entry(window,width=50)
    passn.pack()
    Button(window,text="OK",command=lambda:chgpass(passn.get())).pack()
    window.mainloop()

def cpass():
    global window
    window.destroy()
    window = Tk()
    Label(window,text="Conform and Save new password:").pack()
    passn = Entry(window,width=50)
    passn.pack()
    Button(window,text="OK",command=lambda:chgpass(passn.get())).pack()
    window.mainloop()

def chgpass(newpass):
    global window
    global storedPassword
    storedPassword = newpass
    window.destroy()
    login()

def login():
    global window

    Label(window,text="Dealer Code:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    usern = Entry(window,width=30)
    usern.pack(ipadx=20, pady=10, padx=30)
    
    Label(window,text="Phone Number:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    passw = Entry(window,width=30)
    passw.pack(ipadx=20, pady=10, padx=30)

    
    Button(window,text="Verify",font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=10,command=lambda:loginok(usern.get(),passw.get())).pack(ipadx=30, pady=10, padx=50)

    Label(window,text="Enter OTP:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    usern = Entry(window,width=30)
    usern.pack(ipadx=20, pady=10, padx=30)

    def myClick():
            myLabel = Label(window, text="OTP Verified !", bg="#F3DFCA")
            myLabel.place(x=400,y=300)

    myButton = Button(window, text="Verify OTP", bg="#022D66",fg ="white", command = lambda:myClick())
    myButton.place(x=320,y=420)
    
    myButton.pack()
    Label(window,text="Enter New Password:",font=('Rockwell bold', 12, 'bold'),
                      bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    usern = Entry(window,width=30)
    usern.pack(ipadx=20, pady=10, padx=30)    
    Button(window,text="Enter and save New Password",font=('arial', 8, 'bold'),
                      bg="#022D66", fg='WHITE', width=20,command=cpass).pack(ipadx=20, pady=10, padx=30)
    #Label(window,text="Enter New Password Here:",font=('Rockwell bold', 12, 'bold'),
     #                 bg="#F3DFCA", fg='BLACK', width=12).pack(ipadx=20, pady=10, padx=30)
    #usern = Entry(window,width=30)
    #usern.pack(ipadx=50, pady=10, padx=50)
    
    #label1 = label(window, text="Enter OTP",width=20,font=("Rockwell bold",10))
    #entry1.place(x=350,y=250)
    window.mainloop()
    
login()
