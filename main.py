from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
import random

notes = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
mistakes = 0
points = 0
highscore = 0



class MainScreen(Screen):
    pass


class InGameScreen(Screen):


    def choose_note(self):
        return random.choice(notes)
    input = ObjectProperty(None)


    def reset_points(self):
        global points
        points = 0


    def reset_mistakes(self):
        global mistakes
        mistakes = 0



    def show_score(self):
        global points
        self.show_score.text = 'Glückwunsch! du hast ' + str(points) + ' Punkte erreicht.'


    def set_highscore(self):
        global points, highscore
        if points > highscore:
            highscore = points
            self.highscore.text = 'Neuer Highscore: ' + str(highscore) + '!!!'


    def __init__(self, **kwargs):
        super(InGameScreen, self).__init__(**kwargs)

    def press_game_button(self):
        global mistakes, points

        print(self.input.text)

        if self.input.text == self.note.text:
            points += 1
            self.input.text = ''
            self.note.text = self.choose_note()
            print('Richtig!')
        else:
            mistakes += 1
            print('Falsch!')
            self.input.text = ''
            if mistakes >= 3:
                self.manager.current = "score"
                self.show_score()
                self.set_highscore()
                self.reset_mistakes()
                self.reset_points()





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
