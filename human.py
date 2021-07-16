from player import Player

class Human(Player):

    def select_gesture(self):
        # Display options
        option_string = "Please select an option: \n\n"
        user_options = []
        for i in range(len(self.gestures)):
            option_string += f"{i + 1}: {self.gestures[i]}\n"
            user_options.append(f"{i+1}")
        # Get user selection
        selection_invalid = True

        # Validate user selection
        while selection_invalid:
            user_selection = input(option_string)
            if user_selection in user_options:
                selection_invalid = False
        # Set new choice
        new_gesture = self.gestures[int(user_selection) - 1]
        self.set_gesture(new_gesture)