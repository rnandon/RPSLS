from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player1 = None # Will always be a human player
        self.player2 = None # Can be human or ai player
        self.winner = None

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!!\n" + 
            "Here are the Rules:\n\n" +
            "Rock crushes Scissors\n" +
            "Scissors cuts Paper\n" +
            "Paper covers Rock\n" +
            "Rock crushes Lizard\n" +
            "Lizard poisons Spock\n" +
            "Spock smashes Scissors\n" +
            "Scissors decapitates Lizard\n" +
            "Lizard eats Paper\n" +
            "Paper disproves Spock\n" +
            "Spock vaporizes Rock\n")

    def display_options(self):
        pass # currently in select_gestures

    def get_number_of_players(self):
        #display select player "menu"
        print("How many people are playing?  (1 or 2)")

        user_options = ["1", "2"]

        # Get user selection
        selection_invalid = True

        # Validate user selection
        while selection_invalid:
            user_selection = input()
            if user_selection in user_options:
                selection_invalid = False
        
        #instantiate players
        if user_selection == "2":
            self.player2 = Human()
        else:
            self.player2 = Ai()

        self.player1 = Human()

        
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