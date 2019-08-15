from kivy.config import ConfigParser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
import requests


class RegistrationScreen(Screen):
    def __init__(self, screen_name, navigate_to):
        super(RegistrationScreen, self).__init__()
        self.conf_parser = ConfigParser()
        self.conf_parser.read('settings.ini')
        self.host = self.conf_parser['host_settings']['host_ip']
        self.port = self.conf_parser['host_settings']['host_port']

        self.name = screen_name
        self.navigate_to_screen = navigate_to

        self.lower_panel = BoxLayout()
        self.add_widget(self.lower_panel)
        self.username_input = TextInput(size_hint_y=.6)
        self.email_inout = TextInput(text='', size_hint_y=.6)
        self.password_input = TextInput(text='', size_hint_y=.6)
        self.repeat_password_input = TextInput(text='', size_hint_y=.6)
        self.register_button = Button(text='Register user', on_release=self.register, size_hint_y=.7,
                                      background_normal='',  background_color=[.99, .3, .3, .99])
        self.back_to_login_button = Button(text='Back to login', size_hint_y=.7,
                                           background_normal='',  background_color=[.99, .3, .3, .99])

        self.status_label = Label(text='')

        lower_grid = GridLayout(cols=1, spacing=5, padding=15)
        lower_grid.add_widget(Label(text='Username:', size_hint_y=.6))
        lower_grid.add_widget(self.username_input)
        lower_grid.add_widget(Label(text='Email:', size_hint_y=.6))
        lower_grid.add_widget(self.email_inout)
        lower_grid.add_widget(Label(text='Password:', size_hint_y=.6))
        lower_grid.add_widget(self.password_input)
        lower_grid.add_widget(Label(text='Repeat password:', size_hint_y=.6))
        lower_grid.add_widget(self.repeat_password_input)
        lower_grid.add_widget(self.register_button)
        lower_grid.add_widget(self.back_to_login_button)
        lower_grid.add_widget(self.status_label)
        self.lower_panel.add_widget(lower_grid)

    def register(self, *args):
        link = r'http://{}:{}/register/'.format(self.host, self.port)
        j_data = {}
        j_data["username"] = self.username_input.text
        j_data["email"] = self.email_inout.text
        j_data["password"] = self.password_input.text

        if '@' not in j_data['email'] and '.' not in j_data['email']:
            self.status_label.text = 'Incorrect email format'
        elif j_data['password'] != self.repeat_password_input.text:
            self.status_label.text = 'Password and repeat password' + '\r\n' + 'are not equal'
        else:
            try:
                response = requests.post(link, data=j_data)
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data['state'] == 'ok':
                        self.manager.transition.direction = 'up'
                        self.manager.current = self.navigate_to_screen
                    else:
                        self.status_label.text = 'Unexpected error ocurred'
                if response.status_code == 403:
                    self.status_label.text = 'User with such username already exists'
            except:
                self.status_label.text = 'Network error'


