from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_string(
  """
<Electronic>:
    name: 'electronic'
    MDLabel:
        bold:True
        pos_hint:{"center_x": .5}
        adaptive_size: True
        text: "Sign Left"
        padding: "4dp", "4dp"
        allow_selection: True
        allow_copy: True
        font_size: "48dp"
    MDScrollView:
        orientation:'vertical'
        adaptive_height:True
        pos_hint:{'center_x':.5}
        MDCard:
            orientation:'vertical'
            radius:15
            padding:'15dp'
            spacing:'30dp'
            adaptive_height:True
            pos_hint:{'center_x':.5,}
            MDTextField:
                id: Mobile_phones
                MDTextFieldHintText:
                    text: "mobile phones:"
            MDTextField:
                id: chargers_and_adapters
                MDTextFieldHintText:
                    text: "chargers and adapters:"
            MDTextField:
                id: head_and_earphones
                MDTextFieldHintText:
                    text: "head and earphones:"
            MDTextField:
                id: televisions
                MDTextFieldHintText:
                    text: "televisions:"
            MDTextField:
                id: radios
                MDTextFieldHintText:
                    text: "radios:"
            MDTextField:
                id: cameras
                MDTextFieldHintText:
                    text: "cameras:"
            MDTextField:
                id: small_phones_appliances
                MDTextFieldHintText:
                    text: "small phones appliances:"
            MDBoxLayout:
                adaptive_width: True
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5}
                spacing: "5dp"
            MDButton:
                pos_hint: {"center_x":.5}
                size_hint_y: None
                radius:"4dp"
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
"""
)


class Electronic(Screen):
    pass
