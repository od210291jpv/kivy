from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from base_classes.base_screen import BaseScreen


class MainMenuScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(MainMenuScreen, self).__init__(name, *navigate_screens)
        self.label_box = GridLayout(cols=1, spacing=20, size_hint=(1, .25))
        self.lower_panel.orientation = 'vertical'
        self.lower_panel.cols = 1
        self.lower_panel.add_widget(self.label_box)

        self.tts_label = Label(text='Text to speech')
        self.tts_input = TextInput(font_size=30)

        self.label_box.add_widget(self.tts_label)
        self.label_box.add_widget(self.tts_input)

