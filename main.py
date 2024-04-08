from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import random
import main2 as m

class MainScreen(Screen):
    pass


class InGameScreen(Screen):


    def __init__(self, **kwargs):
        super(InGameScreen, self).__init__(**kwargs)
        self.play_round_easy()


    def play_round_easy(self):
        self.input.text = m.choose_note()
        print(self.input.text)
        m.show_score()
        m.set_highscore()
        m.reset_mistakes()
        m.reset_points()


    def press_game_button(self):

        self.note.text = m.choose_note()
        print(self.note.text)

        if self.input.text == self.note.text:
            m.points += 1
            self.input.text = ''
            self.note.text = self.choose_note()
            print('Richtig!')
        else:
            m.mistakes += 1
            print('Falsch!')
            self.input.text = ''
            if m.mistakes >= 3:
                self.manager.current = "score"

class ScoreScreen(Screen):

    def __init__(self, **kwargs):
        super(ScoreScreen, self).__init__(**kwargs)



class ScreensManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
