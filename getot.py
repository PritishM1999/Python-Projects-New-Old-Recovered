import wx
from wx import *
import sys

app = wx.App() 

#def quitProgram(*args):
 #   sys.exit()

#def restart(*args):
  #  app.MainLoop()
    

xSize = 500
ySize = 300
window = wx.Frame(None, title = "My GUI", size = (xSize,ySize)) 
panel = wx.Panel(window)     


# generic label
DC = wx.StaticText(panel, label = 'Distributor Code', pos = (2,30))
email=wx.StaticText(panel, label = 'Enter email address', pos = (2,80))
enterotp=wx.StaticText(panel, label = 'Enter OTP', pos = (2,120))
Newpass=wx.StaticText(panel, label = 'New password', pos = (2,150))
Repass=wx.StaticText(panel, label = 'Reenter password', pos = (2,200))
wx.TextCtrl(panel,pos = (200,100), size=(160,22))
wx.TextCtrl(panel,pos = (300,120), size=(160,22))
wx.TextCtrl(panel,pos = (280,150), size=(160,22))
wx.TextCtrl(panel,pos = (350,180), size=(160,22))
wx.TextCtrl(panel,pos = (300,200), size=(160,22))
getotp= wx.Button(panel, label="GetOTP", pos = (100,1), size=(-1,-1))
VerifyOTP = wx.Button(panel, label="VerifyOTP", pos = (200,1), size=(-1,-1))
ConfirmPassword=wx.Button(panel, label="ConfirmOTP", pos = (300,1), size=(-1,-1))
#exit = wx.Button(panel, label="Exit", pos = (1, 1), size=(-1,-1))
#exit.Bind(wx.EVT_BUTTON, quitProgram)
# reset button
#reset = wx.Button(panel, label="Refresh", pos = (100,1), size=(-1,-1))
#reset.Bind(wx.EVT_BUTTON, restart)

window.Show(True) 

app.MainLoop()
