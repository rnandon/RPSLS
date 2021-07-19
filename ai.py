###        IMPORTS
### ========================
from player import Player
import random


class Ai(Player):
    # Gets init method from Player class

    # Distinct implementation, get random gesture for AI player
    def select_gesture(self):
        random_gesture_selector = random.randint(0, len(self.gestures) - 1) # get rand int for range of gestures list - set as current gesture
        gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        selected_gesture = gesture_options[random_gesture_selector]
        return selected_gesture