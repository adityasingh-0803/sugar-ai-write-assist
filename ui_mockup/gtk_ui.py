import gi
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GrammarAssistant(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="AI Write Assistant")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.textview = Gtk.TextView()
        vbox.pack_start(self.textview, True, True, 0)

        self.grammar_button = Gtk.Button(label="Correct Grammar")
        self.grammar_button.connect("clicked", self.on_grammar_clicked)
        vbox.pack_start(self.grammar_button, False, False, 0)

        self.suggestion_button = Gtk.Button(label="Suggest Next Sentence")
        self.suggestion_button.connect("clicked", self.on_suggest_clicked)
        vbox.pack_start(self.suggestion_button, False, False, 0)

    def on_grammar_clicked(self, widget):
        buffer = self.textview.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, True)
        response = requests.post("http://localhost:5000/correct", json={"text": text}).json()
        buffer.set_text(response["corrected"])

    def on_suggest_clicked(self, widget):
        buffer = self.textview.get_buffer()
        start_iter, end_iter = buffer.get_bounds()
        text = buffer.get_text(start_iter, end_iter, True)
        response = requests.post("http://localhost:5000/suggest", json={"text": text}).json()
        buffer.set_text(text + " " + response["suggestion"])

win = GrammarAssistant()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
