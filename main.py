from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.sst_screen import STTScreen
from screens.web_images_menu import WebImagesMenu
from screens.images_menu import ImagesMenu
from screens.main_menu import MainMenuScreen

sm = ScreenManager()
main_menu_screen = MainMenuScreen('Main menu', 'Images', '', 'Main menu')
images_screen = ImagesMenu('Images', 'ApiScreen', 'Main menu', 'Main menu')
api_screen = WebImagesMenu('ApiScreen', 'STT', 'Images', 'Main menu')
stt_screen = STTScreen('STT', '', 'ApiScreen', 'Main menu')

sm.add_widget(main_menu_screen)
sm.add_widget(images_screen)
sm.add_widget(api_screen)
sm.add_widget(stt_screen)


class MainApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    MainApp().run()
