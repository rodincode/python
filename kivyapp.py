from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.theming import ThemeManager
from kivymd.utils import asynckivy
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

kv = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Hictchhicher"
            left_action_items: [["menu", lambda x: nav_draw.set_state()]]
        
        MDTabs:
            id: tabs

    FloatLayout:
        MDFillRoundFlatIconButton:
            text: "Pull a Request"
            icon: "language-python"
            line_color: 0, 1, 0, 1
            pos_hint: {"center_x": .5, "center_y": .07}
            on_release: app.tap_target_start()

    NavigationLayout:    
        ScreenManager:
            id: screen_manager
            Screen:
                name: "scr1"
                MDLabel:
                    text: "Welcome to Hicthhicker! Want to ask for some help from your neighbours?"
                    halign: "center"
                    color: "white"
        
            Screen:
                name: "scr2"
                MDLabel:
                    text: "Screen 2"
                    halign: "center"
                        
        MDNavigationDrawer:
            id: nav_draw
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"
            
            AnchorLayout:
                anchor_x: "left"
                size_hint_y: None
                height: avatar.height
    
                Image:
                    id: avatar
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: "data/logo/kivy-icon-256.png"
    
            MDLabel:
                text: "RODINcode"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]
        
            MDLabel:
                text: "rodincode@gmail.com"
                font_style: "Caption"
                size_hint_y: None
                height: self.texture_size[1]
            
            ScrollView:
                MDList:
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr1"
    
                        text: "Home"
                        IconLeftWidget:
                            icon: "home"
    
                    OneLineAvatarListItem:
                        on_press:
                            nav_draw.set_state("close")
                            screen_manager.current = "scr2"
                        text: "About"
                        IconLeftWidget:
                            icon: 'information'
                                
            Widget:
    
    MDFloatingActionButton:
        id: button
        icon: "plus"
        pos: 10, 10
        
    
        
<Tab>:

    MDIconButton:
        id: icon
        icon: app.icons[0]
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
"""
class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class ItemForList(OneLineIconListItem):
    icon = StringProperty()

class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
    
    icons = list(md_icons.keys())[0:30]
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "A700"  # "500"
        self.theme_cls.accent_palette = 'Lime'
        speed_dial = MDFloatingActionButtonSpeedDial()
        speed_dial.hint_animation= True
        speed_dial.right_pad = True
        speed_dial.data = self.data
        speed_dial.root_button_anim = True
        screen= Builder.load_string(kv)
        screen.add_widget(speed_dial)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="Add Trip",
            description_text="Let people know where are you heading",
            widget_position="left_bottom",
        )
        
        return screen

    def on_start(self):
        for name_tab in self.icons:
            self.root.ids.tabs.add_widget(Tab(text=name_tab))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        count_icon = [k for k, v in md_icons.items() if v == tab_text]
        instance_tab.ids.icon.icon = count_icon[0]

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

    def set_list(self):
        async def set_list():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.screen.ids.box.add_widget(
                    ItemForList(icon=name_icon, text=name_icon))
        asynckivy.start(set_list())

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


MyApp().run()


