#!/usr/bin/env python

from gi.repository import Gtk, Gdk

import pairdefs

# Define the gui and its actions.
class Picker:
    def pick_rand(self, widget=None, data=None):
        self.disp.set_text(self.pairdict.pick())

    def copy(self, widget, data=None):
        self.clipboard.set_text(self.disp.get_text(), -1)

    def delete_event(self, widget, event, data=None):
        return False

    def destroy(self, widget, data=None):
        Gtk.main_quit()

    def update_title(self):
        self.title = "RandomSK - %s" % self.key
        self.window.set_title(self.title)
    
    def choose_pair(self, widget=None, data=None):
        self.key = self.pairs_store[self.picker.get_active_iter()][0]
        self.pairdict = self.pairs[self.key]
        self.update_title()
        
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("randomsk.ui")
        self.title = "RandomSK"
        self.pairs = pairdefs.pairs
        
        # get refs to every part we'll be manipulating
        self.disp = self.builder.get_object("output_text")
        self.picker = self.builder.get_object("pair_select")
        
        # set up the picker's label store and attach
        self.pairs_store = Gtk.ListStore(str)
        for k in sorted(self.pairs.keys()):
            self.pairs_store.append([k])
        self.picker.set_model(self.pairs_store)
        renderer_text = Gtk.CellRendererText()
        self.picker.pack_start(renderer_text, True)
        self.picker.add_attribute(renderer_text, "text", 0)
        
        # set up signal handlers
        handlers_main = {
            "app.quit": self.destroy,
            "app.generate": self.pick_rand,
            "app.do_copy": self.copy,
            "app.pick": self.choose_pair
        }
        self.builder.connect_signals(handlers_main)
        
        # create a clipboard for easy copying
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        
        #set our initial title and display the lot
        self.window = self.builder.get_object("main_window")
        self.window.set_title(self.title)
        self.window.show_all()
        
        # set the value for our dropdown, activating update triggers
        self.picker.set_active_iter(self.pairs_store[0].iter)
        self.pick_rand()

def main():
    Gtk.main()
    return

# If the program is run directly or passed as an argument to the python
# interpreter then create a Picker instance and show it
if __name__ == "__main__":
    choose = Picker()
    main()
