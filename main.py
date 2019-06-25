from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from base_classes.base_screen import BaseScreen
from screens.main_menu import MainMenuScreen

sm = ScreenManager()
main_menu_screen = MainMenuScreen('Main menu', 'Settings', 'Settings', 'Main menu')
flash_screen = BaseScreen('Settings', 'Main menu', 'Settings', 'Main menu')

sm.add_widget(main_menu_screen)
sm.add_widget(flash_screen)


class MainApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MainApp().run()
