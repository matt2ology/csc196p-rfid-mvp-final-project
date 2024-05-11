import sys


def launch_gui():
    """Import and launch your GUI module"""
    # import gui.gui # Import gui module from gui package in src directory
    # gui.gui.main() # Call main function in gui module to start the GUI


def launch_cli():
    """Import and launch your CLI module
    """
    from cli import CLI_Menu
    while True:
        CLI_Menu().run()  # Call the run method on the instance


def main():
    """Check command-line arguments or user input to
    determine the interface to launch
    """
    print("Launching...")

    # TODO: Add GUI
    # if len(sys.argv) > 1 and sys.argv[1] == "--cli":
    #     launch_cli()
    # else:
    #     launch_gui()
    launch_cli()

if __name__ == "__main__":
    main()
