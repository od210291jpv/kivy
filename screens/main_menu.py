import time

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from plyer import tts, stt


class MainMenuScreen(Screen):
    def __init__(self):
        super(MainMenuScreen, self).__init__()
        self.name = 'Main menu'


class MainMenuUpperPanel(GridLayout):
    def __init__(self, parent=None, **kwargs):
        self.parent_screen = parent
        super(MainMenuUpperPanel, self).__init__(**kwargs)
        self.cols = 3
        self.orientation = 'horizontal'
        self.padding = 2
        self.height = 10
        self.add_widget(Button(text='<< Prev'))
        self.add_widget(Button(text='Home'))
        self.add_widget(Button(text='Next >>', on_press=self.navigation_next))

    def navigation_next(self, args):
        self.parent_screen.manager.current = 'Flash Menu'


class MainMenuLowerPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenuLowerPanel, self).__init__(**kwargs)
        self.label_box = GridLayout(cols=1, spacing=20, orientation='vertical', size_hint=(1, .25))
        self.tts_label = Label(text='Text to speech')
        self.label_box.add_widget(self.tts_label)
        self.add_widget(self.label_box)

        self.tts_input_box = BoxLayout(size_hint=(1, .25))
        self.tts_input = TextInput(font_size=30)
        self.tts_input_box.add_widget(self.tts_input)
        self.add_widget(self.tts_input_box)

        self.buttons_grid = GridLayout(cols=3, orientation='horizontal', padding=10, size_hint=(1, .50), spacing=10)
        self.add_widget(self.buttons_grid)
        self.buttons_grid.add_widget(Button(text='CLR', on_press=self.stt_stop_callback))
        self.buttons_grid.add_widget(Button(text='Read', on_press=self.stt_start_callback))
        self.buttons_grid.add_widget(Button(text='Speak', on_press=self.tts_callback))

        self.stt_listening = None

    def tts_callback(self, *args):
        text = self.tts_input.text
        if len(text) < 1:

            error = Popup(title='No input text entered',
                          content=Label(text='Press enter text and press "Speak"'), size=(10, 10), size_hint=(.50, .50))
            error.open()
        else:
            tts.speak(text)

    @staticmethod
    def stt_start_callback(*args):
        stt.start()

    def stt_stop_callback(self, *args):
        stt.stop()
        time.sleep(4)
        self.tts_label.text = stt.results
