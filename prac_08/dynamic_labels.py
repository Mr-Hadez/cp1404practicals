from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

NEW_COLOUR = (1, 0, 0, 1)


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = ("Bob Brown", "Cat Cyan", "Oren Ochre")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create label from data and add them to the GUI."""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            temp_label.background_color = NEW_COLOUR
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
