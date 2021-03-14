import wx
  
########################################################################
class MyForm(wx.Frame):
  
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Audiometer")
        panel = wx.Panel(self, wx.ID_ANY,size=(1000,600))
        self.SetBackgroundColour((255,255,255))#2nd input change - ShanksD
        self.Centre()#Change -ShanksD
        self.Show()#Change -ShanksD
 
         
        #self.buttonOne.SetPosition((20, 20))
        #self.buttonTwo.SetPosition((40, 40))
        #self.buttonThree.SetPosition((60, 60))
        #self.buttonFour.SetPosition((80, 80))
        #self.buttonFive.SetPosition((100, 100))
        #self.buttonSix.SetPosition((120, 120))
        #self.buttonSeven.SetPosition((140, 140))
  
        sizer = wx.BoxSizer(wx.VERTICAL)
        buttonOne = wx.Button(panel, label="Frequency", name="Frequency")
        buttonTwo = wx.Button(panel, label="Volume", name="Volume")
        buttonThree = wx.Button(panel, label="Pulse Tone", name="Pulse Tone")
        buttonFour = wx.Button(panel, label="Mask", name="Mask")
        buttonFive = wx.Button(panel, label="Air Bone", name="Air Bone")
        buttonSix = wx.Button(panel, label="Test Select", name="Test Select")
        buttonSeven = wx.Button(panel, label="INT", name="INT")
                               
        buttons = [buttonOne, buttonTwo, buttonThree,buttonFour, buttonFive,buttonSix,buttonSeven]
  
        for button in buttons:
            self.buildButtons(button, sizer)
  
        panel.SetSizer(sizer)
  
    #----------------------------------------------------------------------
    def buildButtons(self, btn, sizer):
        """"""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 10, wx.ALL,37 )#Do not Change the VA=alue
  
    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        button = event.GetEventObject()
        print ("The button you pressed was labeled  " + button.Label())
        print ("The button's name is " + button.GetName())
  
        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print ("The button you pressed was labeled: ") + button_by_id.GetLabel()
        print ("The button's name is " + button_by_id.GetName())
  
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
