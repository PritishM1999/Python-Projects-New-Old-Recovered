import wx
from wx import *
from functools import partial
import sys

def quitProgram(*args):
    sys.exit()

def restart(*args):
    app.MainLoop()




def dealerVerify(event, distCodeEntry, emailid):
    print("Dealer code entered :", distCodeEntry.GetValue())
    print("Phone Number entered :", emailid.GetValue())

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='HPCL Reset Password - Translator', size=(715,540))
        self.panel = wx.Panel(self)
        Newpass=wx.TextCtrl(self.panel,pos = (450,180), size=(-1,-1))
        Repass=wx.TextCtrl(self.panel,pos = (450,210), size=(-1,-1))
        #getotp= wx.Button(panel, label="GetOTP", pos = (350,90), size=(-1,-1))
        VerifyOTP = wx.Button(self.panel, label="Verify OTP", pos = (450,150), size=(-1,-1))
        ConfirmPassword=wx.Button(self.panel, label="Save", pos = (450,240), size=(-1,-1))
        
        #reset button
        #reset = wx.Button(self.panel, label="Refresh", pos = (100,1), size=(-1,-1))
        #reset.Bind(wx.EVT_BUTTON, restart)
        Enterotp=wx.TextCtrl(self.panel,pos = (450,120), size=(-1,-1))
        emailid=wx.TextCtrl(self.panel,pos = (450,60), size=(-1,-1))
        distCodeEntry=wx.TextCtrl(self.panel,pos = (450,30), size=(-1,-1))
        dealerVerify1 = partial(dealerVerify, distCodeEntry,emailid)        
        getotp = wx.Button(self.panel, label="GetOTP", pos = (450,90), size=(-1,-1))
        getotp.Bind(wx.EVT_BUTTON, dealerVerify1)
        image_file = r'C:\Users\PRITESH\Desktop\imgpy\HPCL5.png'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (0, 0))
        str1 = "%s  %dx %d" % (image_file, bmp1.GetWidth(),bmp1.GetHeight()) 

        wx.StaticText(self.panel, label = 'Distributor Code', pos = (330,30))
        
        
        wx.StaticText(self.panel, label = 'Enter email address', pos = (330,60))
        
        
        
        
        


#DC.Bind(wx.EVT_BUTTON,Emailid)

        wx.StaticText(self.panel, label = 'Enter OTP', pos = (330,120))


        wx.StaticText(self.panel, label = 'New password', pos = (330,180))
        wx.StaticText(self.panel, label = 'Re-Enter password', pos = (330,210))
        
        
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    #frame1 = wx.Frame(None)
    frame = MyFrame()
    #panel1 =Panel1(frame1,-1)
    #frame1.Show(True)
    app.MainLoop()
