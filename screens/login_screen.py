from kivy.config import ConfigParser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    def __init__(self, screen_name, navigate_to, register_screen):
        super(LoginScreen, self).__init__()
        self.conf_parser = ConfigParser()
        self.conf_parser.read('settings.ini')
        self.host = self.conf_parser['host_settings']['host_ip']
        self.port = self.conf_parser['host_settings']['host_port']

        self.navigate_to_screen = navigate_to
        self.name = screen_name
        self.register_screen = register_screen

        self.lower_panel = BoxLayout(orientation='vertical', spacing=5, padding=5)
        self.add_widget(self.lower_panel)

        self.username_input = TextInput(text='username')
        self.password_input = TextInput(text='password')

        self.login_button = Button(text='Login', on_release=self.login_user)
        self.register_button = Button(text='Registration', on_release=self.go_to_registration)

        self.status_label = Label()

        self.lower_panel.add_widget(Label(text='Login'))
        self.lower_panel.add_widget(self.username_input)
        self.lower_panel.add_widget(Label(text='Password'))
        self.lower_panel.add_widget(self.password_input)
        self.lower_panel.add_widget(self.login_button)
        self.lower_panel.add_widget(self.register_button)
        self.lower_panel.add_widget(self.status_label)

    def login_user(self, *args):
        pass

    def go_to_registration(self, *args):
        self.manager.transition.direction = 'up'
        self.manager.current = self.register_screen
