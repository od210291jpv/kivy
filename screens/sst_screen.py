from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from base_classes.base_screen import BaseScreen
from plyer import stt


class STTScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(STTScreen, self).__init__(name, *navigate_screens)
        box = BoxLayout(orientation='vertical')
        self.grid = GridLayout(cols=2, size_hint_y=0.5)

        self.results_label = Label(text='Result: ')
        self.partial_results_label = Label(text='Partial Res: ')
        self.recognize_button = Button(text='Recognize', on_press=self.stt_start_listen)
        self.clear_button = Button(text='Stop', on_press=self.stt_stop_listen)

        self.grid.add_widget(self.results_label)
        self.grid.add_widget(self.partial_results_label)
        self.grid.add_widget(self.recognize_button)
        self.grid.add_widget(self.clear_button)

        self.add_widget(box)
        box.add_widget(self.grid)

    def update(self):
        self.results_label.text = '\n'.join(stt.results)
        self.partial_results_label.text = '\n'.join(stt.partial_results)

    @staticmethod
    def stt_start_listen(*args):
        if stt.listening:
            stt.stop_listening()
        stt.start()

    def stt_stop_listen(self, *args):
        stt.stop()
        self.update()


