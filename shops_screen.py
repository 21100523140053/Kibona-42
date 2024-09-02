from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Set the window size (width, height)
Window.size = (360, 640)

class ShopsScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ShopsScreen, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 10
        self.spacing = 10

        # Right side layout for shop list
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1.0))

        # Title and shop list
        title = Label(text='Shops List', font_size=24, size_hint_y=None, height=40)
        right_layout.add_widget(title)

        # Scrollable area for shop names and locations
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        shop_layout = GridLayout(cols=1, spacing=8, size_hint_y=None)
        shop_layout.bind(minimum_height=shop_layout.setter('height'))

        # Example shop entries
        shops = [
            {'name': 'Vunjabei', 'location': 'Dar es Salaam, Tanzania'},
            {'name': 'Jiji Store', 'location': 'Nairobi, Kenya'},
            {'name': 'Kigali Mart', 'location': 'Kigali, Rwanda'},
            {'name': 'Kinshasa Plaza', 'location': 'Kinshasa, DR Congo'},
            {'name': 'Bujumbura Market', 'location': 'Bujumbura, Burundi'},
            {'name': 'Kampala Shops', 'location': 'Kampala, Uganda'}
        ]

        # Adding each shop as a box with a border
        for shop in shops:
            shop_box = BoxLayout(orientation='vertical', size_hint_y=None, height=100, padding=10, spacing=5)

            # Drawing the box's border and background
            with shop_box.canvas.before:
                Color(1, 1, 1, 1)  # White background
                Rectangle(pos=shop_box.pos, size=shop_box.size)
                Color(0.5, 0.5, 0.5, 1)  # Grey border
                Rectangle(pos=shop_box.pos, size=shop_box.size)

            # Bind the position and size of the Rectangle to shop_box
            shop_box.bind(pos=self.update_rect, size=self.update_rect)

            shop_name = Label(text=f"Name: {shop['name']}", size_hint_y=None, height=30, color=(0, 0, 0, 1))
            shop_location = Label(text=f"Location: {shop['location']}", size_hint_y=None, height=30, color=(0, 0, 0, 1))
            shop_box.add_widget(shop_name)
            shop_box.add_widget(shop_location)
            shop_layout.add_widget(shop_box)

        scroll_view.add_widget(shop_layout)
        right_layout.add_widget(scroll_view)

        self.add_widget(right_layout)

    def update_rect(self, instance, value):
        # Update the size and position of the rectangles when the layout changes
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)  # White background
            Rectangle(pos=instance.pos, size=instance.size)
            Color(0.5, 0.5, 0.5, 1)  # Grey border
            Rectangle(pos=instance.pos, size=instance.size)


class ShopsApp(App):
    def build(self):
        return ShopsScreen()


if __name__ == '__main__':
    ShopsApp().run()
