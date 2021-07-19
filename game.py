###        IMPORTS
### =======================
from human import Human
from ai import Ai
from user_interface import User_Interface

class Game:
    ###        INITIALIZERS
    ### =======================================
    def __init__(self):
        self.player1 = None # Will always be a human player
        self.player2 = None # Can be human or ai player
        self.winner = None
        self.winner_name = ""
        self.ui = User_Interface()

        # Start the game
        self.run_game()


    ###        DISPLAY METHODS  => moving to ui
    ### =======================================

    # Display who won the game
    def display_winner(self):
        if self.winner == self.player1:
            print("Player 1 won!!!")
        else:
            print("Player 2 won!!!")

    # Prompt user for number of players and initialize the player objects
    def get_number_of_players(self):
        user_selection = self.ui.display_player_number_prompt()
        
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
        # Initialize game screen
        self.ui.display_welcome(['Rock, Paper, Scissors,', 'Lizard, Spock'])
        self.get_number_of_players()

        # Core game loop - while there is no game winner the game continues
        while not self.winner:
            self.round()

        # Once there is a winner, show it
        self.ui.display_winner(self.winner_name)

    # Main controller for game functions
    def round(self):
        # instantiate player turn method below
        self.player_turn(self.player1)
        self.player_turn(self.player2)

        #store player gesture in variable
        player1_gesture = self.player1.get_gesture()
        player2_gesture = self.player2.get_gesture()

        #determine the round winner
        winner = self.get_round_winner(player1_gesture, player2_gesture)

        #displays player selections and round results
        self.ui.display_results(player1_gesture, player2_gesture, winner)

        #check to see if a player has won two times and won game
        self.check_for_game_winner()

    # Have the player select a gesture
    def player_turn(self, player):
        new_gesture_name = ""

        # get player gesture selection
        if player.is_human:
            new_gesture_name = self.ui.display_game_screen()
        else:
            new_gesture_name = player.select_gesture()

        #pass gesture into player
        player.set_gesture(new_gesture_name)

        
    # Check to see who won the round
    def get_round_winner(self, player1_gesture, player2_gesture):
        # If both gestures are the same, nobody wins
        # Otherwise either player1 or player2 won (not both)
        p1_won = player1_gesture.check_against_opponent(player2_gesture)
        p2_won = player2_gesture.check_against_opponent(player1_gesture)


        if p1_won:
            self.player1.win_round()
            return "Player 1"
        elif p2_won:
            self.player2.win_round()
            return "Player 2"
        else:
            return None

    # Check if someone has won the entire game
    def check_for_game_winner(self):
        # Wins stored on each player as a count
        player1_wins = self.player1.get_wins()
        player2_wins = self.player2.get_wins()

        # If either player has 2 or more wins, then they have won best of 3
        if player1_wins >= 2:
            self.winner = self.player1
            self.winner_name = "Player 1"
        elif player2_wins >= 2:
            self.winner = self.player2
            self.winner_name = "Player 2"