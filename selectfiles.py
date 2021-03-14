from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile


root = Tk()
root.geometry("700x500")
root.config(bg="ivory")
root.title(" HPCL Language Converter")
root.resizable(0, 0)



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
        pdfFile = open(pdf, 'rU', 'rB', 'wb')
        
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

root.mainloop()

#bg="#F3DFCA", fg='#022D66'

