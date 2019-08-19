from kivy.uix.accordion import AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage

from base_classes.base_screen import BaseScreen
from kivymd.accordion import MDAccordion

from base_classes.profile_menu_label import MenuItemLabel
from screens.feed_screen import Feed


class MainMenuScreen(BaseScreen):
    def __init__(self, name, *navigate_screens):
        super(MainMenuScreen, self).__init__(name, *navigate_screens)

        self.accordion = MDAccordion(orientation='vertical')

        self.profile = AccordionItem(title='Profile')
        self.feed = AccordionItem(title='Feed')

        self.accordion.add_widget(self.profile)
        self.accordion.add_widget(self.feed)

        self.lower_panel.add_widget(self.accordion)

        base_box = BoxLayout(orientation='vertical')

        box = BoxLayout(orientation='vertical', spacing=5)
        box.add_widget(AsyncImage(source='https://codeguida.com/media/post_title/kivy-logo-black-256_70JCttF.png', size_hint_y=.2, size_hint_x=.5))
        menu_items_box = BoxLayout(orientation='vertical', padding=2, size_hint_y=.5)

        base_box.add_widget(box)
        base_box.add_widget(menu_items_box)

        self.username_label = MenuItemLabel(text='Test username')
        self.followers_label = MenuItemLabel(text='Followers')
        self.posts_amount = MenuItemLabel(text='Posts published')

        menu_items_box.add_widget(self.username_label)
        menu_items_box.add_widget(self.followers_label)
        menu_items_box.add_widget(self.posts_amount)

        self.profile.add_widget(base_box)

        # self.feed.add_widget(FeedItem(image_path='https://codeguida.com/media/post_title/kivy-logo-black-256_70JCttF.png'))
        self.feed.add_widget(Feed())

    def update_label(self, *args):
        pass
