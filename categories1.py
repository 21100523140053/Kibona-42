from kivy.uix.accordion import StringProperty, ListProperty
import asynckivy
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivy.core.window import Window

# Set the window size (width, height)
Window.size = (360, 640)


KV = '''
<ExpansionPanelItem>:
    title: ""
    subcategories: []

    MDExpansionPanelHeader:
        MDListItem:
            theme_bg_color: "Custom"
            md_bg_color: self.theme_cls.surfaceContainerLowColor
            ripple_effect: False

            MDListItemSupportingText:
                text: root.title
            TrailingPressedIconButton:
                id: chevron
                icon: "chevron-right"
                on_release: app.tap_expansion_chevron(root, chevron)

    MDExpansionPanelContent:
        orientation: "vertical"
        padding: "12dp", 0, "12dp", "12dp"
        md_bg_color: self.theme_cls.surfaceContainerLowestColor

        MDLabel:
            text: root.title
            adaptive_height: True
            padding_x: "16dp"
            padding_y: "12dp"

        BoxLayout:
            orientation: "vertical"
            spacing: "4dp"

            # Dynamic subcategory list
            MDListItem:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.surfaceContainerLowestColor
                # MDListItemSupportingText:
                #     text: "Subcategories:"

            BoxLayout:
                orientation: "vertical"
                spacing: "2dp"

                # Dynamically added subcategories
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[0] if len(root.subcategories) > 0 else ""

                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[1] if len(root.subcategories) > 1 else ""

                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[2] if len(root.subcategories) > 2 else ""

                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[3] if len(root.subcategories) > 3 else ""
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[4] if len(root.subcategories) > 4 else ""
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[5] if len(root.subcategories) > 5 else ""
                MDListItem:
                    theme_bg_color: "Custom"
                    md_bg_color: self.theme_cls.surfaceContainerLowestColor
                    MDListItemSupportingText:
                        text: root.subcategories[6] if len(root.subcategories) > 6 else ""

MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    ScrollView:
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}

        MDList:
            id: container
'''


class ExpansionPanelItem(MDExpansionPanel):
    title = StringProperty("")
    subcategories = ListProperty([])


class TrailingPressedIconButton(ButtonBehavior, RotateBehavior, MDListItemTrailingIcon):
    ...


class Example(MDApp):
    def on_start(self):
        async def set_panel_list():
            categories = [
                {"title": "Electronics products", "subcategories": ["Mobile phones", "Chargers and Adapters", "Cameras", "Head and Earphones","Small Phone Appliances","Radios","Televisions"]},
                {"title": "Fashions", "subcategories": ["Clothings", "Shoes", "Bags abd Purses","Jewelry and Accessories","Traditional African Wears"]},
                {"title": "Groceries", "subcategories": ["Fresh Fruits and Vegetables","Meat and Fishes","Grains","Spices and Herbs","Beverages" "Packaged Foods and Snacks"]},
                {"title": "Vehicles Parts", "subcategories": ["Car Batteries", "Tiles","Engine parts","Car Cleaning Supplies","Car accessories"]},
                {"title": "Home Goods", "subcategories": ["Cleaning supplies", "Curtains and Drapes","Home Decor items","Beds"]},
                {"title": "Media Devices and Supplies", "subcategories": ["USB Drivers", "Computer accessories","CDs and DVDs","Memory Cards"]},
                {"title": "Tools and Hardwares", "subcategories": ["Hand Tools", "Construction materials","Plumbing supplies","Electronic Devices","Power Tools"]},
                {"title": "Books and Media", "subcategories": ["Textbooks and Educational materials", "Novels and Literature","Magazines and Newspapers","Religious books"]},
            ]

            for category in categories:
                await asynckivy.sleep(0)
                self.root.ids.container.add_widget(
                    ExpansionPanelItem(title=category["title"], subcategories=category["subcategories"])
                )

        asynckivy.start(set_panel_list())

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def tap_expansion_chevron(self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton):
        Animation(
            padding=[0, dp(12), 0, dp(12)] if not panel.is_open else [0, 0, 0, 0],
            d=0.2,
        ).start(panel)
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(chevron) if not panel.is_open else panel.set_chevron_up(chevron)


Example().run()
