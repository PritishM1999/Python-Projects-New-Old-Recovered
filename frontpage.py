from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile

root = Tk()
root.geometry('700x600')
root.config(bg="ivory")
root.title("CASH MEMO Translator")
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
        #scrollbar=Scrollbar(root)
        #scrollbar.pack(side=RIGHT,fill='y')
        c=Canvas(root, height=550, width=630).place(x=200,y=100)
        #scrollbar.config(command=c.yview)
        return
    
        def openFile():
            file = askopenfilename(defaultextension=".pdf",filetypes=[("Pdf files", "*.pdf",".txt")])
            if file == "":
                file = None
            else:
                fileEntry.delete(0, END)
                fileEntry.config(fg="blue")
                fileEntry.insert(0, file)


        def convert():
            try:
                pdf = fileEntry.get()
                pdfFile = open(pdf, 'rb')
                
                pdfReader = PdfFileReader(pdfFile)

                
                pageObj = pdfReader.getPage(0)

                
                extractedText = pageObj.extractText()
                readPdf.delete(1.0, END)
                readPdf.insert(INSERT, extractedText)

                
                pdfFile.close()
            except FileNotFoundError:
                fileEntry.delete(0, END)
                fileEntry.config(fg="red")
                fileEntry.insert(0, "Please select a file first")
            except:
                pass


        def save2word():
            text = str(readPdf.get(1.0, END))
            wordfile = asksaveasfile(mode='w', defaultextension=".doc",
                                     filetypes=[("word file", "*.doc"),
                                                ("text file", "*.txt"),
                                                ("Python file", "*.py")])

            if wordfile is None:
                return
            wordfile.write(text)
            wordfile.close()
            print("saved")
            fileEntry.delete(0, END)
            fileEntry.insert(0, "file Extracted and Saved...")



        root = Tk()
        root.geometry("700x500")
        root.config(bg="ivory")
        root.title(" Language Converter")
        root.resizable(0, 0)
        try:
            root.wm_iconbitmap("pdf2.ico")
        except:
            print('icon file is not available')
            pass
        file = ""
        defaultText = "\n\n\n\n\t\t You can select more files from here.\n \t\t  modify that text too."

        appName = Label(root, text="English to Hindi Converter ", font=('Rockwell Bold', 12, 'bold'),
                        bg="ivory", fg='#022D66')
        appName.place(x=250, y=5)

# Select  file
labelFile = Label(root, text="Select File", font=('Rockwell Bold', 10, 'bold'))
labelFile.place(x=30, y=50)
fileEntry = Entry(root, font=('Rockwell Bold', 10, 'bold'))
fileEntry.pack(ipadx=100, pady=50, padx=150)

openFileButton = Button(root, text=" Upload Here ", font=('Rockwell Bold', 10, 'bold'), width=25,
                        bg="#F3DFCA", fg='#022D66', command=openFile)
openFileButton.place(x=240, y=80)

convert2Text = Button(root, text="Read", font=('Rockwell Bold', 10, 'bold'),
                      bg="#F3DFCA", fg='#022D66', width=10, command=convert)
convert2Text.place(x=300, y=120)

readPdf = Text(root, font=('Rockwell Bold', 10, 'bold'), bg="#F3DFCA", fg='#022D66', width=60, height=20, bd=10)
readPdf.pack(padx=20, ipadx=20, pady=20, ipady=20)
readPdf.insert(INSERT, defaultText)

save2Word = Button(root, text="Save File", font=('Rockwell Bold', 10, 'bold'),
                  bg="#022D66", fg='#F3DFCA', command=save2word)
save2Word.place(x=325, y=320)

def Records():
    print("Records Found")

def Settings():
    print("Settings")

def UpdateLib():
    print("Update Library")
    

appName = Label(root, text=" CASH MEMO TRANSLATOR ", font=('Rockwell Bold', 20, 'bold'),bg="#F3DFCA", width=35, fg='#022D66')
appName.place(x=150, y=10)

appName = Label(root, text="Control Panel ", font=('Rockwell Bold', 12, 'bold'),bg="ivory", fg='maroon')
appName.place(x=50, y=70)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

CashMemo = Button(root, text="Cash Memo", font=('Rockwell Bold', 8, 'bold'),
bg="#F3DFCA", fg='#022D66', width=20, command=CashMemo)
CashMemo.place(x=30, y=110)

LanguageConverter = Button(root, text="Language Converter", font=('Rockwell Bold', 8, 'bold'),
bg="#F3DFCA", fg='#022D66', width=20, command=LanguageConverter)
LanguageConverter.place(x=30, y=160)

OpenFiles = Button(root, text="Open Files", font=('Rockwell Bold', 8, 'bold'),
bg="#F3DFCA", fg='#022D66', width=20, command=Records)
OpenFiles.place(x=30, y=210)

Settings = Button(root, text="Settings", font=('Rockwell Bold', 8, 'bold'),
bg="#F3DFCA", fg='#022D66', width=20, command=Settings)
Settings.place(x=30, y=260)

UpdateLib = Button(root, text="Update Library", font=('Rockwell Bold', 8, 'bold'),
bg="#F3DFCA", fg='#022D66', width=20, command=UpdateLib)
UpdateLib.place(x=30, y=320)


mainloop()
