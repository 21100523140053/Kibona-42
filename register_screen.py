from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string(
   """
<RegisterScreen>:
    name: "register"
    MDIconButton:
        icon: "arrow-left"
        size_hint_y:None
        pos_hint:{"center_y": .9,"center_x": .1}
        on_press: app.change_screen('login')
    MDBoxLayout:
        orientation: "vertical"
        size_hint_y:None
        spacing:'15dp'
        padding:'15dp'
        pos_hint:{"center_x": .5, "center_y": .5}
        MDLabel:
            bold:True
            pos_hint:{"center_x": .5}
            adaptive_size: True
            text: "Choose Account!"
            padding: "4dp", "4dp"
            allow_selection: True
            allow_copy: True
            font_size: "48dp"

        MDCard:
            orientation:'vertical'
            radius:15
            padding:'15dp'
            spacing:'30dp'
            adaptive_height:True
            pos_hint:{'center_x':.5, 'center_y':.5}
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                theme_bg_color: "Custom"
                md_bg_color: 'green'
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_press: app.change_screen('seller_register')
                MDIcon:
                    icon:"account"
                    pos_hint:{"center_x": .5,}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Register as a Seller"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                    font_size: "48dp"
            MDLabel:
                bold:True
                pos_hint:{"center_x": .5}
                adaptive_size: True
                text: "or"
                padding: "4dp", "4dp"
                allow_selection: True
                allow_copy: True
                font_size: "48dp"
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                theme_bg_color: "Custom"
                md_bg_color: 'green'
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_press: app.change_screen('customer_register')

                MDIcon:
                    icon:"cart"
                    pos_hint:{"center_x": .5,}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Register as a Customer"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                    font_size: "48dp"
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_release: app.change_screen('login')
                MDIcon:
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Do not have an account? Sign up"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
"""
)


class RegisterScreen(Screen):
    pass
