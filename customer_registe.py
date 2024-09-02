from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder


Builder.load_string(
  """
<CustomerRegister>:
    name: 'customer_register'
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
                id: username
                MDTextFieldHintText:
                    text: "Username:"
            MDTextField:
                id: email
                validator: "email"
                email_format: "example@example.com"
                MDTextFieldHintText:
                    text: "Email:"
                MDTextFieldHelperText:
                    text: "example@example.com"
                    mode: "on_error"
            MDTextField:
                id: phone number
                MDTextFieldHintText:
                    text: "Phone Number:"
            MDTextField:
                id: passw
                password: True
                MDTextFieldHintText:
                    text: "Password:"
            MDTextField:
                id: passw1
                password: True
                MDTextFieldHintText:
                    text: "Confirm Password:"
            MDBoxLayout:
                adaptive_width: True
                size_hint: .85, None
                height: "30dp"
                pos_hint: {"center_x":.5}
                spacing: "5dp"
                MDCheckbox:
                    id:cd
                    size_hint: None, None
                    width:"30dp"
                    height: "30dp"
                    pos_hint: {"center_x":.5}
                    on_press:
                        passw.password = False if passw.password == True else True

                        passw1.password = False if passw1.password == True else True


                MDLabel:
                    text: "[ref=Show Password]Show Password[/ref]"
                    markup: True
                    pos_hint: cd.pos_hint
                    on_ref_press:
                        cd.active = False if cd.active == True else True
                        passw.password = False if passw.password == True else True
                        passw1.password = False if passw1.password == True else True
            MDButton:
                pos_hint: {"center_x":.5}
                size_hint_y: None
                radius:"4dp"
                MDButtonText:
                    text:"Sign Up"
                MDButtonIcon:
                    icon:"login"
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
                    text: "Have an account? Sign In"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    font_size: "48dp"
"""
)


class CustomerRegister(Screen):

    pass
