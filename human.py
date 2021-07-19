###        IMPORTS
### ========================
from player import Player

class Human(Player):
    # Gets init method from Player class

    # Distinct implementation, prompts user for input
    def select_gesture(self):
        # Display options
        option_string = "Please select an option: \n\n"
        user_options = ['1', '2', '3', '4', '5']
        options_values = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        option_string += '''    1. Rock
    2. Paper
    3. Scissors
    4. Lizard
    5. Spock'''

        # Get and validate user selection
        selection_invalid = True
        while selection_invalid:
            user_selection = input(option_string)
            if user_selection in user_options:
                selection_invalid = False
                


        # Set new choice
        new_gesture = options_values[int(user_selection) - 1]
        self.set_gesture(new_gesture)