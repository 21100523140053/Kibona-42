from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior

from kivymd.app import MDApp
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDExpansionPanel:
        id: panel
        pos_hint: {"center_x": .5, "center_y": .5}

        MDExpansionPanelHeader:

            MDListItem:
                theme_bg_color: "Custom"
                md_bg_color: self.theme_cls.surfaceContainerLowColor
                ripple_effect: False

                MDListItemSupportingText:
                    text: "Categories"

                TrailingPressedIconButton:
                    id: chevron
                    icon: "chevron-right"
                    on_release: app.tap_expansion_chevron(panel, chevron)

        MDExpansionPanelContent:
            orientation: "vertical"
            padding: "12dp", 0, "12dp", 0

            MDLabel:
                text: "Channel information"
                adaptive_height: True
                padding_x: "16dp"
                padding_y: "12dp"

            MDListItem:

                MDListItemLeadingIcon:
                    icon: "electronics_product"
                MDListItemHeadlineText:
                    text: "Electronics Product"

                MDListItemSupportingText:
                    text: "phone"
                    MDListItemSupportingText:
                    text: "pc"
                    MDListItemSupportingText:
                    text: "tv"
                    
                    MDListItemLeadingIcon:
                    icon: "fashions"
                    
                MDListItemHeadlineText:
                    text: "Fashions"
                     MDListItemLeadingIcon:
                    icon: "home_goods"
                    
                MDListItemHeadlineText:
                    text: "Home Goods"
                     MDListItemLeadingIcon:
                    icon: "groceries"
                    
                MDListItemHeadlineText:
                    text: "Groceries"
                     MDListItemLeadingIcon:
                    icon: "book"
                    
                MDListItemHeadlineText:
                    text: "Books and Media"
                     MDListItemLeadingIcon:
                    icon: "media_devices_and_supplies"
                    
                MDListItemHeadlineText:
                    text: "Media devices and Supplies"
                     MDListItemLeadingIcon:
                    icon: "vehicle_parts_and_accessories"
                    
                MDListItemHeadlineText:
                    text: "Vehicle parts and Accessories"
                    
            MDListItem:

                MDListItemLeadingIcon:
                    icon: "tools""

               MDListItemHeadlineText:
                    text: "Tools and Hardwares"

                MDListItemSupportingText:
                    text: "Pc"

                MDListItemTertiaryText:
                    text: "www.instagram.com/KivyMD"
'''


class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)


Example().run()