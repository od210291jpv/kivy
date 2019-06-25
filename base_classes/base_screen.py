from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from base_classes.base_upper_panel import BaseUpperPanel


class BaseScreen(Screen):
    def __init__(self, name='', *navigate_screens):
        super(BaseScreen, self).__init__()
        self.name = name
        self.base = self
        self.base_layout = BoxLayout(orientation='vertical', cols=1)
        self.base_upper = BoxLayout(orientation='horizontal', cols=3, size_hint=(1, .10), padding=5, spacing=2)
        self.base_lower = BoxLayout()
        self.upper_panel = BaseUpperPanel(parent=self.base, navigate_screens=navigate_screens)
        self.lower_panel = BoxLayout(orientation='vertical')

        self.base_layout.add_widget(self.base_upper)
        self.base_layout.add_widget(self.base_lower)
        self.base_upper.add_widget(self.upper_panel)
        self.base_lower.add_widget(self.lower_panel)

        self.add_widget(self.base_layout)

        def test_callback():
            print 'test callback'
