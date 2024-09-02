
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_string(
"""
<OtpScreen>:
    name: 'otp'
    # MDIconButton:
    #     icon: "arrow-left"
    #     size_hint_y:None
    #     pos_hint:{"center_y": .9,"center_x": .1}
    #     on_press: app.change_screen('login') 
    # MDBoxLayout:
    #     orientation: "vertical"
    #     size_hint_y:None
    #     spacing:'15dp'
    #     padding:'15dp'
    #     pos_hint:{"center_x": .5, "center_y": .5}       
    #     MDLabel:
    #         bold:True
    #         pos_hint:{"center_x": .5}
    #         adaptive_size: True
    #         text: "Enter Your OTP Here"
    #         padding: "4dp", "4dp"
    #         allow_selection: True
    #         allow_copy: True
    #         font_size: "48dp"
        
    #     MDCard:
    #         orientation:'horizontal'
    #         radius:15
    #         padding:'15dp'
    #         spacing:'30dp'
    #         adaptive_height:True
    #         pos_hint:{'center_x':.5, 'center_y':.5}
    MDBoxLayout:
        orientation: 'horizontal'
        pos_hint: {"center_y":.93}  
        size_hint_y: None    
        MDGridLayout:
            colas: 6
            padding: 0
            # spacing: '3dp'
            # orientation:'horizontal'
            adaptive_width:True
            MDTextField:
                max_height: "20dp"
                max_width: "2dp"
            MDTextField:
                max_height: "2dp"
                max_width: "2dp"
            MDTextField:
                max_height: "20dp"
                max_width: "2dp"
            MDTextField:
                max_height: "20dp"
                max_width: "2dp"
            MDTextField:
                max_height: "20dp"
                max_width: "2dp"
            MDTextField:
                max_height: "20dp"
                max_width: "2dp"
    # TextIconButton:
    #     text: 'Submit'
    #     icon: 'upload'
                
                

                
"""
)

class OtpScreen(Screen):
    pass