import random

notes = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
mistakes = 0
points = 0
highscore = 0


def main():
    command = input('Starte eine Runde (S for start)')
    play = True
    level = ' '

    if command.lower() == 's':
        level = input('Easy [E] oder Hard [H]?')

    while play:
        if command.lower() == 's':

            if level.lower() == 'e':
                play_one_round_easy()
            elif level.lower() == 'h':
                play_one_round_hard()

            again = input('Nochmal?/Modus Wechseln! (Wähle Nochmal(N)/Easy(E)/Hard(H))')

            if again.lower() == 'n':
                continue
            if again.lower() == 'e' or again.lower() == 'h':
                play = True
                level = again.lower()
            else:
                play = False
                print('Schönen Tag noch :)')
        else:
            play = False
            print('Schönen Tag noch :)')


def choose_note():
    return random.choice(notes)


def random_minor_chord():
    global notes
    chosen_note = choose_note()
    note1 = notes[int(notes.index(chosen_note))]

    if notes.index(chosen_note) + 3 <= 11:
        note2 = notes[int(notes.index(chosen_note) + 3)]
    else:
        note2 = notes[int(notes.index(chosen_note) - 9)]

    if notes.index(chosen_note) + 7 <= 11:
        note3 = notes[int(notes.index(chosen_note) + 7)]
    else:
        note3 = notes[int(notes.index(chosen_note) - 5)]
    minor_chord = (note1, note2, note3)
    return minor_chord


def random_major_chord():
    global notes
    chosen_note = choose_note()
    note1 = notes[int(notes.index(chosen_note))]

    if notes.index(chosen_note) + 4 <= 11:
        note2 = notes[int(notes.index(chosen_note) + 4)]
    else:
        note2 = notes[int(notes.index(chosen_note) - 8)]

    if notes.index(chosen_note) + 7 <= 11:
        note3 = notes[int(notes.index(chosen_note) + 7)]
    else:
        note3 = notes[int(notes.index(chosen_note) - 5)]
    major_chord = (note1, note2, note3)
    return major_chord


def reset_points():
    global points
    points = 0


def reset_mistakes():
    global mistakes
    mistakes = 0


def show_score():
    global points
    print('Glückwunsch! du hast ' + str(points) + ' Punkte erreicht.')


def set_highscore():
    global points, highscore
    if points > highscore:
        highscore = points
        print('Neuer Highscore: ' + str(highscore) + '!!!')


def play_one_round_easy():
    global mistakes, points
    chosen_note = choose_note()

    while mistakes <= 2:
        print(chosen_note)
        answer = input()
        if answer.lower() == chosen_note:
            print('Richtig!')
            points += 1
            chosen_note = choose_note()
        elif answer.lower() not in notes:
            print('Diese Option gibt es nicht! Versuche es erneut:')
        else:
            print('Falsch!')
            mistakes += 1

    show_score()
    set_highscore()
    reset_mistakes()
    reset_points()


def play_one_round_hard():
    global mistakes, points
    chord_backup = random.choice([random_minor_chord(), random_major_chord()])
    chord = list(chord_backup)

    while mistakes <= 2:
        print(chord)
        answer1 = input()
        if answer1 in chord:
            chord.remove(answer1)
            answer2 = input()
            if answer2 in chord:
                chord.remove(answer2)
                answer3 = input()
                if answer3 in chord:
                    print('Richtig!')
                    points += 1
                    chord_backup = random.choice([random_minor_chord(), random_major_chord()])
                    chord = list(chord_backup)
                else:
                    print('Falsch!')
                    chord = list(chord_backup)
                    mistakes += 1
            else:
                print('Falsch!')
                chord = list(chord_backup)
                mistakes += 1
        else:
            print('Falsch!')
            chord = list(chord_backup)
            mistakes += 1

    show_score()
    set_highscore()
    reset_mistakes()
    reset_points()
