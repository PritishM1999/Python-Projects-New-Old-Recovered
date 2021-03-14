import wx
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Dialog Test",size=(500,400))
        self.panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.log = wx.TextCtrl(self.panel, wx.ID_ANY, size=(400,300),style = wx.TE_MULTILINE|wx.TE_READONLY|wx.VSCROLL)
        self.button = wx.Button(self.panel, label="Click Here To Register")
        sizer.Add(self.log, 0, wx.EXPAND | wx.ALL, 10)
        sizer.Add(self.button, 0, wx.EXPAND | wx.ALL, 10)
        self.panel.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self,event):
        dlg = GetData(parent = self.panel) 
        dlg.ShowModal()
        if dlg.result_DistributorCode:
            self.log.AppendText("Distributor Code: "+dlg.result_DistributorCode+"\n")
            self.log.AppendText("DistributorName: "+dlg.result_DistributorName+"\n")
            self.log.AppendText("MobileNo: "+dlg.result_MobileNo+"\n")
            self.log.AppendText("Email Address: "+dlg.result_Email+"\n")
            self.log.AppendText("OfficeAddress: "+dlg.result_OfficeAddress+"\n")
            self.log.AppendText("District: "+dlg.result_District+"\n")
            self.log.AppendText("SalesRegion: "+dlg.result_SalesRegion+"\n")
            self.log.AppendText("SalesOfficer: "+dlg.result_SalesOfficer+"\n")
            self.log.AppendText("Password: "+dlg.result_Password+"\n")
            self.log.AppendText("Confirm Password: "+dlg.result_ConfirmPassword+"\n")
        else:
            self.log.AppendText("No Input found\n")
        dlg.Destroy()

class GetData(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Name Input", size= (750,620))
        self.panel = wx.Panel(self,wx.ID_ANY)

         #Distributor Code
        self.lblDistributorCode = wx.StaticText(self.panel, label="Distributor Code", pos=(20,20))
        self.DistributorCode = wx.TextCtrl(self.panel, value="", pos=(110,20), size=(500,-1))
        #Distributor Name
        self.lblDistributorName = wx.StaticText(self.panel, label="DistributorName", pos=(20,60))
        self.DistributorName = wx.TextCtrl(self.panel, value="", pos=(110,60), size=(500,-1))
        #Phone No
        self.lblMobileNo = wx.StaticText(self.panel, label="MobileNo", pos=(20,100))
        self.MobileNo = wx.TextCtrl(self.panel, value="", pos=(110,100), size=(500,-1))
    
        #Email Address
        self.lblEmail = wx.StaticText(self.panel, label="Email Address", pos=(20,140))
        self.Email = wx.TextCtrl(self.panel, value="", pos=(110,140), size=(500,-1))
        #Office Address
        self.lblOfficeAddress = wx.StaticText(self.panel, label="OfficeAddress", pos=(20,180))
        self.OfficeAddress = wx.TextCtrl(self.panel, value="", pos=(110,180), size=(500,-1))

       #District
        self.lblDistrict = wx.StaticText(self.panel, label="District", pos=(20,220))
        self.District = wx.TextCtrl(self.panel, value="", pos=(110,220), size=(500,-1))
        #Sales Region
        self.lblSalesRegion = wx.StaticText(self.panel, label="SalesRegion", pos=(20,260))
        self.SalesRegion = wx.TextCtrl(self.panel, value="", pos=(110,260), size=(500,-1))
        #Sales Officer
        self.lblSalesOfficer = wx.StaticText(self.panel, label="SalesOfficer", pos=(20,300))
        self.SalesOfficer = wx.TextCtrl(self.panel, value="", pos=(110,300), size=(500,-1))
        #Password
        self.lblPassword = wx.StaticText(self.panel, label="Password", pos=(20,340))
        self.Password = wx.TextCtrl(self.panel, value="", pos=(110,340), size=(500,-1))
        #ConfirmPAss
        self.lblConfirmPassword = wx.StaticText(self.panel, label="ConfirmPassword", pos=(20,380))
        self.ConfirmPassword = wx.TextCtrl(self.panel, value="", pos=(110,380), size=(500,-1))

        #SaveandClose
        self.saveButton =wx.Button(self.panel, label="Save", pos=(110,420))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(210,460))
    
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.Show()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()

    def SaveConnString(self, event):
        self.result_DistributorCode = self.DistributorCode.GetValue()
        self.result_DistributorName = self.DistributorName.GetValue()
        self.result_MobileNo = self.MobileNo.GetValue()
        self.result_Email = self.Email.GetValue()
        self.result_OfficeAddress = self.OfficeAddress.GetValue()
        self.result_District = self.District.GetValue()
        self.result_SalesRegion = self.SalesRegion.GetValue()
        self.result_SalesOfficer = self.SalesOfficer.GetValue()
        self.result_Password = self.Password.GetValue()
        self.result_ConfirmPassword = self.ConfirmPassword.GetValue()


app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()
