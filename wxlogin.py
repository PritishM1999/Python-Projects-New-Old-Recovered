import wx


class MyDealer(wx.Frame):
    def __init__(self, parent, title ="Dealer Login" ):
        super(MyDealer, self).__init__(parent, title=title, size = (700,500))
        self.panel = wx.Panel(self)
        #user_sizer = wx.BoxSizer(wx.HORIZONTAL)
 
        desCode_lbl = wx.StaticText(self.Panel, label = 'Distributor Code :', pos = (410,140))
        desPass_lbl = wx.StaticText(self.Panel, label = 'Password :', pos = (410,180))
        disCodeEntry = wx.TextCtrl(self.Panel, pos = (530,137), size=(-1,-1))
        disPassword = wx.TextCtrl(self.Panel, pos = (530,177), size=(-1,-1))
        self.Show()
        
        '''wx.Dialog.__init__(seif, None, title="Dealer Login", size = (715,540))
        
        self.logged_in = False
        
        dealer_sizer = wx.BoxSizer(wx,Horizontal)

        del_Lbl = wx.StaticText(Self, label="Distributor Code:", pos = (330,30))
        delEntry=wx.TextCtrl(self.panel,pos = (450,30), size=(-1,-1))


        
        wx.StaticText(self.panel, label = 'Distributor Code', pos = (330,30))
        self.show()'''
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyDealer(parent=None, title="Main Application Window")
        self.frame.Show()

        return True
    
app = MyApp()
app.MainLoop()    


'''def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        
class MyPanel(wx.Panel):
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)'''


#if __name__ == "__main__":
   # app = wx.App(True)
#    frame = MainFrame()


