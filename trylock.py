import tkinter as tk
count = 0

def func(en):
    en.configure(state=tk.NORMAL)
    global count
    count += 1
    count=str(count)
    en.delete(0, tk.END)
    text = str(count)
    en.insert(0, text)
    en.configure(state=tk.DISABLED)
    count=int(count)


root = tk.Tk()

e = tk.Entry(root)
e.pack()

b = tk.Button(root, text='Click', command=lambda: func(e))
b.pack()

root.mainloop()
