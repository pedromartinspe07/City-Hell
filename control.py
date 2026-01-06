#!/usr/bin/env python3
import json
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

PERM_FILE = "/opt/p-linux/services/p-linux-ai/permissions.json"

class ControlCenter(Gtk.Window):
    def __init__(self):
        super().__init__(title="P-Linux Control Center")
        self.set_border_width(10)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.checks = {}
        for perm in ["voice", "camera", "memory", "disk"]:
            cb = Gtk.CheckButton(label=perm.capitalize())
            cb.connect("toggled", self.on_toggle, perm)
            self.box.pack_start(cb, False, False, 0)
            self.checks[perm] = cb

        self.load_permissions()
        self.show_all()

    def load_permissions(self):
        with open(PERM_FILE) as f:
            perms = json.load(f)
        for k, v in perms.items():
            self.checks[k].set_active(v)

    def on_toggle(self, widget, perm):
        with open(PERM_FILE) as f:
            perms = json.load(f)
        perms[perm] = widget.get_active()
        with open(PERM_FILE, "w") as f:
            json.dump(perms, f, indent=2)

win = ControlCenter()
win.connect("destroy", Gtk.main_quit)
Gtk.main()