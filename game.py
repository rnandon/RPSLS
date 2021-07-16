from player import Player


class Game:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.player1  # Will always be a human player
        self.player2  # Can be human or ai player
        self.winner = None

    def display_welcome(self):
        pass

    def display_options(self):
        pass

    def run_game(self):
        pass

    def player_turn(self):
        pass

    def round(self):
        pass

    def get_round_winner(self):
        pass

    def check_for_game_winner(self):
        pass