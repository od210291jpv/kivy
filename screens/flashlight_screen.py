from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from plyer import flash


class FlashLightScreen(Screen):
    def __init__(self):
        super(FlashLightScreen, self).__init__()
        self.name = 'Flash Menu'

    def navigate_callback(self):
        self.manager.current = 'Main Menu'


class FlashLightScreenLowerPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(FlashLightScreenLowerPanel, self).__init__(**kwargs)
        self.add_widget(Button(text='Flash on', on_press=lambda x: flash.on()))
        self.add_widget(Button(text='Flash off', on_press=lambda x: flash.off()))
