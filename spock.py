#import gestures
from gestures import Gestures

#create Spock class
class Spock(Gestures):
    def __init__(self):
        super().__init__("Spock", ["Scissors", "Rock"])