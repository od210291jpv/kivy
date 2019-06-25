from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class BaseUpperPanel(GridLayout):
    def __init__(self, parent, navigate_screens, **kwargs):
        super(BaseUpperPanel, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.parent_screen = parent

        self.next_screen = navigate_screens[0]
        self.previous_screen = navigate_screens[1]
        self.home_screen = navigate_screens[2]

        self.cols = 3
        self.orientation = 'horizontal'
        self.padding = 2
        self.height = 10
        self.add_widget(Button(text='<< Prev', on_press=self.navigate_back))
        self.add_widget(Button(text='Home', on_press=self.navigate_home))
        self.add_widget(Button(text='Next >>', on_press=self.navigate_next))

    def navigate_next(self, *args):
        if len(self.next_screen) > 0:
            self.parent_screen.manager.current = self.next_screen

    def navigate_back(self, *args):
        if len(self.previous_screen) > 0:
            self.parent_screen.manager.current = self.previous_screen

    def navigate_home(self, *args):
        if len(self.home_screen) > 0:
            self.parent_screen.manager.current = self.home_screen

