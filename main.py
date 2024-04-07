from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout


class MainScreen(Screen):
    pass


class InGameScreen(Screen):

    def __init__(self, **kwargs):
        super(InGameScreen, self).__init__(**kwargs)

    def test(self):
        print("test")


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
