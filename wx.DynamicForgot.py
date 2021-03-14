import wx
from wx import *
from functools import partial
import sys

class MyFrame(wx.Frame):
     def _init_(self):
        super()._init_(None, title='HPCL Reset Password - Translator', size=(740,540))
        self.panel = wx.Panel(self)
   
        wx.StaticText(self.panel, label = 'Distributor Code', pos = (410,140))
        wx.StaticText(self.panel, label = 'Enter email address', pos = (410,180))
        distCodeEntry=wx.TextCtrl(self.panel,pos = (530,137), size=(-1,-1))
        emailid=wx.TextCtrl(self.panel,pos = (530,177), size=(-1,-1))
        getotp = wx.Button(self.panel, label="GetOTP", pos = (545,210), size=(-1,-1))
        #getotp.Bind(wx.EVT_BUTTON, self.Verify())
        self.Bind(wx.EVT_BUTTON, self.Verify)
        self.Show()
   
     def Verify(self,value1):
          wx.StaticText(self.panel, label = 'Enter OTP', pos = (410,250))
          Enterotp=wx.TextCtrl(self.panel,pos = (530,244), size=(-1,-1))
          VerifyOTP = wx.Button(self.panel, label="VerifyOTP", pos = (547,278), size=(-1,-1))
          self.Bind(wx.EVT_BUTTON, self.Password)
          self.Show()

     def Password(self,value):
          wx.StaticText(self.panel, label = 'New password', pos = (410,310))
          Newpass=wx.TextCtrl(self.panel,pos = (530,310), size=(-1,-1))
          wx.StaticText(self.panel, label = 'Re-Enter password', pos = (410,350))
          Repass=wx.TextCtrl(self.panel,pos = (530,345), size=(-1,-1))
          ConfirmPassword=wx.Button(self.panel, label="Confirm Password", pos = (526,380), size=(-1,-1))
          self.Show()

     #def image(self):
      #    image_file = r'C:\Users\ACER\Desktop\INTERNSHIP\backgroundimage.png'
       #   bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #  self.bitmap1 = wx.StaticBitmap(self.panel, -1, bmp1, (0, 0))
         # str1 = "%s  %dx %d" % (image_file, bmp1.GetWidth(),bmp1.GetHeight()) 
          #self.Show()"""


    
               
if _name_ == '_main_':
    app = wx.App()
    #frame1 = wx.Frame(None)
    frame = MyFrame()
    
    #frame.image()
    #panel1 =Panel1(frame1,-1)
    #frame1.Show(True)
    app.MainLoop()
