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

        self.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8, margin=10)
        self.add(vbox)

        self.entry1 = Gtk.Entry(placeholder_text="First Name")
        vbox.pack_start(self.entry1, True, True, 0)

        self.entry2 = Gtk.Entry(placeholder_text="Second Name")
        vbox.pack_start(self.entry2, True, True, 0)

        self.button = Gtk.Button(label="Get FLAMES")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        firstName = self.entry1.get_text()
        secondName = self.entry2.get_text()
        res = flames(firstName, secondName)
        if res == "Friends":
            os.system('notify-send "Friends" "Maintain Friendship for ever"')
        elif res == "Love":
            os.system('notify-send "Love" ""')
        elif res == "Attraction":
            os.system('notify-send "Attraction" ""')
        elif res == "Marriage":
            os.system('notify-send "Marriage" ""')
        elif res == "Enemy":
            os.system('notify-send "Enemy" ""')
        elif res == "Siblings":
            os.system('notify-send "Siblings" ""')

# Start GTK
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
