#import gestures
from gestures import Gestures

#create scissors class
class Scissors(Gestures):
    def __init__(self):
        super().__init__("Scissors", ["Paper", "Lizard"])