
import tkinter as tk
import random

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=400, height=400, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Plot some rectangles
        for n in range(50):
            x0 = random.randint(0, 900)
            y0 = random.randint(50, 900)
            x1 = x0, random.randint(50, 100)
            y1 = y0, random.randint(50,100)
            color = ("red", "orange", "yellow", "green", "blue")[random.randint(0,4)]
            self.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill=color, activefill="black", tags=n)
        self.canvas.create_text(50,10, anchor="nw", text="Click and drag to move the canvas\nScroll to zoom.")

        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        #linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #windows scroll
        self.canvas.bind("<MouseWheel>",self.zoomer)

    #move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    #windows zoom
    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #linux zoom
    def zoomerP(self,event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

    '''set c [canvas .c -width 600 -height 500 \
            -xscrollcommand ".shoriz set" \
            -yscrollcommand ".svert set"]

    scrollbar .svert  -orient v -command "$c yview"
    scrollbar .shoriz -orient h -command "$c xview" 
    grid .c      -row 0 -column 0 -columnspan 3 -sticky news
    grid .svert  -row 0 -column 3 -columnspan 1 -sticky ns
    grid .shoriz -row 1 -column 0 -columnspan 3 -sticky ew
    grid columnconfigure . 0 -weight 1
    grid columnconfigure . 1 -weight 1
    grid columnconfigure . 2 -weight 1
    grid rowconfigure . 0 -weight 1
    #  Add a couple of zooming buttons
    button .zoomin  -text "Zoom In"  -command "zoom $c 1.25" 
    button .zoomout -text "Zoom Out" -command "zoom $c 0.8"
    grid .zoomin .zoomout 

    # Set up event bindings for canvas:
    bind $c <3> "zoomMark $c %x %y"
    bind $c <B3-Motion> "zoomStroke $c %x %y"
    bind $c <ButtonRelease-3> "zoomArea $c %x %y"


    #--------------------------------------------------------
    #
    #  zoomMark
    #
    #  Mark the first (x,y) coordinate for zooming.
    #
    #--------------------------------------------------------
    proc zoomMark {c x y} {
        global zoomArea
        set zoomArea(x0) [$c canvasx $x]
        set zoomArea(y0) [$c canvasy $y]
        $c create rectangle $x $y $x $y -outline black -tag zoomArea
    }

    #--------------------------------------------------------
    #
    #  zoomStroke
    #
    #  Zoom in to the area selected by itemMark and
    #  itemStroke.
    #
    #--------------------------------------------------------
    proc zoomStroke {c x y} {
        global zoomArea
        set zoomArea(x1) [$c canvasx $x]
        set zoomArea(y1) [$c canvasy $y]
        $c coords zoomArea $zoomArea(x0) $zoomArea(y0) $zoomArea(x1) $zoomArea(y1)
    }

    #--------------------------------------------------------
    #
    #  zoomArea
    #
    #  Zoom in to the area selected by itemMark and
    #  itemStroke.
    #
    #--------------------------------------------------------
    proc zoomArea {c x y} {
        global zoomArea

        #--------------------------------------------------------
        #  Get the final coordinates.
        #  Remove area selection rectangle
        #--------------------------------------------------------
        set zoomArea(x1) [$c canvasx $x]
        set zoomArea(y1) [$c canvasy $y]
        $c delete zoomArea

        #--------------------------------------------------------
        #  Check for zero-size area
        #--------------------------------------------------------
        if {($zoomArea(x0)==$zoomArea(x1)) || ($zoomArea(y0)==$zoomArea(y1))} {
            return
        }

        #--------------------------------------------------------
        #  Determine size and center of selected area
        #--------------------------------------------------------
        set areaxlength [expr {abs($zoomArea(x1)-$zoomArea(x0))}]
        set areaylength [expr {abs($zoomArea(y1)-$zoomArea(y0))}]
        set xcenter [expr {($zoomArea(x0)+$zoomArea(x1))/2.0}]
        set ycenter [expr {($zoomArea(y0)+$zoomArea(y1))/2.0}]

        #--------------------------------------------------------
        #  Determine size of current window view
        #  Note that canvas scaling always changes the coordinates
        #  into pixel coordinates, so the size of the current
        #  viewport is always the canvas size in pixels.
        #  Since the canvas may have been resized, ask the
        #  window manager for the canvas dimensions.
        #--------------------------------------------------------
        set winxlength [winfo width $c]
        set winylength [winfo height $c]

        #--------------------------------------------------------
        #  Calculate scale factors, and choose smaller
        #--------------------------------------------------------
        set xscale [expr {$winxlength/$areaxlength}]
        set yscale [expr {$winylength/$areaylength}]
        if { $xscale > $yscale } {
            set factor $yscale
        } else {
            set factor $xscale
        }

        #--------------------------------------------------------
        #  Perform zoom operation
        #--------------------------------------------------------
        zoom $c $factor $xcenter $ycenter $winxlength $winylength
    }


    #--------------------------------------------------------
    #
    #  zoom
    #
    #  Zoom the canvas view, based on scale factor 
    #  and centerpoint and size of new viewport.  
    #  If the center point is not provided, zoom 
    #  in/out on the current window center point.
    #
    #  This procedure uses the canvas scale function to
    #  change coordinates of all objects in the canvas.
    #
    #--------------------------------------------------------
    proc zoom { canvas factor \
            {xcenter ""} {ycenter ""} \
            {winxlength ""} {winylength ""} } {

        #--------------------------------------------------------
        #  If (xcenter,ycenter) were not supplied,
        #  get the canvas coordinates of the center
        #  of the current view.  Note that canvas
        #  size may have changed, so ask the window 
        #  manager for its size
        #--------------------------------------------------------
        set winxlength [winfo width $canvas]; # Always calculate [ljl]
        set winylength [winfo height $canvas]
        if { [string equal $xcenter ""] } {
            set xcenter [$canvas canvasx [expr {$winxlength/2.0}]]
            set ycenter [$canvas canvasy [expr {$winylength/2.0}]]
        }

        #--------------------------------------------------------
        #  Scale all objects in the canvas
        #  Adjust our viewport center point
        #--------------------------------------------------------
        $canvas scale all 0 0 $factor $factor
        set xcenter [expr {$xcenter * $factor}]
        set ycenter [expr {$ycenter * $factor}]

        #--------------------------------------------------------
        #  Get the size of all the items on the canvas.
        #
        #  This is *really easy* using 
        #      $canvas bbox all
        #  but it is also wrong.  Non-scalable canvas
        #  items like text and windows now have a different
        #  relative size when compared to all the lines and
        #  rectangles that were uniformly scaled with the 
        #  [$canvas scale] command.  
        #
        #  It would be better to tag all scalable items,
        #  and make a single call to [bbox].
        #  Instead, we iterate through all canvas items and
        #  their coordinates to compute our own bbox.
        #--------------------------------------------------------
        set x0 1.0e30; set x1 -1.0e30 ;
        set y0 1.0e30; set y1 -1.0e30 ;
        foreach item [$canvas find all] {
            switch -exact [$canvas type $item] {
                "arc" -
                "line" -
                "oval" -
                "polygon" -
                "rectangle" {
                    set coords [$canvas coords $item]
                    foreach {x y} $coords {
                        if { $x < $x0 } {set x0 $x}
                        if { $x > $x1 } {set x1 $x}
                        if { $y < $y0 } {set y0 $y}
                        if { $y > $y0 } {set y1 $y}
                    }
                }
            }
        }

        #--------------------------------------------------------
        #  Now figure the size of the bounding box
        #--------------------------------------------------------
        set xlength [expr {$x1-$x0}]
        set ylength [expr {$y1-$y0}]

        #--------------------------------------------------------
        #  But ... if we set the scrollregion and xview/yview 
        #  based on only the scalable items, then it is not 
        #  possible to zoom in on one of the non-scalable items
        #  that is outside of the boundary of the scalable items.
        #
        #  So expand the [bbox] of scaled items until it is
        #  larger than [bbox all], but do so uniformly.
        #--------------------------------------------------------
        foreach {ax0 ay0 ax1 ay1} [$canvas bbox all] {break}

        while { ($ax0<$x0) || ($ay0<$y0) || ($ax1>$x1) || ($ay1>$y1) } {
            # triple the scalable area size
            set x0 [expr {$x0-$xlength}]
            set x1 [expr {$x1+$xlength}]
            set y0 [expr {$y0-$ylength}]
            set y1 [expr {$y1+$ylength}]
            set xlength [expr {$xlength*3.0}]
            set ylength [expr {$ylength*3.0}]
        }

        #--------------------------------------------------------
        #  Now that we've finally got a region defined with
        #  the proper aspect ratio (of only the scalable items)
        #  but large enough to include all items, we can compute
        #  the xview/yview fractions and set our new viewport
        #  correctly.
        #--------------------------------------------------------
        set newxleft [expr {($xcenter-$x0-($winxlength/2.0))/$xlength}]
        set newytop  [expr {($ycenter-$y0-($winylength/2.0))/$ylength}]
        $canvas configure -scrollregion [list $x0 $y0 $x1 $y1]
        $canvas xview moveto $newxleft 
        $canvas yview moveto $newytop 

        #--------------------------------------------------------
        #  Change the scroll region one last time, to fit the
        #  items on the canvas.
        #--------------------------------------------------------
        $canvas configure -scrollregion [$canvas bbox all]
    }


    #  supply a little test data
    for {set i 10} {$i<500} {incr i 30} {
        for {set j 10} {$j<600} {incr j 30} {
            .c create rectangle $i $j [expr {$i+10}] [expr {$j+10}]
            .c create text $i $j -text "($i,$j)" -anchor ne
        }
    }'''

'''from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
import sys
     # enhancer widget
class Enhance(Frame):
    def __init__(self, master, name, enhancer, lo, hi):
        Frame.__init__(self, master)
            # set up the image
        self.tkim = ImageTk.PhotoImage(image.mode, image.size)
        self.enhancer = enhancer(image)
            #mid = (lo + hi)/2
        self.update('1.0') # normalize
            # image window
        Label(self, image=self.tkim).grid()
            # scale
        s = Scale(self, label=name, orient=HORIZONTAL,
                from_=lo, to=hi, resolution=0.01,
                command=self.update)
            #if image == "ip_img.jpg" or image == "not_img.jpg":
             #   s.config(state=DISABLED)
        s.set(self.value)
        s.grid(row=0,column=0)
    def update(self, value):
        self.value = eval(value)
        tkim.paste(self.enhancer.enhance(self.value))'''
