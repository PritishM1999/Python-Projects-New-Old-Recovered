#To Import image in background
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk

def dealerLogin(dealercode, password):
	print("dealer code entered :", dealercode.get())
	print("password entered :", password.get())
	return


tkDealer = Tk()
tkDealer.title("HP")
tkDealer.geometry('670x495')
tkDealer.config(bg="ivory")
tkDealer.iconbitmap(r'C:/Users/PRITESH/Desktop/imgpy/favicon.ico') 
tkDealer.title('HPCL Dealer Login - designed by pritish')

background_image=tk.PhotoImage(file='C:/Users/PRITESH/Desktop/imgpy/hpfill (1).png')
background_label = tk.Label(image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

dealercode = StringVar()
dealerLabel = Label(tkDealer, text="     Dealer Code     ")
dealerLabel.place(x=50, y=120)
usernameEntry = Entry(tkDealer, textvariable=dealercode)  
usernameEntry.place(x=160, y=120)

password = StringVar()
passwordLabel = Label(tkDealer,text="      Password      ")
passwordLabel.place(x=50, y=180)
passwordEntry = Entry(tkDealer, textvariable=password, show='*') 
passwordEntry.place(x=160, y=180)


loginButton = Button(tkDealer, text="Login", command=dealerLogin)
loginButton.place(x=80, y=250)
forgotButton = Button(tkDealer, text="Forgot Password", command=password)
forgotButton.place(x=140, y=250)


dealerLogin = partial(dealerLogin, dealercode, password)

tkDealer.mainloop()
#root.mainloop()
#from tkinter import *
#root = Tk() 
#root.title("HP") 
#root.iconbitmap(r'C:/Users/sneharsh/Desktop/Fully Python Iternship/gas_R14_icon.ico') 
  
