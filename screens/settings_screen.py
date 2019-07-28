from kivy.config import ConfigParser
from kivy.uix.settings import Settings
from kivymd.theming import ThemeManager

from base_classes.base_screen import BaseScreen


class SettingsScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(SettingsScreen, self).__init__(name, *navigate_screens)
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'Red'
        settings = Settings(on_close=self.open_home_screen)
        s_config = ConfigParser()
        s_config.read('settings.ini')

        settings.add_json_panel('Settings', s_config, 'settings.json')
        self.add_widget(settings)

    def open_home_screen(self, *args):
        self.upper_panel.navigate_home()
