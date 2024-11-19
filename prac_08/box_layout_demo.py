"""
Box Layout Demo
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app for creating a box layout."""

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet, display greeting in label text."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear, set input and output label text blank."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
