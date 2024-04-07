from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MainScreen(Screen):
    pass


class InGameScreen(Screen):

    input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(InGameScreen, self).__init__(**kwargs)

    def press_game_button(self):
        print(self.input.text)



class ScoreScreen(Screen):
    pass


class ScreensManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
