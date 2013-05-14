#!/usr/bin/env python

from gi.repository import Gtk, Gdk

import pairdefs

class Picker:
    '''RandomSK UI and related functions.'''
    def pick_rand(self, widget=None, data=None):
        '''Pick a random sequence from our current pairdict and set output text.'''
        self.disp.set_text(self.pairdict.pick())

    def copy(self, widget, data=None):
        '''Copy displayed text to the system clipboard.'''
        self.clipboard.set_text(self.disp.get_text(), -1)

    def destroy(self, widget, data=None):
        '''Quit function.'''
        Gtk.main_quit()

    def update_title(self):
        '''Update title string to reflect current pairdict name.'''
        self.title = "RandomSK - %s" % self.key
        self.window.set_title(self.title)
    
    def choose_pair(self, widget=None, data=None):
        '''Store selected pairdict name and pairdict.'''
        self.key = self.pairs_store[self.picker.get_active_iter()][0]
        self.pairdict = self.pairs[self.key]
        self.update_title()
        
    def __init__(self):
        '''Set up UI and internal vars.'''
        self.builder = Gtk.Builder()
        self.builder.add_from_file("randomsk.ui")
        self.title = "RandomSK" #initial title string
        self.pairs = pairdefs.pairs
        
        # get refs to every part we'll be manipulating
        self.disp = self.builder.get_object("output_text") #text field for output
        self.picker = self.builder.get_object("pair_select") #combobox for choosing pairdict
        
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
        
        # set our initial title and display the lot
        self.window = self.builder.get_object("main_window")
        self.window.set_title(self.title)
        self.window.show_all()
        
        # set the initial value for our dropdown, activating update triggers
        self.picker.set_active_iter(self.pairs_store[0].iter)
        self.pick_rand() #pick immediately

def main():
    Gtk.main()
    return

# If the program is run directly or passed as an argument to the python
# interpreter then create a Picker instance and show it
if __name__ == "__main__":
    rsk = Picker()
    main()
