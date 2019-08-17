from kivy.uix.anchorlayout import AnchorLayout
from kivymd.label import MDLabel


class MenuItemLabel(AnchorLayout):
    def __init__(self, text, **kwargs):
        super(MenuItemLabel, self).__init__(**kwargs)
        self.anchor_x = 'right'
        self.anchor_y = 'top'
        self.size_hint_y = .2
        self.add_widget(MDLabel(text=text))
