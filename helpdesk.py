from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter.filedialog import askopenfile

def HelpDesk(AppDown,Cdcms,Ncms):
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
root.geometry("1000x650")

C61=Canvas(root, height=520, width=700, bg='#F3DFCA', bd=15, relief='ridge').place(x=225,y=50)

'''
seg = Label(C61, text="Segment", font=('Rockwell Bold', 12, 'bold'), bg='whitesmoke', fg='#022D66').place(x=350,y=70)

AppDown = Button(root, text="Application Down", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=20, height = -1, command=AppDown)
AppDown.place(x=45, y=90)

Cdcms = Button(root, text="CDCMS", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=20, height = -1, command=Cdcms)
Cdcms.place(x=45, y=90)

Ncms = Button(root, text="Non-CDCMS", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=20, height = -1, command=Ncms)
Ncms.place(x=45, y=90)
'''


#HelpDesk = partial(AppDown,Cdcms,Ncms)

'''var = StringVar()
R1 = Radiobutton(C61, text="Application Down", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='AppDown',
                  command=HelpDesk).place(x=430,y=70)

R2 = Radiobutton(C61, text="CDCMS", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='Cdcms',
                  command=HelpDesk).place(x=580,y=70)

R3 = Radiobutton(C61, text="Non-CDCMS", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='Ncms',
                  command=HelpDesk).place(x=670,y=70)

#HelpDesk = partial(AppDown,Cdcms,Ncms)
deskBtn = Button(C61, text="Select", bg='#022D66' , fg='White',font=('Rockwell Bold', 10, 'bold'),
                         command = lambda: AppDown)
deskBtn.place(x=800, y=70)'''

