# import os
import os
# import flames
from flames import *
# import gtk
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Flames Window
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="FLAMES")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, margin=8)
        self.add(vbox)

        self.label1 = Gtk.Label()
        self.label1.set_text("First Name")
        self.label1.set_justify(Gtk.Justification.LEFT)
        vbox.pack_start(self.label1, True, True, 0)

        self.entry1 = Gtk.Entry()
        vbox.pack_start(self.entry1, True, True, 0)

        self.label2 = Gtk.Label()
        self.label2.set_text("Second Name")
        self.label2.set_justify(Gtk.Justification.LEFT)
        vbox.pack_start(self.label2, True, True, 0)

        self.entry2 = Gtk.Entry()
        vbox.pack_start(self.entry2, True, True, 0)

        self.button = Gtk.Button(label="Get FLAMES")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        firstName = self.entry1.get_text()
        secondName = self.entry2.get_text()
        res = flames(firstName, secondName)
        os.system('notify-send ' + res)

# Start GTK
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
