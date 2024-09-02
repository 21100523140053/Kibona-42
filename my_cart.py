from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

# Set the window size (width, height)
Window.size = (360, 640)


class Shop(BoxLayout):
    def __init__(self, name, total_quantity, shipping_details, price, location, image_source, **kwargs):
        super(Shop, self).__init__(**kwargs)
        self.orientation = 'horizontal'  # Horizontal orientation for image and text side by side
        self.size_hint_y = None
        self.height = 150  # Adjust this to control the box size
        self.padding = 10
        self.spacing = 10

        # Add the product image
        img = Image(source=image_source, size_hint_x=0.3)
        self.add_widget(img)

        # Create a BoxLayout for the shop details
        details_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        details_layout.add_widget(Label(text=f"Shop Name: {name}", font_size=20))
        details_layout.add_widget(Label(text=f"Total Quantity: {total_quantity}"))
        details_layout.add_widget(Label(text=f"Shipping: {shipping_details}"))
        details_layout.add_widget(Label(text=f"Price Range: {price}"))
        details_layout.add_widget(Label(text=f"Location: {location}"))

        # Add the details to the main layout
        self.add_widget(details_layout)


class ShopScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # Creating the 6 shops with product images
        shops = [
            {"name": "Masungule", "total_quantity": 120, "shipping_details": "Free shipping", "price": "$20 - $50", "location": "Dar es Salaam", "image": "masungule_product.jpg"},
            {"name": "Manengo", "total_quantity": 80, "shipping_details": "Paid shipping", "price": "$15 - $40", "location": "Dodoma", "image": "manengo_product.jpg"},
            {"name": "Makande", "total_quantity": 95, "shipping_details": "Free shipping over $100", "price": "$30 - $60", "location": "Mwanza", "image": "makande_product.jpg"},
            {"name": "Masandiko", "total_quantity": 150, "shipping_details": "Express shipping available", "price": "$25 - $55", "location": "Arusha", "image": "masandiko_product.jpg"},
            {"name": "Makumbatile", "total_quantity": 70, "shipping_details": "Paid shipping", "price": "$10 - $35", "location": "Mbeya", "image": "makumbatile_product.jpg"},
            {"name": "Makologoto", "total_quantity": 110, "shipping_details": "Free shipping", "price": "$18 - $45", "location": "Morogoro", "image": "makologoto_product.jpg"}
        ]

        # Add all shops to the layout
        for shop in shops:
            shop_box = Shop(
                name=shop['name'],
                total_quantity=shop['total_quantity'],
                shipping_details=shop['shipping_details'],
                price=shop['price'],
                location=shop['location'],
                image_source=shop['image']  # Pass image source here
            )
            self.add_widget(shop_box)


class ShopApp(App):
    def build(self):
        return ShopScreen()


if __name__ == '__main__':
    ShopApp().run()
