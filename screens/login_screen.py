import requests
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

        self.lower_panel = BoxLayout(orientation='vertical', spacing=5, padding=15)
        self.add_widget(self.lower_panel)

        self.username_input = TextInput(size_hint_y=.6, multiline=False)
        self.password_input = TextInput(size_hint_y=.6, multiline=False)

        self.login_button = Button(text='Login', on_release=self.login_user, size_hint_y=.6, background_normal='',
                                   background_color=[.99, .3, .3, .99])
        self.register_button = Button(text='Registration', on_release=self.go_to_registration, size_hint_y=.6,
                                      background_normal='',  background_color=[.99, .3, .3, .99])

        self.status_label = Label()

        self.lower_panel.add_widget(Label(text='Login', size_hint_y=.6))
        self.lower_panel.add_widget(self.username_input)
        self.lower_panel.add_widget(Label(text='Password', size_hint_y=.6))
        self.lower_panel.add_widget(self.password_input)
        self.lower_panel.add_widget(self.login_button)
        self.lower_panel.add_widget(self.register_button)
        self.lower_panel.add_widget(self.status_label)

    def login_user(self, *args):
        link = r'http://{}:{}/login/'.format(self.host, self.port)
        j_data = {}
        j_data["username"] = self.username_input.text
        j_data["password"] = self.password_input.text

        response = requests.post(link, data=j_data)

        if response.status_code == 200:
            response_data = response.json()
            if response_data['state'] == 'ok':
                self.manager.transition.direction = 'up'
                self.manager.current = self.navigate_to_screen

    def go_to_registration(self, *args):
        self.manager.transition.direction = 'down'
        self.manager.current = self.register_screen
