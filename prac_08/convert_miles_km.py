from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM_CONVERSION = 1.60934


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy App for converting miles to kilometers."""
    km_output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """Handle conversion, output result to label widget."""
        miles = self.validate_float_input(value)
        result = miles * MILE_TO_KM_CONVERSION
        self.km_output = str(result)

    def handle_increment(self, input, value):
        """Handle presses on the up/down buttons to change counter."""
        miles = self.validate_float_input(input)
        miles += value
        self.root.ids.input_number.text = str(miles)

    def validate_float_input(self, input):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(input)
        except ValueError:
            return 0.0

ConvertMilesToKmApp().run()
