#import gestures
from gestures import Gestures

#create rock class
class Rock(Gestures):
    def __init__(self):
        super().__init__("Rock", ["Scissors", "Lizard"])
