import sys  # For sys.exit() method
from core.firebase_client import FirebaseClient
from core.mfrc522_client import RfidReader


class CLI_Menu:
    # List of method names to include in the menu options dictionary
    MENU_METHODS = ['_option1', '_option2', '_option3', '_exit_program']

    def __init__(self):
        """
        Initialize the CLI_Menu class with an empty dictionary to store
        menu options and call the _setup_menu method to create the menu options.

        - _setup_menu (method): Create a dictionary of menu options with the
            option number as the key and a tuple of the option description and
            method name as the value
        - _users_choice_from_input (str): The user's choice from the menu
            options
        - menu_options (dict): Dictionary to store menu options
            (key: option number, value: tuple of option description and
            method name)
        """
        self.menu_options = {}  # Dictionary to store menu options
        self._setup_menu()
        self._users_choice_from_input: str = None

    def _setup_menu(self) -> None:
        """ Create a dictionary of menu options with the option number as the
        key and a tuple of the option description and method name as the value.
        """
        for index, method_name in enumerate(self.MENU_METHODS, start=1):
            option_number: str = str(index)
            option_description: str = method_name[1:].replace("_", " ").title()
            self.menu_options[option_number] = (
                option_description, getattr(self, method_name))

    def _display_menu(self) -> None:
        print("")
        print("+==================+")
        print("| RFID TAG MANAGER |")
        print("+==================+")
        for key, value in self.menu_options.items():
            print(f"{key}. {value[0]}")

        print("")  # Print an empty line for spacing (better readability)

    def _option1(self) -> None:
        print("You chose Option 1")

    def _option2(self) -> None:
        print("You chose Option 2")

    def _option3(self) -> None:
        print("You chose Option 3")

    def _exit_program(self) -> None:
        print("Exiting...")
        sys.exit(0)

    def _prompt_invalid_input_not_a_digit(self) -> bool:
        """ Check if the user's input is a digit

        Returns:
            bool: True if input is not a digit (i.e. not a number)
        """
        return_value: bool = False
        if not self._users_choice_from_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            self._display_menu()
            return_value: bool = True

        return return_value  # True if input is not a digit

    def _prompt_invalid_input_not_in_menu_options(self) -> bool:
        """ Check if the user's input is not in the menu options dictionary

        Returns:
            bool: True if input is not in menu options dictionary
                (i.e. not a valid choice)
        """
        return_value: bool = False
        if self._users_choice_from_input not in self.menu_options:
            print(
                f"Invalid choice. Please enter a number between 1 and " +
                str(len(self.menu_options)) + " (inclusive).")
            self._display_menu()
            return_value: bool = True

        return return_value

    def _read_users_menu_choice(self) -> None:
        """ Prompt the user for input and checks if it is valid
        (i.e. a digit and in the menu options dictionary); otherwise,
        prompt the user again until a valid input is received.
        """
        is_loop_toggle_true: bool = True
        while is_loop_toggle_true:
            self._users_choice_from_input = input("Enter your choice: ")
            if self._prompt_invalid_input_not_a_digit():
                continue  # Skip the rest of the loop and prompt the user again
            elif self._prompt_invalid_input_not_in_menu_options():
                continue  # Skip the rest of the loop and prompt the user again
            else:
                is_loop_toggle_true = False

    def _process_choice(self) -> None:
        """ Process the user's choice and call the corresponding method
        from the menu_options dictionary if it exists. Otherwise, print
        an error message.

        Args:
            choice (str): The user's choice from the menu options
        """
        if self._users_choice_from_input in self.menu_options:
            self.menu_options[self._users_choice_from_input][1]()

    def run(self):
        """ Run the CLI menu program
        """
        while True:
            self._display_menu()
            self._read_users_menu_choice()
            self._process_choice()


if __name__ == "__main__":
    menu = CLI_Menu()
    menu.run()
