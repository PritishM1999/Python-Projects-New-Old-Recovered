import wx

class Panel1(wx.Panel):
    """class Panel1 creates a panel with an image on it, inherits wx.Panel"""
    def __init__(self, parent, id):
        # create the panel
        wx.Panel.__init__(self, parent, id)
        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = r'C:\Users\PRITESH\Desktop\imgpy\HPCL5.png'
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight()) 
            parent.SetTitle(str1)
        except IOError:
            print ("Image file %s not found") % imageFile
            raise SystemExit

        # button goes on the image --> self.bitmap1 is the parent
        self.button1 = wx.Button(self.bitmap1, id=-1, label='Button1', pos=(40, 130))

app = wx.App()
# create a window/frame, no parent, -1 is default ID
# change the size of the frame to fit the backgound images
frame1 = wx.Frame(None, -1, "An image on a panel", size=(720, 540))
# create the class instance
panel1 = Panel1(frame1, -1)
frame1.Show(True)
app.MainLoop()

'''import wx
########################################################################
class MainPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def _init_(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        for num in range(4):
            label = "Button %s" % num
            btn = wx.Button(self, label=label)
            sizer.Add(btn, 0, wx.ALL, 5)
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
    
    #----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("butterfly.jpg")
        dc.DrawBitmap(bmp, 0, 0)
        
    
########################################################################
class MainFrame(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def _init_(self):
        """Constructor"""
        wx.Frame._init_(self, None, size=(600,450))
        panel = MainPanel(self)        
        self.Center()
        
########################################################################
class Main(wx.App):
    """"""
    #----------------------------------------------------------------------
    def _init_(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.MainLoop()'''
