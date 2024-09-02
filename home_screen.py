from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, DictProperty
from kivymd.uix.hero import MDHeroFrom


Builder.load_string('''
<HeroItem>
    size_hint_y: None
    height: "200dp"
    radius: "10dp"

    MDSmartTile:
        id: tile
        size_hint: None, None
        size: root.size
        on_release: root.on_release()

        MDSmartTileImage:
            id: image
            source: "frontend/images/guitar.png"
            radius: dp(10)

        MDSmartTileOverlayContainer:
            id: overlay
            md_bg_color: 0, 0, 0, .5
            adaptive_height: True
            padding: "8dp"
            spacing: "8dp"
            radius: [0, 0, dp(10), dp(10)]

            MDLabel:
                text: root.tag
                theme_text_color: "Custom"
                text_color: "white"
                adaptive_height: True




<HomeScreen>:
    name: "home"
    MDTopAppBar:
        type: "medium"
        pos_hint: {"top": 1}
        theme_bg_color: "Custom"
        md_bg_color: '#F0866B'

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "menu"

        MDTopAppBarTitle:
            text: "Kariakoo"

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "magnify"

            MDActionTopAppBarButton:
                icon: "account"

            MDActionTopAppBarButton:
                icon: "dots-vertical"

    MDScrollView:
        do_scroll_y: True
        effect_cls: 'ScrollEffect'
        bar_width: 0

        BoxLayout:
            adaptive_height: True
            orientation: 'vertical'
            spacing: 20

            Label:
                text: 'Top Linking'
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                padding: '10dp', 0

            ScrollView:
                do_scroll_x: True
                do_scroll_y: False
                bar_width: 0

                BoxLayout:
                    id: top_linking
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 60  # Adjust as needed for item height
                    size_hint_x: None
                    adaptive_width: True  # Expands based on content
                    spacing: 10

            Label:
                text: 'Top Sales'
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                padding: '10dp', 0




<Descriptions>:
    name: "product_descriptions"
    heroes_to: [hero_to]
    MDTopAppBar:
        type: "medium"
        pos_hint: {"top": 1}
        theme_bg_color: "Custom"
        md_bg_color: '#F0866B'

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "arrow-left"

        MDTopAppBarTitle:
            text: "Product View"

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "magnify"

            MDActionTopAppBarButton:
                icon: "account"

            MDActionTopAppBarButton:
                icon: "dots-vertical"

    MDHeroTo:
        id: hero_to
        size_hint: 1, None
        height: "220dp"
        pos_hint: {"top": 1}

''')


class HeroItem(MDHeroFrom):
    text = StringProperty()
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.image.ripple_duration_in_fast = 0.05

        def on_transform_in(self, instance_hero_widget, duration):
            for instance in [
                instance_hero_widget,
                instance_hero_widget._overlay_container,
                instance_hero_widget._image,
            ]:
                Animation(radius=[0, 0, 0, 0], duration=duration).start
                (instance)

        def on_transform_out(self, instance_hero_widget, duration):
            for instance, radius in {
                instance_hero_widget: [dp(10), dp(10), dp(10), dp(10)],
                instance_hero_widget._overlay_container:
                    [0, 0, dp(10), dp(10)],
                instance_hero_widget._image: [dp(10), dp(10), dp(10), dp(10)],
            }.items():
                Animation(
                    radius=radius,
                    duration=duration,
                ).start(instance)

    def on_release(self):
        def switch_screen(*args):
            self.manager.current_heroes = [self.tag]
            self.manager.screens[7].ids.hero_to.tag = self.tag
            self.manager.current = "product_description"

        Clock.schedule_once(switch_screen, .1)


class HomeScreen(Screen):
    def on_enter(self):
        for i in range(12):
            hero_item = HeroItem(
                text=f"Item {i + 1}", tag=f"Tag {i}", manager=self.manager
            )
            if not i % 2:
                hero_item.md_bg_color = "lightgrey"
            self.ids.top_linking.add_widget(hero_item)


class Descriptions(Screen):
    source = StringProperty()
    content = DictProperty(dict())
