from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window

# Set the window size (width, height)
Window.size = (360, 640)


class ProductDescriptionScreen(Screen):
    def __init__(self, **kwargs):
        super(ProductDescriptionScreen, self).__init__(**kwargs)

        # Example product data with placeholders for phone, laptop, and cable images
        product_data = {
            'Name': 'Electronics Bundle',
            'Images': ['phone.png', 'laptop.png', 'cable.png'],  # Replace with actual image paths
            'Price': 'Tsh 1,500,000/=',
            'Availability': 'In Stock',
            'Shop': 'Tech Store XYZ',
            'Shipping cost': 'Tsh 20,000/='
        }

        # Set up the overall layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Create a horizontal BoxLayout for multiple images
        if 'Images' in product_data and product_data['Images']:
            images_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=Window.height * 0.3)

            for image_path in product_data['Images']:
                if image_path:
                    image = Image(source=image_path, size_hint=(None, 1), width=Window.width * 0.3)
                    images_layout.add_widget(image)

            main_layout.add_widget(images_layout)

        # Create a GridLayout for the product details
        layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Add product details to the GridLayout
        for key, value in product_data.items():
            if key != 'Images':  # Skip adding the Images key-value to the grid
                key_label = Label(text=key, size_hint_y=None, height=40, halign='right', valign='middle')
                key_label.bind(size=key_label.setter('text_size'))  # Ensure text wraps within label bounds
                value_label = Label(text=value, size_hint_y=None, height=40, halign='left', valign='middle')
                value_label.bind(size=value_label.setter('text_size'))  # Ensure text wraps within label bounds
                layout.add_widget(key_label)
                layout.add_widget(value_label)

        # Wrap the GridLayout in a ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.4))
        scroll_view.add_widget(layout)

        # Add the ScrollView to the main layout
        main_layout.add_widget(scroll_view)

        # Add buttons at the bottom
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50, spacing=10, padding=(10, 10))

        chat_now_button = Button(text="Chat Now", size_hint=(0.5, 1))
        add_to_cart_button = Button(text="Add to Cart", size_hint=(0.5, 1))

        buttons_layout.add_widget(chat_now_button)
        buttons_layout.add_widget(add_to_cart_button)

        # Add buttons layout to the main layout
        main_layout.add_widget(buttons_layout)

        # Add the main layout to the screen
        self.add_widget(main_layout)


class ProductDescriptionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ProductDescriptionScreen(name='product_description'))
        return sm


if __name__ == '__main__':
    ProductDescriptionApp().run()
