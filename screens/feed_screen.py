from kivy.config import ConfigParser
from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from base_classes.network_interactions import NetworkAdapter


class NewFeedItem(RecycleDataViewBehavior, AsyncImage):
    def __init__(self, **kwargs):
        super(NewFeedItem, self).__init__(**kwargs)
        # grid = FeedItem(self)


Builder.load_string('''
<Feed>:
    viewclass: 'NewFeedItem'
    RecycleBoxLayout:
        default_size: None, dp(300)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')


class Feed(RecycleView):
    def __init__(self, **kwargs):
        super(Feed, self).__init__(**kwargs)
        self.conf_parser = ConfigParser()
        self.conf_parser.read('settings.ini')
        self.host = self.conf_parser['host_settings']['host_ip']
        self.port = self.conf_parser['host_settings']['host_port']

        api_iface = NetworkAdapter(self.host, self.port)
        feed_images = api_iface.get_feed()

        try:
            self.data = [{'source': r'http://{}:{}{}'.format(self.host, self.port, x)} for x in feed_images.values()]
        except AttributeError:
            pass
        print(self.data)