def AppDown():
    print("AppDown")
    C61A=Canvas(root, height=480, width=600, bg="#F3DFCA", highlightthickness=1, highlightbackground="Black", relief='flat').place(x=300,y=98)
    #seg1 = Label(C61, text="Canvas A", font=('Rockwell Bold', 12, 'bold'), bg='#F3DFCA', fg='#022D66').place(x=250,y=100)

    dic = {"Application": ["Application Slowness",
                           "ARB Portal Application Down",
                           "CDCMS Application Down",
                           "Consumer Subsidy information Portal Down",
                           "DBTL Seeding Portal Down",
                           "IVRS Application Down",
                           "LPG Panchayat Portal Down",
                           "OMC TV Portal Application Down",
                           "UJJWALA Application Down"],
           "Application Down": ["CDCMS","Consumer Subsidy Information Portal","DBTL Seeding Portal","IVRS","OMC TV PORTAL","Panchayat Portal","UJJWALA"]}
           #"C": ["Watermelon","Kiwi"]}

    def on_select(event):
        option_box2["values"] = dic[option_box1.get()] #modify 2nd combobox directly
        option_box2.current(0)

    cat = Label(C61, text="Category", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    cat.place(x=470, y=135)
    
    var_cat = StringVar()
    var_cat.set("Category")
    option_box1 = ttk.Combobox(C61, value=[k for k in dic],state="readonly")
    option_box1.place(x=550, y=135)

    Scat = Label(C61, text="Sub Category", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    Scat.place(x=448, y=185)
    
    var_scat = StringVar()
    var_scat.set("Sub Category")    
    option_box2 = ttk.Combobox(C61,state="readonly", width = 40)
    option_box2.place(x=550, y=185)

    option_box1.bind("<<ComboboxSelected>>",on_select)

    ProbDis = StringVar()
    Prob = Label(C61, text="Problem Description", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    Prob.place(x=400, y=235)
    ProbDis = Text(C61, width=30,height=3).place(x=550, y=235)

    ResTime = Label(C61, text="Resolution Time", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    ResTime.place(x=430, y=305)
    ResTime2 = Label(C61, text="Hours", font=('Rockwell Bold', 9, 'bold'), bg='#F3DFCA', fg='RED')
    ResTime2.place(x=550, y=305)    

    TeamVir = StringVar()
    TeamVir = Label(C61, text="Team Viewer ID", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    TeamVir.place(x=428, y=345)
    TeamVir = Entry(C61, width=30).place(x=550, y=345)

    ProbDis = StringVar()
    Prob = Label(C61, text="Dealer Contact Number", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    Prob.place(x=380, y=395)
    ProbDis = Entry(C61, width=30).place(x=550, y=395)

    Selfil = Label(C61, text="Select File", font=('Rockwell Bold', 10, 'bold'), bg='#F3DFCA')
    Selfil.place(x=465, y=445)

    def open_file(): 
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
        if file is not None: 
            content = file.read() 
            print(content) 
  
    UplBtn = Button(C61, text ='Upload Here', bg='#022D66' , fg='White',font=('Rockwell Bold', 10, 'bold'), command = lambda:open_file()) 
    UplBtn.place(x=550, y=440) 

    SubBtn = Button(C61, text ='Submit', bg='#022D66' , fg='White',font=('Rockwell Bold', 10, 'bold'), command = lambda:Save) 
    SubBtn.place(x=470, y=500)

    ResBtn = Button(C61, text ='Reset', bg='#022D66' , fg='White',font=('Rockwell Bold', 10, 'bold'), command = lambda:Reset) 
    ResBtn.place(x=550, y=500)    

def Cdcms():
    print("Cdcms")
    C61B=Canvas(root, height=480, width=600, bg="#F3DFCA", highlightthickness=1, highlightbackground="Black", relief='flat').place(x=300,y=100)
    seg2 = Label(C61, text="Canvas B", font=('Rockwell Bold', 12, 'bold'), bg='#F3DFCA', fg='#022D66').place(x=350,y=100)


def Ncms():
    print("Ncms")
    C61C=Canvas(root, height=480, width=600, bg="#F3DFCA", highlightthickness=1, highlightbackground="Black", relief='flat').place(x=300,y=100)
    seg3 = Label(C61, text="Canvas C", font=('Rockwell Bold', 12, 'bold'), bg='#F3DFCA', fg='#022D66').place(x=350,y=100)

seg = Label(C61, text="Segment", font=('Rockwell Bold', 12, 'bold'), bg='#F3DFCA', fg='#022D66').place(x=400,y=70)

AppDown = Button(root, text="Application Down", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=15, height = -1, command=AppDown)
AppDown.place(x=500,y=70)

Cdcms = Button(root, text="CDCMS", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=10, height = -1, command=Cdcms)
Cdcms.place(x=630, y=70)

Ncms = Button(root, text="Non-CDCMS", font=('Rockwell Bold', 8, 'bold'), bg="white", fg='Black', width=10, height = -1, command=Ncms)
Ncms.place(x=725, y=70)


label = Label(root)
label.pack()
root.mainloop()

'''from tkinter import *

def HelpDesk():
    #myDesk = Label(C61, text=value).place(x=350,y=170)
    selection = "You selected the option " + str(var.get()
    label.config(text = selection)

root = Tk()
root.geometry("1000x650")

C61=Canvas(root, height=520, width=700, bg='#F3DFCA', bd=15, relief='ridge').place(x=225,y=50)

seg = Label(C61, text="Segment", font=('Rockwell Bold', 12, 'bold'), bg='whitesmoke', fg='#022D66').place(x=350,y=70)

#HelpDesk = partial(AppDown,Cdcms,Ncms)

var = StringVar()
R1 = Radiobutton(C61, text="Application Down", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='AppDown',
                  command=HelpDesk).place(x=430,y=70)


R2 = Radiobutton(C61, text="CDCMS", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='Cdcms',
                  command=HelpDesk).place(x=580,y=70)


R3 = Radiobutton(C61, text="Non-CDCMS", font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke', variable=var, value='Ncms',
                  command=HelpDesk).place(x=670,y=70)

Cat = Label(root, text=var.get(), font=('Rockwell Bold', 10, 'bold'), bg='whitesmoke')
Cat.place(x=400, y=100)

deskBtn = Button(C61, text="Select", bg='#022D66' , fg='White',font=('Rockwell Bold', 10, 'bold'),
                         command = lambda: HelpDesk)
deskBtn.place(x=800, y=70)

label = Label(root)
label.pack()
root.mainloop()
'''

'''from tkinter import *

master = Tk()
var = IntVar()
var.set(1)

entry_text = StringVar()
entry_text.set("###")

def quit_loop():
    print ("Selection:",var.get())
    global selection
    selection = var.get()

    if selection == 2:
        selection = entry_text.get()

    master.quit()

# Add columnspan to these widgets
Label(master, text = "Select OCR language").grid(row=0, sticky=W, columnspan=3)
Radiobutton(master, text = "default", variable=var, value = 1).grid(row=1, sticky=W, columnspan=3)

# Order these widgets in their appropriate columns
Radiobutton(master, variable=var, value = 2).grid(row=2, sticky=W, column=0)
Label(master, text="Enter value:").grid(row=2, sticky=W, column=1)
Entry(master, textvariable=entry_text).grid(row=2, sticky=W, column=2)

# Example of what happens without columnspan
Button(master, text = "OK", command=quit_loop).grid(row=3, sticky=W)

master.mainloop()

print (selection)
'''




'''
from tkinter import *

master = Tk()
var = IntVar()
var.set(1)

entry_text = StringVar()
entry_text.set("###")

def quit_loop():
    print ("Selection:",var.get())
    global selection
    selection = var.get()

    if selection == 2:
        selection = entry_text.get()

    master.quit()

# Add columnspan to these widgets
Label(master, text = "Select OCR language").grid(row=0, sticky=W, columnspan=3)
Radiobutton(master, text = "default", variable=var, value = 1).grid(row=1, sticky=W, columnspan=3)

# Order these widgets in their appropriate columns
Radiobutton(master, variable=var, value = 2).grid(row=2, sticky=W, column=0)
Label(master, text="Enter value:").grid(row=2, sticky=W, column=1)
Entry(master, textvariable=entry_text).grid(row=2, sticky=W, column=2)

# Example of what happens without columnspan
Button(master, text = "OK", command=quit_loop).grid(row=3, sticky=W)

master.mainloop()

print (selection)
'''
