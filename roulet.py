##
# roulet.py
# MR-Spagetty

import random
import os
import time


def no_keyboard_interrupt(function_to_run):
    try:
        function_to_run
    except InterruptedError:
        print("No interrupt for you")


class Gun:
    states = {
        0: """  _____
 /     \\
|  O @  |
| O   O |
|  O O  |
 \\_____/""",
        1: """  _____
 /     \\
|  O O  |
| O   @ |
|  O O  |
 \\_____/""",
        2: """  _____
 /     \\
|  O O  |
| O   O |
|  O @  |
 \\_____/""",
        3: """  _____
 /     \\
|  O O  |
| O   O |
|  @ O  |
 \\_____/""",
        4: """  _____
 /     \\
|  O O  |
| @   O |
|  O O  |
 \\_____/""",
        5: """  _____
 /     \\
|  @ O  |
| O   O |
|  O O  |
 \\_____/"""}

    def __init__(self) -> None:
        self.start_barrel = random.choice(list(self.states.keys()))
        self.shooting_barrel = 1
        self.positions_to_spin = random.randint(15, 30)
        self.time_between_states = 0.1

    def animate(self, points):
        for moved in range(self.positions_to_spin + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            current_state = (self.start_barrel + moved) % 6
            print(self.states[current_state])
            time.sleep(self.time_between_states)
        if current_state == self.shooting_barrel:
            print(" __  __   ______   __  __       ______    ________  "
                  "______   ______\n/_/\\/_/\\ /_____/\\ /_/\\/_/\\     /"
                  "_____/\\  /_______/\\/_____/\\ /_____/\\\n\\ \\ \\ \\ "
                  "\\\\:::_ \\ \\\\:\\ \\:\\ \\    \\:::_ \\ \\ \\__.::._"
                  "\\/\\::::_\\/_\\:::_ \\ \\\n \\:\\_\\ \\ \\\\:\\ \\ \\ "
                  "\\\\:\\ \\:\\ \\    \\:\\ \\ \\ \\   \\::\\ \\  \\:\\/"
                  "___/\\\\:\\ \\ \\ \\\n  \\::::_\\/ \\:\\ \\ \\ \\\\:\\ "
                  "\\:\\ \\    \\:\\ \\ \\ \\  _\\::\\ \\__\\::___\\/_\\:"
                  "\\ \\ \\ \\\n    \\::\\ \\  \\:\\_\\ \\ \\\\:\\_\\:\\ "
                  "\\    \\:\\/.:| |/__\\::\\__/\\\\:\\____/\\\\:\\/.:| |"
                  "\n     \\__\\/   \\_____\\/ \\_____\\/     \\____/_/\\"
                  "________\\/ \\_____\\/ \\____/_/")
            print("you lost the points you bet")
            points = 0
        else:
            print("you survived and the points you bet were doubled you now "
                  f"have {points*2} points")
            points *= 2
        return points


game = Gun()
game.animate(2)