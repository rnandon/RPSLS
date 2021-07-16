###        IMPORTS
### =======================
from human import Human
from ai import Ai

class Game:
    ###        INITIALIZERS
    ### =======================================
    def __init__(self):
        self.player1 = None # Will always be a human player
        self.player2 = None # Can be human or ai player
        self.winner = None


    ###        DISPLAY METHODS
    ### =======================================
    # Show welcome message and rules
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

    # Display who won the game
    def display_winner(self):
        if self.winner == self.player1:
            print("Player 1 won!!!")
        else:
            print("Player 2 won!!!")

    # Prompt user for number of players and initialize the player objects
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


    ###        GAME LOGIC
    ### ======================================================
    # Main game loop  
    def run_game(self):
        while not self.winner:
            self.round()

    # Main controller for game functions
    def round(self):
        self.player_turn(self.player1)
        self.player_turn(self.player2)

        player1_gesture = self.player1.get_gesture()
        player2_gesture = self.player2.get_gesture()

        print(f'Player 1 chose: {player1_gesture}\nPlayer 2 chose: {player2_gesture}')

        self.get_round_winner(player1_gesture, player2_gesture)

        self.check_for_game_winner()

    # Have the player select a gesture
    def player_turn(self, player):
        # Human players get prompted, AI players automatically select
        player.select_gesture()
        
    # Check to see who won the round
    def get_round_winner(self, player1_gesture, player2_gesture):
        # If both gestures are the same, nobody wins
        # Otherwise either player1 or player2 won (not both)
        p1_won = False

        if player1_gesture == player2_gesture:
            return

        # Check all cases
        # TODO - Refactor into new method
        if player1_gesture == "Rock":
            if player2_gesture == "Scissors" or player2_gesture == "Lizard":
                p1_won = True
        elif player1_gesture == "Scissors":
            if player2_gesture == "Paper" or player2_gesture == "Lizard":
                p1_won = True
        elif player1_gesture == "Paper":
            if player2_gesture == "Rock" or player2_gesture == "Spock":
                p1_won = True
        elif player1_gesture == "Lizard":
            if player2_gesture == "Paper" or player2_gesture == "Spock":
                p1_won = True
        elif player1_gesture == "Spock":
            if player2_gesture == "Scissors" or player2_gesture == "Rock":
                p1_won = True

        # Display who won, increment player's win count
        if p1_won:
            self.player1.win_round()
            print("Player 1 won the round!")
        else:
            self.player2.win_round()
            print("Player 2 won the round!")

    # Check if someone has won the entire game
    def check_for_game_winner(self):
        # Wins stored on each player as a count
        player1_wins = self.player1.get_wins()
        player2_wins = self.player2.get_wins()

        # If either player has 2 or more wins, then they have won best of 3
        if player1_wins >= 2:
            self.winner = self.player1
        elif player2_wins >= 2:
            self.winner = self.player2