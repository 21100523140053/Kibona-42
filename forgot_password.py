from kivymd.uix.pickers.datepicker.datepicker import MDTextField

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder



Builder.load_string(
"""
<ForgotPasswordScreen>:
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
            text: "Forgot Password"
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
                id: email
                validator: "email"
                email_format: "example@example.com"              
                MDTextFieldHintText:
                    text: "Email:"

                MDTextFieldHelperText:
                    text: "example@example.com"
                    mode: "on_error"
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
                    text: "Remember Your Password Click Here"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
            MDIconButton:
                icon : "upload"
                radius: "4dp"
                pos_hint: {"center_x": .5}
                on_press: app.change_screen('otp')
            MDCard:
                spacing: "5dp"
                padding: "15dp"
                pos_hint:{"center_x": .5}
                ripple_behavior:True
                height: "40dp"
                radius: '5dp'
                size_hint_y: None
                on_release: app.change_screen('register')
                MDIcon:
                    icon:"register"
                    pos_hint:{"center_x": .5, "center_y": .5}
                MDLabel:
                    size_hint_y: None
                    bold:True
                    pos_hint:{"center_x": .5, "center_y": .5}
                    adaptive_size: True
                    text: "Don't have an account? Sign Up"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
            
        

"""
)


class ForgotPasswordScreen(Screen):
    pass