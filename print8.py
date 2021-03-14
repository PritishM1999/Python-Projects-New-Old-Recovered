from tkinter import *
from threading import Thread
import wx

def f_imprimir(ventana, entry):
    class TextDocPrintout(wx.Printout):
        def __init__(self):
            wx.Printout.__init__(self)

        def OnPrintPage(self, page):
            dc = self.GetDC()

            ppiPrinterX, ppiPrinterY = self.GetPPIPrinter()     
            ppiScreenX, ppiScreenY = self.GetPPIScreen()     
            logScale = float(ppiPrinterX)/float(ppiScreenX)

            pw, ph = self.GetPageSizePixels()
            dw, dh = dc.GetSize()     
            scale = logScale * float(dw)/float(pw)
            dc.SetUserScale(scale, scale)

            logUnitsMM = float(ppiPrinterX)/(logScale*25.4)

            ### Print code ###

            return True

    class PrintFrameworkSample(wx.Frame):        
        def OnPrint(self):
            pdata = wx.PrintData()
            pdata.SetPaperId(wx.PAPER_A4)
            pdata.SetOrientation(wx.LANDSCAPE)

            data = wx.PrintDialogData(pdata)
            printer = wx.Printer(data)

            printout = TextDocPrintout()

            useSetupDialog = True

            if not printer.Print(self, printout, useSetupDialog) and printer.GetLastError() == wx.PRINTER_ERROR:wx.MessageBox(wx.OK)

            else:
                data = printer.GetPrintDialogData() 
                pdata = wx.PrintData(data.GetPrintData()) # force a copy

            printout.Destroy()
            self.Destroy()

    app=wx.App(False)
    PrintFrameworkSample().OnPrint()
    entry.config(state="normal")


def process(ventana, entry):
    entry.config(state="disable")
    t = Thread(target=f_imprimir, args=(ventana,entry))
    t.start()

v = Tk()
entry = Entry(v)
entry.pack()
v.bind("a", lambda a:process(v,entry))
