from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from base_classes.base_screen import BaseScreen
from screens.images_menu import ImagesMenu, ShowImageScreen
from screens.main_menu import MainMenuScreen

sm = ScreenManager()
main_menu_screen = MainMenuScreen('Main menu', 'Settings', '', 'Main menu')
flash_screen = BaseScreen('Settings', 'Images', 'Main menu', 'Main menu')
images_screen = ImagesMenu('Images', 'Image', 'Settings', 'Main menu')
show_image_screen = ShowImageScreen('Image', '', 'Main menu', 'Main menu')

sm.add_widget(main_menu_screen)
sm.add_widget(flash_screen)
sm.add_widget(images_screen)
sm.add_widget(show_image_screen)


class MainApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MainApp().run()
