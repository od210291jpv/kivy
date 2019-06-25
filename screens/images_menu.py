import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image

from base_classes.base_screen import BaseScreen


class ShowImageScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(ShowImageScreen, self).__init__(name, *navigate_screens)
        self.image = Image(source=r'')
        self.add_widget(self.image)


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
        if len(filename) > 1:
            pass
        else:
            img_file = os.path.join(path, filename[0])
            # print img_file
            return ShowImageScreen(img_file)
