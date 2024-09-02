from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, DictProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem

Builder.load_string('''
<ImageLayout>
    id: image_layout
    orientation: 'vertical'
    # size: (60, 80)
    size_hint: (None, None)
    height: 250
    width: 200
    radius: [4,4,4,4]
    FitImage:
        source: root.source
        width: image_layout.width
        height: image_layout.height
        size: image_layout.size
        radius: image_layout.radius
        
    
<GuitarItem>
    theme_bg_color: "Custom"
    md_bg_color: "2d4a50"
    id: card
    size_hint_y:None
    height:"200dp"
    orientation:"horizontal"
    radius:20
    padding:"10dp"
    on_press:app.change_screen('product_descriptions')
    FitImage:
        source: "images/guitar.png"
        radius: card.radius
    MDRelativeLayout:
        BoxLayout:
            orientation:"vertical" 
            spacing: "3dp"
            padding: "10dp"
            MDLabel:
                text: "Ibanez"
                font_style: "Display"
                role: "small"        
            MDLabel:
                text: "GRG121DX-BKF" 
            MDLabel:
                text: "$445,99"
        
<BaseMDNavigationItem>

    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text

<HomeScreen>:
    name: "home"
    MDSliverAppbar:
        background_color: "2d4a50"
        hide_appbar: True
        MDTopAppBar:
            type: "small"
            pos_hint: {"top": 1}
            theme_bg_color: "Custom"
            md_bg_color: '#F0866B'
    
            MDTopAppBarLeadingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "menu"
    
            MDTopAppBarTitle:
                text: "Kariakoo"
    
            MDTopAppBarTrailingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "magnify"
    
                MDActionTopAppBarButton:
                    icon: "account"
    
                MDActionTopAppBarButton:
                    icon: "bell"
        MDSliverAppbarHeader:

            FitImage:
                source: "images/guitar.png"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            theme_bg_color: "Custom"
            md_bg_color: "2d4a50"
            
    
     
    MDNavigationBar:
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem
            icon: "home"
            text: "home"
            active: True

        BaseMDNavigationItem
            icon: "bookmark"
            text: "bookmark"

        BaseMDNavigationItem
            icon: "message"
            text: "message"
        BaseMDNavigationItem
            icon: "cart"
            text: "Cart"
        BaseMDNavigationItem
            icon: "store"
            text: "kariakoo"
            


                
                        

<Descriptions>:
    name: "product_descriptions"
    MDBoxLayout: 
        orientation: "vertical"
        MDTopAppBar:
            type: "small"
            pos_hint: {"top": 1}
            theme_bg_color: "Custom"
            md_bg_color: "2d4a50"
    
            MDTopAppBarLeadingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "arrow-left"
                    on_press: app.change_screen('home')
    
            MDTopAppBarTitle:
                text: "Product View"
    
            MDTopAppBarTrailingButtonContainer:
    
                MDActionTopAppBarButton:
                    icon: "magnify"
    
                MDActionTopAppBarButton:
                    icon: "account"
    
                MDActionTopAppBarButton:
                    icon: "dots-vertical"
                
        MDScrollView:
            do_scroll_y: True
            # effect_cls: 'ScrollEffect'
            bar_width: 0
            MDBoxLayout:
                adaptive_height: True
                orientation: 'vertical'
                spacing: 4
                MDLabel:
                    text: 'Product Image'
                    size_hint_y: None
                    height: self.texture_size[1]
                    bold: True
                    padding: '10dp', 0
                MDBoxLayout:
                    height: 250
                    size_hint_y: None
                    ScrollView:
                        do_scroll_x: True
                        do_scroll_y: False
                        bar_width: 0
                        MDBoxLayout: 
                            id: image_layout  
                            size_hint: None, .85
                            orientation: 'horizontal'
                            adaptive_width: True
                            spacing: 5
                            padding: [5, 0, 0, 0]
                            ImageLayout:
                                source: "images/guitar.png"
                            ImageLayout:
                                source: "images/guitar.png"
                            ImageLayout:
                                source: "images/guitar.png"
                            ImageLayout:
                                source: "images/guitar.png"        
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    adaptive_height: True
                    radius: [10, 10, 0, 0]
                    padding: [0, 0, 0, 4]
                    theme_bg_color: "Custom"
                    md_bg_color: "2d4a50"
                    MDLabel:
                        text: 'Product Descriptions:'
                        size_hint_y: None
                        height: self.texture_size[1]
                        bold: True
                        padding: '10dp', 0
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Name"
                    
                        MDListItemSupportingText:
                            text: "Supporting text"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                            
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Reviews"
                    
                        MDListItemSupportingText:
                            text: "Supporting text"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                            
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Price"
                    
                        MDListItemSupportingText:
                            text: "Supporting text"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                            
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Specifications"
                    
                        MDListItemSupportingText:
                            text: "Supporting text"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                            
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Description"
                    
                        MDListItemSupportingText:
                            text: "Please ensure you have the appropriate permissions. have no cols or rows set, layout is not triggered,have no cols or rows set, layout is not triggered"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                    MDListItem:
                        theme_bg_color: "Custom"
                        md_bg_color: "2d4a50"
                        MDListItemLeadingIcon:
                            icon: "note"
                    
                        MDListItemHeadlineText:
                            text: "Product Shipping Cost"
                    
                        MDListItemSupportingText:
                            text: "Supporting text"
                    
                        MDListItemTrailingIcon:
                            icon: "star"
                    
                        
                    
    MDBoxLayout:
        
'''
                    )


class GuitarItem(MDCard):
    pass


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class HomeScreen(Screen):
    def on_enter(self):
        for x in range(10):
            self.ids.content.add_widget(GuitarItem())


class Descriptions(Screen):
    source = StringProperty()
    content = DictProperty(dict())


class ImageLayout(MDBoxLayout):
    source = StringProperty()
