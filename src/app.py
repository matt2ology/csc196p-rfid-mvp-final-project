import sys


def launch_gui():
    """Import and launch your GUI module"""
    # import gui.gui # Import gui module from gui package in src directory
    # gui.gui.main() # Call main function in gui module to start the GUI


def launch_cli():
    """Import and launch your CLI module
    """
    from cli.cli import CLI_Menu
    CLI_Menu().run()


def main():
    """Check command-line arguments or user input to
    determine the interface to launch
    """
    print("Launching...")
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        launch_cli()
    else:
        launch_gui()


if __name__ == "__main__":
    main()
