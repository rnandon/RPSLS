class Player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.current_gesture = None
        self.total_wins = 0

    # Get and set current gesture
    def get_gesture(self):
        return self.current_gesture

    def set_gesture(self, gesture):
        self.current_gesture = gesture

    # Get and set win count
    def get_wins(self):
        return self.total_wins

    def win_round(self):
        self.total_wins += 1