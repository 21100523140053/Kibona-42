from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Set the window size (width, height)
Window.size = (360, 640)


class MessengerScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MessengerScreen, self).__init__(**kwargs)
        self.padding = 10
        self.spacing = 10

        # Set white background for the screen
        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        # Notification icon on the top-right corner
        icon_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(60, 60))
        icon_layout.pos = (self.width - 70, self.height - 70)  # Top-right position, with some padding

        icon = Label(text='🔔', font_size=50, size_hint=(None, None), size=(50, 50))
        icon_layout.add_widget(icon)

        self.add_widget(icon_layout)

        # Layout for shop buttons (icon buttons) arranged horizontally
        self.shops_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), spacing=10)

        # Example shops with notification counts
        shops = [
            {'name': 'Vunjabei', 'notifications': 10},
            {'name': 'Jiji Store', 'notifications': 15},
            {'name': 'Patabure', 'notifications': 5},
            {'name': 'Beichee', 'notifications': 20},
        ]

        # Add shop buttons (icon buttons with notification count)
        for shop in shops:
            shop_box = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 100))

            # Notification label (showing number of notifications) on top
            notification_label = Label(
                text=str(shop['notifications']),
                font_size=18,
                size_hint_y=None,
                height=50,
                color=(1, 0, 0, 1)  # Red color for the notification number
            )

            # Shop button (acts as icon button)
            shop_button = Button(
                text=shop['name'],
                size_hint=(None, None),
                size=(100, 100),
                background_color=(0.5, 1, 1, 1),  # Gray background for the button
                color=(1, 1, 1, 1)  # White text color for the button
            )

            # Add the notification label and shop button to the shop_box
            shop_box.add_widget(notification_label)
            shop_box.add_widget(shop_button)

            # Add the shop_box to the main shops_layout
            self.shops_layout.add_widget(shop_box)

        # Add shops_layout to the main layout
        self.add_widget(self.shops_layout)
        self.bind(size=self.update_shops_layout_pos)

    def update_shops_layout_pos(self, *args):
        # Update the position of shops_layout to be on the left and centered vertically
        self.shops_layout.pos = (10, self.height / 2 - self.shops_layout.height / 2)  # Left and vertically centered

    def update_rect(self, *args):
        # Update the background rectangle when the layout size or position changes
        self.rect.pos = self.pos
        self.rect.size = self.size

        # Update the position of the notification icon layout to always be at the top-right
        self.children[0].pos = (self.width - 70, self.height - 70)  # Update position dynamically


class MessengerApp(App):
    def build(self):
        return MessengerScreen()


if __name__ == '__main__':
    MessengerApp().run()
