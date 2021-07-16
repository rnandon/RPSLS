class Player:
    def __init__(self):
        self.current_gesture = None
        self.total_wins = 0

    def get_gesture(self):
        return self.current_gesture

    def set_gesture(self, gesture):
        self.current_gesture = gesture

    def get_wins(self):
        return self.total_wins

    def win_round(self):
        self.total_wins += 1