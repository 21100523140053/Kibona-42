from kivy.uix.accordion import StringProperty
from kivymd.uix.backdrop.backdrop import _BackLayer
from kivymd.uix.backdrop.backdrop import MDCard
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder
# Set the window size (width, height)
Window.size = (360, 640)
Builder.load_string(
"""
<ProductCart>:
    adaptive_height: True
    radius: [10,10,10,10]
    ImageFit:
        source: root.source
        radius: root.radius
    MDBoxLa
"""
)


class ProductCart(MDCard):
    product_name = StringProperty()
    product_price = StringProperty()
    product_quantity = StringProperty()
    product_shipping_cost = StringProperty()
    source = StringProperty()
    pass


class CartScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CartScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 10
        self.spacing = 10

        # Left side layout for keys and buttons
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1), spacing=10, padding=[10, 10, 10, 10])

        # Key-value buttons
        quantity_button = Button(text='Quantity: 3', size_hint_y=None, height=50)
        total_price_button = Button(text='Total Price: $100', size_hint_y=None, height=50)
        total_cost_button = Button(text='Total Cost: $120', size_hint_y=None, height=50)

        # Buttons for actions
        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        checkout_button = Button(text='Checkout', size_hint_y=None, height=50)
        remove_item_button = Button(text='Remove Item', size_hint_y=None, height=50)
        continue_shopping_button = Button(text='Continue Shopping', size_hint_y=None, height=50)
        save_for_later_button = Button(text='Save for Later', size_hint_y=None, height=50)

        button_layout.add_widget(checkout_button)
        button_layout.add_widget(remove_item_button)
        button_layout.add_widget(continue_shopping_button)
        button_layout.add_widget(save_for_later_button)

        # Adding buttons to the left layout in the correct order
        left_layout.add_widget(quantity_button)
        left_layout.add_widget(total_price_button)
        left_layout.add_widget(total_cost_button)
        left_layout.add_widget(button_layout)

        # Adding Customer Information button below button layout
        customer_info_button = Button(text='Customer Information\n', size_hint_y=None, height=50)
        left_layout.add_widget(customer_info_button)

        self.add_widget(left_layout)

        # Right side layout for product list
        top_right_layout = BoxLayout(orientation='vertical', size_hint=(.5, 2.0))

        # Example product entries
        products = [
            {'image': 'path/to/image1.png', 'name': 'Product 1', 'price': '$20'},
            {'image': 'path/to/image2.png', 'name': 'Product 2', 'price': '$30'},
            {'image': 'path/to/image3.png', 'name': 'Product 3', 'price': '$40'}
        ]

        # Title and product list
        title = Label(text='Product List', font_size=24, size_hint_y=None, height=10)
        top_right_layout.add_widget(title)

        # Scrollable area for product images and titles
        scroll_view = ScrollView(size_hint=(1, 0.3), do_scroll_x=True, do_scroll_y=False)
        product_layout = GridLayout(cols=3, spacing=8, size_hint_x=None, height=10)  # Reduced height
        product_layout.bind(minimum_width=product_layout.setter('width'))

        for product in products:
            product_box = BoxLayout(orientation='vertical', size_hint_x=None, width=100, padding=4)  # Adjusted width
            product_image = Image(source=product['image'], size_hint_y=0.6, allow_stretch=True, keep_ratio=False)
            product_details = BoxLayout(orientation='vertical', size_hint_y=0.4)
            product_name = Label(text=product['name'], size_hint_y=None, height=15, font_size=10)  # Adjusted height and font size
            product_price = Label(text=f"Price: {product['price']}", size_hint_y=None, height=15, font_size=10)  # Adjusted height and font size
            product_details.add_widget(product_name)
            product_details.add_widget(product_price)
            product_box.add_widget(product_image)
            product_box.add_widget(product_details)
            product_layout.add_widget(product_box)

        scroll_view.add_widget(product_layout)
        top_right_layout.add_widget(scroll_view)

        self.add_widget(top_right_layout)


class CartApp(App):
    def build(self):
        return CartScreen()


if __name__ == '__main__':
    CartApp().run()
