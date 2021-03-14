import tkinter as tk
from tkinter import *
from functools import partial

def on_configure(event):
    canvas1.configure(scrollregion=canvas1.bbox('all'))

def previous_window():
    window.destroy()
    from HPCL import Login
    #exec(open("./login.py").read())
    
window = Tk()
window.config(bg="#F3DFCA")
window.iconbitmap(r'C:\Users\ACER\Desktop\INTERNSHIP\ARCS logo.ico') 
window.title('Distributer Registration')
window.resizable(0,0)


label_0 = Label(window, text="NEW DEALER REGISTRATION",font=('Rockwell bold', 12, 'bold'), bg="#F3DFCA", fg='#022D66', width=35)
label_0.place(x=5,y=5)

canvas1=Canvas(window,width=700,height=500,bg='ivory')
canvas1.pack(side=tk.LEFT, fill='y')

scrollbar = tk.Scrollbar(window, command=canvas1.yview)
scrollbar.pack(side=tk.LEFT, fill='y')


canvas1.configure(yscrollcommand = scrollbar.set)
canvas1.bind('<Configure>', on_configure)

frame = tk.Frame(canvas1)
canvas1.create_window((0,0), window=frame, anchor='nw',width=700,height=800)

background_image=tk.PhotoImage(file=r'C:\Users\ACER\Desktop\INTERNSHIP\backgroundimage.png')
background_label = tk.Label(frame, image=background_image, bd=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

photo = PhotoImage(file = r"C:\Users\ACER\Desktop\INTERNSHIP\backgroundimage.png")
previous_window1 = partial(previous_window)
Back = Button(window, relief = "flat", text="Back", image=photo,bg="#022D66", fg='WHITE', width=32, height=18, command = previous_window1).place(x=16, y=17)

def register(DesCodeEntry,DesNameEntry,emailEntry,phoneEntry,addressEntry,districtEntry,salesEntry,officerEntry,pasEntry,cpasEntry):
    print("Dealer code entered :",DesCodeEntry.get())
    print("Phone Name entered :",DesNameEntry.get())
    print("Email Entered",emailEntry.get())
    print("Phone Number entered :",phoneEntry.get())              
    print("Address",addressEntry.get())
    #print("Address line 1:", add1Entry.get())
    #print("Address line 2:", add2Entry.get())
    print("District:",districtEntry.get())
    print("Sales Region",salesEntry.get())
    print("Sales Officer :", officerEntry.get())
    print("Password",pasEntry.get())
    print("confirm Password",cpasEntry.get())
    return
#scrollbar = tk.Scrollbar(window, command=canvas1.yview)
#scrollbar.pack(side=tk.RIGHT, fill='y')
DesCode=tk.Label(frame, text="New Destributer Registration Form",font=('Rockwell Bold',13),
                 bg="#F3DFCA", fg='#022D66', width=30)
DesCode.place(x=100,y=5)

DesCode=tk.Label(frame, text="Destributer Code:",font=('Rockwell Bold',11),
                 bg="#F3DFCA", fg='#022D66', width=15)
DesCode.place(x=380,y=50)
DesCodeEntry = StringVar()
DesCodeEntry=tk.Entry(frame,width=20, textvariable=DesCodeEntry)
DesCodeEntry.place(x=550,y=50)


DesNameLabel = tk.Label(frame, text="Distributor Name:",font=('Rockwell bold',11),
                    bg="#F3DFCA", fg='#022D66', width=15)
DesNameLabel.place(x=380,y=100)
DesNameEntry = StringVar()
DesNameEntry = tk.Entry(frame,width=20, textvariable=DesNameEntry)
DesNameEntry.place(x=550,y=100)


emailLabel = tk.Label(frame, text="Dealer E-mail address:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=20)
emailLabel.place(x=340,y=200 )
emailEntry = StringVar()
emailEntry = tk.Entry(frame,width=20, textvariable=emailEntry)
emailEntry.place(x=550,y=200)

phoneEntry = StringVar()
phoneLabel = tk.Label(frame, text="Phone Number:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=20)
phoneLabel.place(x=365,y=150)
phoneEntry = tk.Entry(frame,width=20, textvariable=phoneEntry)
phoneEntry.place(x=550,y=150)


#OfficeEntry = tk.Entry(frame,width=20,bd=5)
#OfficeEntry.place(x=550,y=200)

addressEntry = StringVar()
addressLabel = tk.Label(frame, text="Address:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
addressLabel.place(x=425,y=250)
addressEntry = tk.Combobox(frame,width=30, textvariable=addressEntry)
addressEntry.place(x=475,y=250)
#addressEntry.pack(ipadx=60, pady=260, padx=320, ipady=30)
addressEntry = Text()
ScrollBar = Scrollbar(root)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack(expand=YES, fill=BOTH)
#addressEntry.place(x=550,y=250)

'''add1Entry = StringVar()
add1Label = tk.Label(frame, text="Address Line 1:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
add1Label.place(x=400,y=350)
add1Entry = tk.Entry(frame,width=20, textvariable=add1Entry)
add1Entry.place(x=550,y=350)

add2Entry = StringVar()
add2Label = tk.Label(frame, text="Address Line 2:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
add2Label.place(x=400,y=400)
add2Entry = tk.Entry(frame,width=20, textvariable=add2Entry)
add2Entry.place(x=550,y=400) '''              

districtEntry = StringVar()
districtLabel = tk.Label(frame, text="District:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66')
districtLabel.place(x=470,y=350)
districtEntry = tk.Entry(frame,width=20, textvariable=districtEntry)
districtEntry.place(x=550,y=350)

salesEntry = StringVar()
salesLabel = tk.Label(frame, text="Sales Region:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
salesLabel.place(x=400,y=400)
salesEntry = tk.Entry(frame,width=20, textvariable=salesEntry)
salesEntry.place(x=550,y=400)

officerEntry = StringVar()
officerLabel = tk.Label(frame, text="Sales Officer Name:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
officerLabel.place(x=380,y=450)
officerEntry = tk.Entry(frame,width=20, textvariable=officerEntry)
officerEntry.place(x=550,y=450)

pasEntry = StringVar()
pasLabel = tk.Label(frame, text="Create Password:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
pasLabel.place(x=390,y=500)
pasEntry = tk.Entry(frame,width=20, textvariable=pasEntry)
pasEntry.place(x=550,y=500)

cpasEntry = StringVar()
cpasLabel = tk.Label(frame, text="Conform Password:",font=('Rockwell bold', 11),
                    bg="#F3DFCA", fg='#022D66', width=15)
cpasLabel.place(x=380,y=550)
cpasEntry = tk.Entry(frame,width=20, textvariable=cpasEntry)
cpasEntry.place(x=550,y=550)


saveDetails = partial(register, DesCodeEntry,DesNameEntry,emailEntry,phoneEntry,addressEntry,districtEntry,salesEntry,officerEntry,
                pasEntry,cpasEntry)

Submit=tk.Button(frame,text="Submit",font=('Rockwell bold', 11),
                    bg="#022D66", fg='#F3DFCA', width=10, command = saveDetails)
Submit.place(x=550,y=600)

window.mainloop()
