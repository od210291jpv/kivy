from requests import Request
from base_classes.base_screen import BaseScreen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class WebAPIMenu(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(WebAPIMenu, self).__init__(name, *navigate_screens)
        pass