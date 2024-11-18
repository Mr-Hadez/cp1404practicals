from kivy.app import App
from kivy.lang import Builder

MILE_TO_KM_CONVERSION = 1.60934


class ConvertMilesToKmApp(App):
    """ ConvertMilesToKmApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = float(value) * MILE_TO_KM_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, input, value):
        """Handle presses on the up/down buttons to change counter."""
        input = int(input)
        input += value
        self.root.ids.input_number.text = str(input)

ConvertMilesToKmApp().run()
