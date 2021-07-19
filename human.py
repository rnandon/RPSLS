###        IMPORTS
### ========================
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.is_human = True

    # Distinct implementation, prompts user for input
    def select_gesture(self):
        

        # Get and validate user selection
        selection_invalid = True
        while selection_invalid:
            user_selection = input(option_string)
            if user_selection in user_options:
                selection_invalid = False
                


        # Set new choice
        new_gesture = options_values[int(user_selection) - 1]
        self.set_gesture(new_gesture)