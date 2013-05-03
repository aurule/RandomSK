#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

# attempt to load gi modules for forward compatability
try:
    import gi
    import gi.pygtkcompat

    gi.pygtkcompat.enable() 
    gi.pygtkcompat.enable_gtk(version='3.0')
except ImportError, e:
    pass # gi module doesn't exist, deal with it

from random import choice

# Available seemings and kiths. Change as you like to suit your needs.
seemings = ["Beast","Darkling","Elemental","Fairest","Ogre","Wizened"]
kiths = {"Beast":[
            "Broadback",
            "Hunterheart",
            "Runnerswift",
            "Skitterskulk",
            "Swimmerskin",
            "Venombite",
            "Windwing"
        ],"Darkling":[
            "Antiquarian",
            "Gravewight",
            "Leechfinger",
            "Mirrorskin",
            "Tunnelgrub"
        ],"Elemental":[
            "Airtouched",
            "Earthbones",
            "Fireheart",
            "Manikin",
            "Waterborn",
            "Woodblood"
        ],"Fairest":[
            "Bright one",
            "Dancer",
            "Draconic",
            "Flowering",
            "Muse"
        ],"Ogre":[
            "Cyclopean",
            "Farwalker",
            "Gargantuan",
            "Gristlegrinder",
            "Stonebones",
            "Water-dweller"
        ],"Wizened":[
            "Artist",
            "Brewer",
            "Chatelaine",
            "Chirurgeon",
            "Smith",
            "Soldier"
        ]}


# Define the gui and its actions.
class Picker:
    def pick_rand(self, widget, data=None):
        seeming = choice(seemings)
        kith = choice(kiths[seeming])
        self.disp.set_text(seeming+" "+kith)

    def copy(self, widget, data=None):
        self.clipboard.set_text(self.disp.get_text())

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.tooltips = gtk.Tooltips()
        
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Random Seeming and Kith")
        self.window.set_default_size(350, 50)
        self.window.set_border_width(10)
        icon = self.window.render_icon(gtk.STOCK_DIALOG_INFO, gtk.ICON_SIZE_BUTTON)
        self.window.set_icon(icon)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
    
        # create master box
        self.allbox = gtk.VBox(False, 10)
        self.window.add(self.allbox)
        
        # create data box
        self.dbox = gtk.HBox(False, 5)
        self.allbox.pack_start(self.dbox, True, True)
        
        # create seeming and kith display widget
        self.disp = gtk.Entry()
        self.dbox.pack_start(self.disp, True, True, 0)
        self.disp.show()
        
        # create copy button
        self.copybtn = gtk.Button()
        self.copybtn.set_relief(gtk.RELIEF_NONE)
        self.copybtn.set_focus_on_click(False)
        copyimg = gtk.Image() #workaround to show an icon instead of text
        copyimg.set_from_stock(gtk.STOCK_COPY, gtk.ICON_SIZE_BUTTON)
        self.copybtn.set_image(copyimg)
        self.copybtn.connect("clicked", self.copy, None)
        self.tooltips.set_tip(self.copybtn, "Copy")
        self.dbox.pack_start(self.copybtn, False, False)
        self.copybtn.show()
        
        # create button box
        self.bbox = gtk.HBox(False, 5)
        self.allbox.pack_start(self.bbox, True, False, 0)
    
        # create buttons and add each to button box
        self.rand = gtk.Button("_Randomize")
        self.rand.set_use_underline(True)
        self.rand.connect("clicked", self.pick_rand, None)
        self.bbox.pack_start(self.rand, False, True, 0)
        self.rand.show()
        
        self.exit = gtk.Button("Exit")
        self.exit.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.bbox.pack_start(self.exit, False, True, 0)
        self.exit.show()
    
        # The final step is to display this newly created widget and its window.
        self.dbox.show()
        self.bbox.show()
        self.allbox.show()
        self.window.show()
        self.pick_rand(self, self.rand) #populate label on startup
        
        # create a clipboard for easy copying
        self.clipboard = gtk.Clipboard(gtk.gdk.display_get_default(), "CLIPBOARD")

    def main(self):
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    choose = Picker()
    choose.main()
