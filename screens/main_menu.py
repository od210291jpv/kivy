from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from base_classes.base_screen import BaseScreen
from kivy.clock import Clock


class MainMenuScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(MainMenuScreen, self).__init__(name, *navigate_screens)
        self.label_box = GridLayout(cols=1, spacing=20, size_hint=(1, .25))
        self.lower_panel.orientation = 'vertical'
        self.lower_panel.cols = 1
        self.lower_panel.add_widget(self.label_box)

        self.tts_label = Label(text='Width: {}, Height: {}'.format(self.width, self.height))
        Clock.schedule_interval(self.update_label, 0.5)
        self.tts_input = TextInput(font_size=30)

        self.label_box.add_widget(self.tts_label)
        self.label_box.add_widget(self.tts_input)

    def update_label(self, *args):
        self.tts_label.text = text='Width: {}, Height: {}'.format(self.width, self.height)

