###        IMPORTS
### ================================
from time import sleep

# User Interface class: Handles all interactions with terminal and user
class User_Interface:
    ###        INIT METHODS
    ### ======================================================================
    def __init__(self, menu_width=80, options_width=64, border_thickness=3):
        # Basic definitions
        self.border_character = '*'
        self.separator = '||'
        self.menu_width = menu_width
        self.options_width = options_width
        self.border_thickness = border_thickness

        self.build_custom_strings()

    def build_custom_strings(self):
        # Custom widths
        self.main_between_border_space = self.menu_width - (2 * self.border_thickness)
        self.secondary_between_border_space = self.options_width - (2 * self.border_thickness)
        self.left_cell_width = (self.main_between_border_space - len(self.separator)) // 2
        self.right_cell_width = self.main_between_border_space - len(self.separator) - self.left_cell_width

        # Creating custom string blocks
        self.main_pad = '\t\t'
        self.secondary_pad = '\t\t\t'
        self.end = '\n'
        self.left_main_border = f'{self.main_pad}{self.border_character * self.border_thickness}'
        self.right_main_border = f'{self.border_character * self.border_thickness}{self.end}'
        self.left_secondary_border = f'{self.secondary_pad}{self.border_character * self.border_thickness}'
        self.right_secondary_border = self.right_main_border
        self.main_full_bar = f'{self.main_pad}{self.border_character * self.menu_width}{self.end}'
        self.main_empty_bar = f'{self.left_main_border}{" " * self.main_between_border_space}{self.right_main_border}'
        self.secondary_full_bar = f'{self.secondary_pad}{self.border_character * self.options_width}{self.end}'
        self.secondary_empty_bar = f'{self.left_secondary_border}{" " * self.options_width}{self.right_secondary_border}'

    ###        DISPLAY METHODS
    ### ======================================================================
    def display_welcome(self, game_name):
        self.refresh()
        welcome_screen = self.get_welcome_screen(game_name)
        welcome_options = self.get_welcome_options()
        print(welcome_screen)
        user_selection = self.verify_inputs(welcome_options, ['1', '2'])

        if user_selection == '2':
            self.refresh()
            self.display_rules(game_name)

        return user_selection

    def display_player_number_prompt(self):
        player_options = self.get_player_number_options()
        user_selection = self.verify_inputs(player_options, ['1', '2'])
        return user_selection

    def get_player_number_options(self):
        player_number_options = f'{self.main_full_bar}'
        player_number_options += f'{self.main_empty_bar}'
        player_number_options += f'{self.main_full_bar}'
        player_number_options += f'{self.left_main_border}{self.center_value_in_space("HOW MANY PEOPLE ARE PLAYING?", self.main_between_border_space)}{self.right_main_border}'
        player_number_options += f'{self.left_main_border}{self.center_value_in_space("1 OR 2", self.main_between_border_space)}{self.right_main_border}'
        player_number_options += f'{self.main_empty_bar}'
        player_number_options += f'{self.main_full_bar}'

        return player_number_options

    def display_rules(self, game_name):
        formatted_rules = self.get_rules(["Rock crushes Scissors", 
            "Scissors cuts Paper", 
            "Paper covers Rock", 
            "Rock crushes Lizard", 
            "Lizard poisons Spock", 
            "Spock smashes Scissors", 
            "Scissors decapitates Lizard", 
            "Lizard eats Paper", 
            "Paper disproves Spock", 
            "Spock vaporizes Rock",
            "",
            "Press enter when you're done"])
        input(formatted_rules)

        self.display_welcome(game_name)

    def display_game_screen(self):
        # Display options
        option_string = "Please select an option: \n\n"
        option_string += '''    1. Rock
    2. Paper
    3. Scissors
    4. Lizard
    5. Spock'''

        # Format game screen and options menu
        game_screen = self.get_game_screen()

        # Display the screen and get user input back
        #print(game_screen)
        user_options = ['1', '2', '3', '4', '5']
        options_values = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        user_selection = self.verify_inputs(game_screen, user_options)
        selected_value = options_values[int(user_selection) - 1]
        return selected_value

    def display_winner(self, winner):
        winner_screen = self.get_winner_screen(winner)
        print(winner_screen)
        return 0

    def display_results(self, player1_gesture, player2_gesture, winner):
        message = f'{self.secondary_full_bar}'
        message += f'{self.left_secondary_border}{self.center_value_in_space(f"Player 1 chose {player1_gesture}.", self.secondary_between_border_space)}{self.right_secondary_border}'
        message += f'{self.left_secondary_border}{self.center_value_in_space(f"Player 2 chose {player2_gesture}.", self.secondary_between_border_space)}{self.right_secondary_border}'
        if winner:
            message += f'{self.left_secondary_border}{self.center_value_in_space(f"{winner} wins the round!", self.secondary_between_border_space)}{self.right_secondary_border}'
        else:
            message += f'{self.left_secondary_border}{self.center_value_in_space("Draw!", self.secondary_between_border_space)}{self.right_secondary_border}'
        message += f'{self.secondary_full_bar}'
        print(message)
        sleep(1)

    def display_restart(self):
        restart_screen = self.get_restart_screen()
        user_selection = self.verify_inputs(restart_screen, ['y', 'n'])
        return user_selection

    def display_exit(self):
        exit_screen = self.get_exit_screen()
        print(exit_screen)

    def refresh(self):
        print(f'{self.end * 100}')

    ###        STRING FORMATTING METHODS
    ### =======================================================================
    def get_welcome_screen(self, game_name):
        # Top of welcome screen w/ 2 empty lines before game name
        welcome_screen = f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'

        # Add each part of the game name on a new line
        for part in game_name:
            line_content = self.center_value_in_space(part, self.main_between_border_space)
            welcome_screen += f'{self.left_main_border}{line_content}{self.right_main_border}'

        # Two empty lines followed by two full width bars of the border character
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_empty_bar}'
        welcome_screen += f'{self.main_full_bar}'
        welcome_screen += f'{self.main_full_bar}'

        return welcome_screen

    def get_welcome_options(self):
        # Top of options, single full bar + title line
        welcome_options = f'{self.secondary_full_bar}'
        welcome_options += f'{self.left_secondary_border}{self.center_value_in_space("ARE YOU READY TO BEGIN?", self.secondary_between_border_space)}{self.right_secondary_border}'
        
        # Options
        welcome_options += f'{self.left_secondary_border}{self.center_value_in_space("1. START GAME", self.secondary_between_border_space)}{self.right_secondary_border}'
        welcome_options += f'{self.left_secondary_border}{self.center_value_in_space("2. SHOW RULES", self.secondary_between_border_space)}{self.right_secondary_border}'

        # Bottom of options, single full bar and push input area over
        welcome_options += f'{self.secondary_full_bar}'
        welcome_options += f'{self.end}{self.end}{self.secondary_pad}'

        return welcome_options

    def get_rules(self, rules):
        # Top of rules screen w/ 1 empty line
        rules_screen = f'{self.main_full_bar}'
        rules_screen += f'{self.left_main_border}{self.center_value_in_space("RPSLS - RULES", self.main_between_border_space)}{self.right_main_border}'
        rules_screen += f'{self.main_full_bar}'
        rules_screen += f'{self.main_empty_bar}'

        # Add each rule on a new line
        for rule in rules:
            line_content = self.center_value_in_space(rule, self.main_between_border_space)
            rules_screen += f'{self.left_main_border}{line_content}{self.right_main_border}'

        # One empty line followed by two full width bars of the border character
        rules_screen += f'{self.main_empty_bar}'
        rules_screen += f'{self.main_full_bar}'
        rules_screen += f'{self.main_full_bar}'

        return rules_screen

        
    def get_game_screen(self):
        # Get the content for the title row
        title_row_width = self.menu_width - (2 * self.border_thickness)
        title_row = self.center_value_in_space("RPSLS", title_row_width)

        # Title bar - Title row between two full bars
        game_screen = f'{self.main_full_bar}'
        game_screen += f'{self.left_main_border}{title_row}{self.right_main_border}'
        game_screen += f'{self.main_full_bar}'

        
        user_options = ['1', '2', '3', '4', '5']
        options_values = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        for i in range(5):
            current_line = f'{self.left_main_border}{self.center_value_in_space(f"{user_options[i]}. {options_values[i]}", self.main_between_border_space)}{self.right_main_border}'
            game_screen += current_line
        
        game_screen += f'{self.main_empty_bar}'
        game_screen += f'{self.main_full_bar}'
        game_screen += f'{self.main_full_bar}'

        return game_screen

    def get_game_options(self, option_name, options):
        # Top of options, single full bar + title line
        game_options = f'{self.secondary_full_bar}'
        game_options += f'{self.left_secondary_border}{self.center_value_in_space(option_name, self.secondary_between_border_space)}{self.right_secondary_border}'

        # Format and add options
        for i in range(len(options)):
            option = options[i]
            current_line = f'{self.left_secondary_border}{self.center_value_in_space(option, self.secondary_between_border_space)}{self.right_secondary_border}'
            game_options += current_line

        # Bottom of options, single full bar and push input area over
        game_options += f'{self.secondary_full_bar}'
        game_options += f'{self.end}{self.end}{self.secondary_pad}'

        return game_options

    def get_winner_screen(self, winner):
        # Top of screen
        winner_screen = f'{self.main_full_bar}'
        winner_screen += f'{self.main_empty_bar}'
        winner_screen += f'{self.left_main_border}{self.center_value_in_space(f"{winner} WINS THE GAME!!!", self.main_between_border_space)}{self.right_main_border}'
        winner_screen += f'{self.main_empty_bar}'
        winner_screen += f'{self.main_full_bar}'

        return winner_screen

    def get_restart_screen(self):
        # Top of screen, full bar + empty bar
        restart_screen = f'{self.main_full_bar}'
        restart_screen += f'{self.main_empty_bar}'

        # Middle of screen, format message into empty lines
        restart_message = ['WOULD YOU', 'LIKE TO', 'PLAY AGAIN?', 'Y/N']
        for part in restart_message:
            current_line = f'{self.left_main_border}{self.center_value_in_space(part, self.main_between_border_space)}{self.right_main_border}'
            restart_screen += current_line

        # Bottom of screen, empty bar + full bar
        restart_screen += f'{self.main_empty_bar}'
        restart_screen += f'{self.main_full_bar}'

        return restart_screen

    def get_exit_screen(self):
        # Top of screen, full bar + empty bar
        exit_screen = f'{self.main_full_bar}'
        exit_screen += f'{self.main_empty_bar}'

        # Middle of screen, format message into empty lines
        exit_message = ['THANKS', 'FOR', 'PLAYING!']
        for part in exit_message:
            current_line = f'{self.left_main_border}{self.center_value_in_space(part, self.main_between_border_space)}{self.right_main_border}'
            exit_screen += current_line

        # Bottom of screen, empty bar + full bar
        exit_screen += f'{self.main_empty_bar}'
        exit_screen += f'{self.main_full_bar}'

        return exit_screen

    def get_option_values(self, data):
        options = []
        # Using numeric selection values, used for list indices after verification
        selections = [f'{i+1}' for i in range(len(data))]

        # Add each option to the list
        for i in range(len(data)):
            current_option = f'{i + 1}: {data[i].name}'
            options.append(current_option)

        return (selections, options)

    ###        AUXILIARY METHODS
    ### ======================================================================
    def format_cell_data(self, left_data, right_data):
        max_data_length = max(len(left_data), len(right_data)) # Make sure to account for different lengths of data
        left_data_length = len(left_data)
        right_data_length = len(right_data)

        left_formatted = []
        right_formatted = []

        for i in range(max_data_length):
            # Avoid going out of range
            left_current_data = ''
            right_current_data = ''
            if i < left_data_length:
                left_current_data = left_data[i]
            if i < right_data_length:
                right_current_data = right_data[i]

            # Left cell formatting
            if left_current_data:
                # Format data if there is some
                left_formatted.append(self.center_value_in_space(f'NAME: {left_current_data.name}', self.left_cell_width))
                status_line = f'   HEALTH: {left_current_data.get_health()}   POWER: {left_current_data.get_resource()}'
                left_formatted.append(f'{status_line}{" " * (self.left_cell_width - len(status_line))}')
            else:
                # Fill with empty lines
                left_formatted.append(" " * self.left_cell_width)
                left_formatted.append(" " * self.left_cell_width)

            # Right cell formatting
            if right_current_data:
                # Format data if there is some
                right_formatted.append(self.center_value_in_space(f'NAME: {right_current_data.name}', self.right_cell_width))
                status_line = f'   HEALTH: {right_current_data.get_health()}   ENERGY: {right_current_data.get_resource()}'
                right_formatted.append(f'{status_line}{" " * (self.right_cell_width - len(status_line))}')
            else:
                # Fill with empty lines
                right_formatted.append(" " * self.right_cell_width)
                right_formatted.append(" " * self.right_cell_width)

        return (left_formatted, right_formatted)

    def verify_inputs(self, message, options):
        # Take in array of valid options and reprompt the user until a valid option is selected
        valid_selection = False
        user_input = ""

        while not valid_selection:
            user_input = input(message).lower()
            if user_input in options:
                valid_selection = True

        return user_input

    def center_value_in_space(self, value, total_width):
        # Format value to be centered in line
        left_pad = (total_width - len(value)) // 2
        right_pad = total_width - left_pad - len(value)
        return f'{" " * left_pad}{value}{" " * right_pad}'

    ###        TESTING
    ### ======================================================================
    def tests(self):
        print("Testing internal variables")
        print(self.left_main_border)
        print(self.left_secondary_border)
        print(self.right_main_border)
        print(self.right_secondary_border)
        print(self.main_full_bar)
        print(self.main_empty_bar)

        self.display_welcome(['WELCOME TO', 'ROBOTS', 'VS.', 'DINOSAURS'])

# test = User_Interface()
# test.tests()