from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import HoverBehavior
from kivy.properties import StringProperty


Builder.load_string(
    """
<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: "vertical"
        size_hint_y:None
        spacing:'15dp'
        padding:'15dp'
        MDLabel:
            bold:True
            pos_hint:{"center_x": .5}
            adaptive_size: True
            text: "Welcome"
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


            MDTextField:
                id: username
                MDTextFieldHintText:
                    text: "Username:"
                    pos_hint:{'center_y':.2}
            MDTextField:
                id: passw
                password: True
                MDTextFieldHintText:
                    text: "Password:"
            MDBoxLayout:
                adaptive_width: True
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5}
                spacing: "5dp"
            MDCheckbox:
                id:cd
                size_hint: None, None
                width:"60dp"
                height: "30dp"
                pos_hint: {"center_x":.8}
                on_press:
                    passw.password = False if passw.password == True else True

            MDLabel:
                text: "[ref=Show Password]Show Password[/ref]"
                markup: True
                pos_hint: cd.pos_hint
                on_ref_press:
                    cd.active = False if cd.active == True else True
                    passw.password = False if passw.password == True else True
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                on_press: app.change_screen('forgot1')
                size_hint_y: None
                MDIcon:
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Forgot Password? Click here"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
            MDButton:
                pos_hint: {"center_x":.5}
                size_hint_y: None
                on_press: app.change_screen('home')
                radius:"4dp"
                MDButtonText:
                    text:"Sign In"
                MDButtonIcon:
                    icon:"login"
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
                md_bg_color: '#F0866B'
                # adaptive_width: True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                MDIcon:
                    icon:"google"
                    pos_hint:{"center_x": .5, "center_y": .5}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Continue with google"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_release: root.go_sign_up()
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

<TextIconButton>:
    spacing: "5dp"
    ripple_behavior:True
    theme_bg_color: "Custom"
    md_bg_color: app.secondary
    adaptive_width: True
    height: "30dp"
    radius: '4dp'

    MDBoxLayout:
        adaptive_width: True
        size_hint: .85, None
        height: "30dp"
        spacing: "5dp"
        MDIconButton:
            radius: '4dp'
            icon: root.icon
            pos_hint: {"center_x":.5, "center_y":.5}
            theme_bg_color: "Custom"
            fill_color_focus: 1,1,0,1
        MDLabel:
            text: root.text
            pos_hint: {"center_x":.5, "center_y":.5}
            theme_text_color:'Custom'
            text_color:"white"

<TextFlatButton>
    spacing: "5dp"
    ripple_behavior:True
    adaptive_width: True
    height: "30dp"
    radius: '4dp'
    MDLabel:
        markup: True
        text: root.text
        pos_hint: {"center_x":.8, "center_y":.5}
    """
)


class LoginScreen(Screen):

    def go_sign_up(self):
        self.manager.current = 'register'


class TextIconButton(MDCard, HoverBehavior):
    text = StringProperty()
    icon = StringProperty()


class TextFlatButton(MDCard, HoverBehavior):
    text = StringProperty()
