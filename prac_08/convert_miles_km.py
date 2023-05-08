from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesToKmApp(App):
    """ConvertMilestoKmApp is a Kivy App for converting miles (input) into kilometres (output)"""
    result = StringProperty()
    new_number = StringProperty()

    def build(self):
        """ built the Kivy app for the kv file """
        Window.size = (300, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """ handle calculation, output result to label widget"""
        try:
            self.result = str(float(value) * 1.60934)
        except ValueError:
            pass

    def handle_increment(self, input_number, increment):
        """ handle increase or decrease of inputted number for calculation """
        try:
            self.new_number = str(float(input_number) + increment)
        except ValueError:
            pass


ConvertMilesToKmApp().run()