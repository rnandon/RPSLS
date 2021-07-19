#import gestures
from gestures import Gestures

#create paper class
class Paper(Gestures):
    def __init__(self):
        super().__init__("Paper", ["Rock", "Spock"])