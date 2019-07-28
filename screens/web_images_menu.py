import random
import string
from kivy.uix.boxlayout import BoxLayout
from kivy.cache import Cache
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivymd.theming import ThemeManager
from kivymd.button import MDRaisedButton
import requests
from base_classes.base_screen import BaseScreen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import ConfigParser


class WebImagesMenu(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(WebImagesMenu, self).__init__(name, *navigate_screens)
        self.conf_parser = ConfigParser()
        self.conf_parser.read('settings.ini')
        self.host = self.conf_parser['host_settings']['host_ip']
        self.port = self.conf_parser['host_settings']['host_port']
        self.content = {}
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'Red'
        Cache.register('json_cache', timeout=180)
        grid = GridLayout(cols=1, size_hint=(1, 0.9), spacing=5, padding=5)
        self.add_widget(grid)
        scan_button = MDRaisedButton(text='Scan for content', on_press=self.scan_content_callback)
        grid.add_widget(scan_button)

    def get_api_response_json(self):
        host_link = r'http://{}:{}/get_json_images/'.format(self.host, self.port)
        data_key = self._load_data_to_cache(requests.get(host_link).json())
        return data_key

    @staticmethod
    def _get_images_list(host, data):
        for x in data.values():
            yield '{}'.format(host) + x

    @staticmethod
    def _load_data_to_cache(data):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        Cache.append('json_cache', key, data)
        return key

    @staticmethod
    def _get_data_from_cache(key):
        return Cache.get('json_cache', key)

    def scan_content_callback(self, *args):
        host_link = r'http://{}:{}'.format(self.host, self.port)
        cache_key = self.get_api_response_json()
        data_obj = self._get_data_from_cache(cache_key)

        if not data_obj:
            cache_key = self.get_api_response_json()
            data_obj = self._get_data_from_cache(cache_key)

        links_generator = self._get_images_list(host_link, data_obj)

        images_pop = Popup()
        popup_box = BoxLayout(orientation='vertical')
        box_scatter = Scatter(scale=4, auto_bring_to_front=False)
        popup_box.add_widget(box_scatter)
        self.image = AsyncImage(source=links_generator.__next__())

        box_scatter.add_widget(self.image)
        next_button = Button(text='>> Next', on_press=lambda x: self._get_next_image(links_generator), size_hint=(1, 0.1))
        popup_box.add_widget(next_button)

        images_pop.add_widget(popup_box)
        images_pop.open()

    def _get_next_image(self, generetor):
        self.image.source = generetor.__next__()
