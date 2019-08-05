from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login_screen import LoginScreen
from screens.registration_screen import RegistrationScreen
from screens.settings_screen import SettingsScreen
from screens.web_images_menu import WebImagesMenu
from screens.images_menu import ImagesMenu
from screens.main_menu import MainMenuScreen
from kivymd.theming import ThemeManager

sm = ScreenManager()
login = LoginScreen('Login', 'Main menu', 'registration')
registration = RegistrationScreen('registration', 'Main menu')
main_menu_screen = MainMenuScreen('Main menu', 'Images', '', 'Main menu')
images_screen = ImagesMenu('Images', 'ApiScreen', 'Main menu', 'Main menu')
api_screen = WebImagesMenu('ApiScreen', 'Settings', 'Images', 'Main menu')
settings_screen = SettingsScreen('Settings', '', 'ApiScreen', 'Main menu')

sm.add_widget(login)
sm.add_widget(registration)
sm.add_widget(main_menu_screen)
sm.add_widget(images_screen)
sm.add_widget(api_screen)
sm.add_widget(settings_screen)


class MainApp(App):

    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = 'Dark'
        return sm


if __name__ == '__main__':
    MainApp().run()
