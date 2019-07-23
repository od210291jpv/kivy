import random
import string

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.cache import Cache
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import requests
from base_classes.base_screen import BaseScreen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class ImageButton(ButtonBehavior, AsyncImage):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = super(ImageButton, self).source


class WebImagesMenu(BaseScreen):
    def __init__(self, name, *navigate_screens):
        self.content = {}
        super(WebImagesMenu, self).__init__(name, *navigate_screens)
        Cache.register('json_cache', timeout='180')
        grid = GridLayout(cols=1, size_hint=(1, 0.9))
        self.add_widget(grid)
        self.host_input = TextInput(size_hint=(0.1, 0.1))
        scan_button = Button(text='Scan for content', on_press=self.scan_content_callback)
        grid.add_widget(self.host_input)
        grid.add_widget(scan_button)

    def get_api_response_json(self):
        host = self.host_input.text
        data_key = self._load_data_to_cache(requests.get(host + '/get_json_images/').json())
        return data_key

    @staticmethod
    def _get_images_list(host, data):
        for x in data.values():
            yield host + x

    @staticmethod
    def _load_data_to_cache(data):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        Cache.append('json_cache', key, data)
        return key

    @staticmethod
    def _get_data_from_cache(key):
        return Cache.get('json_cache', key)

    def scan_content_callback(self, *args):
        host = self.host_input.text
        cache_key = self.get_api_response_json()
        data_obj = self._get_data_from_cache(cache_key)

        if not data_obj:
            cache_key = self.get_api_response_json()
            data_obj = self._get_data_from_cache(cache_key)

        links_generator = self._get_images_list(host, data_obj)

        images_pop = Popup()
        popup_box = BoxLayout(orientation='vertical')
        self.image = ImageButton(source=links_generator.next())

        popup_box.add_widget(self.image)
        next_button = Button(text='>> Next', on_press=lambda x: self._get_next_image(links_generator), size_hint=(1, 0.1))
        popup_box.add_widget(next_button)

        images_pop.add_widget(popup_box)
        images_pop.open()

    def _get_next_image(self, generetor):
        self.image.source = generetor.next()
