###        IMPORTS
### ========================
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class Player:
    def __init__(self):
        self.current_gesture = None
        self.total_wins = 0
        self.is_human = False
        self.gestures = {"Rock": Rock(), "Paper": Paper(), "Scissors": Scissors(), "Lizard": Lizard(), "Spock": Spock()}

    # Get and set current gesture
    def get_gesture(self):
        return self.current_gesture

    def set_gesture(self, gesture_name):
        self.current_gesture = self.gestures[gesture_name]

    # Get and set win count
    def get_wins(self):
        return self.total_wins

    def win_round(self):
        self.total_wins += 1