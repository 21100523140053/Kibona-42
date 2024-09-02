from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

# Set the window size (width, height)
Window.size = (360, 640)


class OTPInput(GridLayout):
    def __init__(self, **kwargs):
        super(OTPInput, self).__init__(**kwargs)
        self.cols = 6  # Number of OTP boxes
        self.spacing = 10  # Spacing between OTP boxes

        self.otp_fields = []
        for _ in range(6):
            otp_field = TextInput(
                font_size=24,
                halign='center',
                size_hint=(None, None),
                size=(40, 40),
                input_filter='int',  # Restrict input to numbers only
                multiline=False,
                write_tab=False
            )
            otp_field.bind(text=self.move_focus)
            self.otp_fields.append(otp_field)
            self.add_widget(otp_field)

    def move_focus(self, instance, value):
        if len(value) == 1:
            next_index = (self.otp_fields.index(instance) + 1) % len(self.otp_fields)
            self.otp_fields[next_index].focus = True

    def submit_otp(self, instance):
        otp_code = ''.join([field.text for field in self.otp_fields])
        print(f'OTP Entered: {otp_code}')


class OTPApp(App):
    def build(self):
        # Create the top-center layout
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        box_layout = BoxLayout(orientation='vertical', size_hint=(None, None), height=200)

        otp_input = OTPInput()
        box_layout.add_widget(otp_input)

        # Add the submit button under the OTP boxes
        submit_button = Button(text='Submit', size_hint=(None, None), size=(100, 40))
        submit_button.bind(on_press=otp_input.submit_otp)
        box_layout.add_widget(submit_button)

        anchor_layout.add_widget(box_layout)

        return anchor_layout


if __name__ == '__main__':
    OTPApp().run()
