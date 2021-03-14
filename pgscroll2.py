def MouseWheelHandler(event):
    global count

    def delta(event):
        if event.num == 5 or event.delta < 0:
            return -1 
        return 1 

    count += delta(event)
    print(count)

import tkinter
root = tkinter.Tk()
count = 0
root.bind("<MouseWheel>",MouseWheelHandler)
root.bind("<Button-4>",MouseWheelHandler)
root.bind("<Button-5>",MouseWheelHandler)
root.mainloop()
