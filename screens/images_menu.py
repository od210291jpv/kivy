import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import platform
from kivymd.label import MDLabel

from base_classes.base_screen import BaseScreen


class ImagesMenu(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(ImagesMenu, self).__init__(name, *navigate_screens)
        self.lower_grid = BoxLayout(orientation='vertical')
        self.lower_panel.add_widget(self.lower_grid)

        self.filechooser = FileChooserListView()
        if platform == 'android':
            self.filechooser.path = '/sdcard/DCIM'
        else:
            self.filechooser.path = os.getcwd()
        self.filechooser.bind(on_selection=lambda x: self.selected(self.filechooser.selection))

        self.open_file_button = Button(text='Open Image', size_hint=(1, .1))
        self.open_file_button.bind(on_release=lambda x: self.open_f(self.filechooser.path, self.filechooser.selection))

        self.lower_grid.add_widget(self.open_file_button)
        self.lower_grid.add_widget(self.filechooser)

    def open_f(self, path, filename):
        if not filename:
            img_file = None
            image_pop = Popup()
            image_pop.add_widget(MDLabel(text='No image file selected', halign='center'))
            image_pop.open()
        else:
            img_file = os.path.join(path, filename[0])
        image_pop = Popup()
        image_pop.add_widget(Image(source=img_file))
        image_pop.open() if img_file else ''

    def open_image_screen_callback(self):
        self.upper_panel.navigate_next()
