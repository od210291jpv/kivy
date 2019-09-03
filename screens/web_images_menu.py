import random
import string
from kivy.uix.boxlayout import BoxLayout
from kivy.cache import Cache
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.scatter import Scatter
from kivymd.theming import ThemeManager
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
        self.conf_parser.read('userinfo.ini')
        self.username = self.conf_parser['user_info']['username']
        self.items_amount = 0
        self.cur_img = 1
        self.loaded_images = []
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'Red'
        Cache.register('json_cache', timeout=180)
        box = BoxLayout(orientation='vertical', spacing=15, padding=20, size_hint_y=.2)
        self.lower_panel.add_widget(box)
        scan_button = Button(text='Scan for content', on_press=self.scan_content_callback, size_hint_y=.2)
        box.add_widget(scan_button)

    def get_api_response_json(self):
        host_link = r'http://{}:{}/get_json_images/'.format(self.host, self.port)
        data_key = self._load_data_to_cache(requests.get(host_link).json())
        return data_key

    @staticmethod
    def _get_images_list(host, data):
        for x in data.values():
            yield '{}'.format(host) + x[0], x[1]

    @staticmethod
    def _load_data_to_cache(data):
        key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        Cache.append('json_cache', key, data)
        return key

    @staticmethod
    def _get_data_from_cache(key):
        return Cache.get('json_cache', key)

    def add_to_fav_callback(self, image_name):
        host_link = r'http://{}:{}/add_to_favs/'.format(self.host, self.port)
        responce = requests.post(host_link, data={'username': self.username, 'image_name': image_name})
        if responce.status_code == str(200):
            if responce.json()['state'] == 'ok':
                return True
        else:
            print(responce.json())

    def scan_content_callback(self, *args):
        host_link = r'http://{}:{}'.format(self.host, self.port)
        cache_key = self.get_api_response_json()
        data_obj = self._get_data_from_cache(cache_key)
        self.items_amount = len(data_obj)

        if not data_obj:
            cache_key = self.get_api_response_json()
            data_obj = self._get_data_from_cache(cache_key)

        links_generator = self._get_images_list(host_link, data_obj)

        images_pop = Popup(on_dismiss=self.clear_counters)
        images_pop.title = '{} image from {}'.format(self.cur_img, self.items_amount)
        popup_box = BoxLayout(orientation='vertical')
        box_scatter = Scatter(scale=6, auto_bring_to_front=False, do_rotation=False)
        popup_box.add_widget(box_scatter)

        lower_buttons_grid = GridLayout(cols=3, spacing=6, padding=5, size_hint=(1, 0.1))

        img_obj = links_generator.__next__()
        self.image = AsyncImage(source=img_obj[0])
        self.img_name = img_obj[1]

        box_scatter.add_widget(self.image)
        next_button = Button(text='>> Next', on_press=lambda x: self._get_next_image(links_generator, images_pop))
        prev_button = Button(text='<< Prev')
        add_to_fav_button = Button(text='Add to Fav', on_release=lambda x: self.add_to_fav_callback(self.img_name))
        popup_box.add_widget(lower_buttons_grid)
        lower_buttons_grid.add_widget(prev_button)
        lower_buttons_grid.add_widget(add_to_fav_button)
        lower_buttons_grid.add_widget(next_button)

        images_pop.add_widget(popup_box)
        images_pop.open()

    def _get_next_image(self, generetor, popup_obj):
        try:
            img_obj = generetor.__next__()

            self.image.source = img_obj[0]
            self.img_name = img_obj[1]
            self.cur_img += 1
            popup_obj.title = '{} image from {}'.format(self.cur_img, self.items_amount)
        except StopIteration:
            pass

    def clear_counters(self, *args):
        self.items_amount = 0
        self.cur_img = 1
