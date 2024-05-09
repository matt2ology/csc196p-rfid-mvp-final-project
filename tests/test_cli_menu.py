import pytest

from src.cli.cli import CLI_Menu


class Test_CLI_Menu:
    @pytest.fixture
    def cli_menu(self):
        """ Create an instance of the CLI_Menu class before each test function

        Returns:
            CLI_Menu: An instance of the CLI_Menu class
        """
        return CLI_Menu()

    @pytest.mark.parametrize(
        "invalid_input",
        ["!", "~", "\"", "DEL", "#", "Ç", "$", "ü", "%", "é", "&", "â", "\'",
         "ä", "(", "à", ")", "å", "*", "ç", "+", "ê", ",", "ë", "-", "è", ".",
         "ï", "/", "î", ":", "ì", ";", "Ä", "<", "Å", "=", "É", ">", "æ", "?",
         "Æ", "@", "ô", "[", "ö", "\\", "ò", "]", "û", "^", "ù", "_", "ÿ", "`",
         "Ö", "{", "Ü", "|", "¢", "}", "£", "🔥", "😎"]
    )
    def test_prompt_invalid_input_not_a_digit(
            self, cli_menu: CLI_Menu, invalid_input: str):
        """ Test if the user's input is not a digit (i.e. a letter, or a symbol)
        Args:
            cli_menu (CLI_Menu): An instance of the CLI_Menu class
            invalid_input (str): Invalid input to be tested
        """
        cli_menu._users_choice_from_input = invalid_input
        assert cli_menu._prompt_invalid_input_not_a_digit() == True

    def test_prompt_invalid_input_not_in_menu_options(self, cli_menu: CLI_Menu):
        """ Test if the user's input is not in the menu options dictionary

        Args:
            cli_menu (CLI_Menu): An instance of the CLI_Menu class
        """
        invalid_input: str = str(len(cli_menu._menu_options) + 1)
        cli_menu._users_choice_from_input = invalid_input
        assert cli_menu._prompt_invalid_input_not_in_menu_options() == True
