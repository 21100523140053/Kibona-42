from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Set the window size (width, height)
Window.size = (360, 640)

class NotificationsScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(NotificationsScreen, self).__init__(**kwargs)
        self.padding = 10
        self.spacing = 10

        # Set white background for the screen
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        # Layout for boxes on the left side
        left_boxes_layout = BoxLayout(
            orientation='vertical', 
            spacing=10, 
            size_hint=(None, 1), 
            width=120,  # Fixed width for the left side boxes
            padding=10
        )
        left_boxes_layout.pos = (0, 0)  # Position on the left side

        # Adding boxes to the left side
        for i in range(3):
            box = BoxLayout(
                orientation='vertical', 
                size_hint=(None, None), 
                size=(120, 100),  # Fixed size for the boxes
                padding=10
            )

            # Set background color for the box
            with box.canvas.before:
                Color(0.8, 0.8, 0.8, 1)  # Light grey background for the box
                Rectangle(size=box.size, pos=box.pos)

            # Box content (text placeholder)
            content = Label(
                text=f"Box {i + 1}",
                size_hint=(1, 1),
                color=(0, 0, 0, 1)
            )
            box.add_widget(content)

            left_boxes_layout.add_widget(box)

        # Add left_boxes_layout to the main layout
        self.add_widget(left_boxes_layout)

        # Layout for content in the center
        content_layout = BoxLayout(
            orientation='vertical', 
            spacing=10, 
            size_hint=(1, 1), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Centered horizontally and vertically
            padding=10
        )

        # Adding content boxes in the center
        for i in range(3):
            content_box = BoxLayout(
                orientation='horizontal', 
                size_hint=(1, None), 
                size=(self.width - 140, 100),  # Adjust width to leave space for left-side boxes
                padding=10
            )

            # Left side of the box (text or image)
            left_widget = Label(
                text=f"Left Side {i + 1}", 
                size_hint=(None, None), 
                size=(100, 100), 
                color=(0, 0, 0, 1)
            )

            # Right side of the box (text or image)
            right_widget = Label(
                text=f"Right Side {i + 1}", 
                size_hint=(None, None), 
                size=(100, 100), 
                color=(0, 0, 0, 1)
            )

            content_box.add_widget(left_widget)
            content_box.add_widget(right_widget)

            content_layout.add_widget(content_box)

        # Add content_layout to the main layout
        self.add_widget(content_layout)

        # Chat Now button at the bottom
        chat_button = Button(
            text="Chat Now",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'center_x': 0.5, 'bottom': 0.05},
            background_color=(0.5, 0.5, 0.5, 1),  # Gray background for the button
            color=(1, 1, 1, 1)  # White text color for the button
        )

        # Add the chat_button to the main layout
        self.add_widget(chat_button)

    def update_rect(self, *args):
        # Update the background rectangle when the layout size or position changes
        self.rect.pos = self.pos
        self.rect.size = self.size

class NotificationsApp(App):
    def build(self):
        return NotificationsScreen()

if __name__ == '__main__':
    NotificationsApp().run()
