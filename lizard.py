#import gestures
from gestures import Gestures

#create lizard class
class Lizard(Gestures):
    def __init__(self):
        super().__init__("Lizard", ["Paper", "Spock"])