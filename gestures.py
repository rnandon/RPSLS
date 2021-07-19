#create gesture Parent class
class Gestures:
    def __init__(self, name, wins_against):
        self.name = name
        self.wins_against = wins_against

    def __repr__(self):
        return self.name

    # set method 
    def check_against_opponent(self, opponent):
        return opponent.name in self.wins_against