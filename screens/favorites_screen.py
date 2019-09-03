from kivy.config import ConfigParser
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from base_classes.network_interactions import NetworkAdapter


class FavsItem(RecycleDataViewBehavior, AsyncImage):
    def __init__(self, **kwargs):
        super(FavsItem, self).__init__(**kwargs)
        # grid = FeedItem(self)


Builder.load_string('''
<FavoritesScreen>:
    viewclass: 'FavsItem'
    RecycleBoxLayout:
        default_size: None, dp(300)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class FavoritesScreen(RecycleView):
    def __init__(self, **kwargs):
        super(FavoritesScreen, self).__init__(**kwargs)
        self.conf_parser = ConfigParser()
        self.conf_parser.read('settings.ini')
        self.host = self.conf_parser['host_settings']['host_ip']
        self.port = self.conf_parser['host_settings']['host_port']
        self.conf_parser.read('userinfo.ini')
        self.username = self.conf_parser['user_info']['username']

        api_iface = NetworkAdapter(self.host, self.port)
        favs_imgs = api_iface.get_my_favorites(self.username)

        # try:
        self.data = [{'source': r'http://{}:{}{}'.format(self.host, self.port, x[0])} for x in favs_imgs.values()]
        # except AttributeError:
        #     pass
