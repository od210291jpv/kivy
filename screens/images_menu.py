import os

from kivy.core.text import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.gridlayout import GridLayout

from base_classes.base_screen import BaseScreen


class ImagesMenu(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(ImagesMenu, self).__init__(name, *navigate_screens)
        self.lower_grid = BoxLayout(orientation='vertical')
        self.lower_panel.add_widget(self.lower_grid)

        self.filechooser = FileChooserListView()
        self.filechooser.bind(on_selection=lambda x: self.selected(self.filechooser.selection))

        self.open_file_button = Button(text='Open Image', size_hint=(1, .1))
        self.open_file_button.bind(on_release=lambda x: self.open_f(self.filechooser.path, self.filechooser.selection))

        self.lower_grid.add_widget(self.open_file_button)
        self.lower_grid.add_widget(self.filechooser)

    def open_f(self, path, filename):
        print(filename)
        if len(filename) > 0:
            with open(os.path.join(path, filename[0])) as f:
                print(f.read())