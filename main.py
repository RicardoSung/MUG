import kivy
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivymd.app import MDApp
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


# class ExtendedButton(
#     RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton
# ):

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.padding = "16dp"
#         Clock.schedule_once(self.set_spacing)

#     def set_spacing(self, interval):
#         self.ids.box.spacing = "12dp"

#     def set_radius(self, *args):
#         if self.rounded_button:
#             self._radius = self.radius = self.height / 4


class LoginDialogContent(MDBoxLayout):
    pass




class MUG(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('./main.kv')

    def LoginDialog(self):
        self.dialog = MDDialog(
            title="Login Your Account",
            type="custom",
            content_cls=LoginDialogContent()
        )
        self.dialog.open()



    def switch_screen(
        self, instance_navigation_rail, instance_navigation_rail_item
    ):
        '''
        Called when tapping on rail menu items. Switches application screens.
        '''

        self.root.ids.screen_manager.current = (
            instance_navigation_rail_item.icon
        )

    # def on_start(self):
    #     navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
    #     navigation_rail_items.reverse()
    #     screen = MDScreen(
    #         md_bg_color=get_color_from_hex("#edd769"),
    #         radius=[18, 0, 0, 0],
    #     )

    #     # box = MDBoxLayout(padding="12dp")

    #     # screen.add_widget(box)
    #     self.root.ids.screen_manager.add_widget(screen)

        return super().on_start()





MUG().run()

















# class ExtendedButton(
#     RoundedRectangularElevationBehavior, MDFillRoundFlatIconButton
# ):
#     '''
#     Implements a button of type
#     `Extended FAB <https://m3.material.io/components/extended-fab/overview>`_.

#     .. rubric::
#         Extended FABs help people take primary actions.
#         They're wider than FABs to accommodate a text label and larger target
#         area.

#     This type of buttons is not yet implemented in the standard widget set
#     of the KivyMD library, so we will implement it ourselves in this class.
#     '''

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.padding = "16dp"
#         Clock.schedule_once(self.set_spacing)

#     def set_spacing(self, interval):
#         self.ids.box.spacing = "12dp"

#     def set_radius(self, *args):
#         if self.rounded_button:
#             self._radius = self.radius = self.height / 4


# class Example(MDApp):
#     def build(self):
#         self.theme_cls.material_style = "M3"
#         self.theme_cls.primary_palette = "Orange"
#         return Builder.load_file("./main.kv")

#     def switch_screen(
#         self, instance_navigation_rail, instance_navigation_rail_item
#     ):
#         '''
#         Called when tapping on rail menu items. Switches application screens.
#         '''

#         self.root.ids.screen_manager.current = (
#             instance_navigation_rail_item.text
#         )

#     def on_start(self):
#         '''Creates application screens.'''

#         navigation_rail_items = self.root.ids.navigation_rail.get_items()[:]
#         navigation_rail_items.reverse()

#         for widget in navigation_rail_items:
#             # name_screen = widget.text
#             screen = MDScreen(
#                 name="name_screen",
#                 md_bg_color=get_color_from_hex("#edd769"),
#                 radius=[18, 0, 0, 0],
#             )
#             box = MDBoxLayout(padding="12dp")
#             # label = MDLabel(
#             #     text=name_screen.capitalize(),
#             #     font_style="H1",
#             #     halign="right",
#             #     adaptive_height=True,
#             #     shorten=True,
#             # )
#             # box.add_widget(label)
#             screen.add_widget(box)
#             self.root.ids.screen_manager.add_widget(screen)
#             self.fps_monitor_start()


# Example().run()











# from kivymd.app import MDApp
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRectangleFlatButton
# from kivy.lang import Builder




# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Orange"  # "Purple", "Red"
#         self.load_all_kv_files("./")
        
#         # screen = MDScreen()

#         # screen.add_widget(
#         #     MDRectangleFlatButton(
#         #         text="Hello, World",
#         #         pos_hint={"center_x": 0.5, "center_y": 0.5},
#         #     )
#         # )
#         # return Builder.load_file("main.kv")

#     def on_start(self):
#         self.fps_monitor_start()


# MainApp().run()
