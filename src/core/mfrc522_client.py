from mfrc522 import SimpleMFRC522  # RFID library for the MFRC522 module
import RPi.GPIO as GPIO  # GPIO library for the Raspberry Pi


class RfidReader:
    def __init__(self):
        GPIO.setwarnings(False)  # Disable GPIO warnings - optional
        self.reader = SimpleMFRC522()  # Allows reading and writing RFID tags

    def read_rfid_tag(self) -> tuple[str, str]:
        """ Read the RFID tag - return the tag's ID and text

        Returns:
            tuple[str, str]: A tuple containing the RFID tag's ID and text
        """
        id, text = self.reader.read()
        return id, text

    def read_rfid_tag_id(self) -> str:
        """Reads the RFID tag's ID number

        Returns:
            str: The RFID tag's ID number
        """
        return self.reader.read_id()

    def read_rfid_tag_text(self) -> str:
        """Reads the RFID tag's text

        Returns:
            str: The RFID tag's text
        """
        return self.reader.read_no_block()[1]

    def write_to_rfid_tag_text(self, data: str) -> None:
        """Write data to the RFID tag's text field - 48 characters max

        Args:
            data (str): Data to be written to the RFID tag (48 characters max)
        """
        self.reader.write(data)


if __name__ == "__main__":
    """ Used for testing the RfidReader class 
    """
    try:
        RfidReader().write_to_rfid_tag_text(
            "I'll take a potato chip...and eat it!"
        )
        print(f"ID: {RfidReader().read_rfid_tag_id()}")
        print(f"Data only: {RfidReader().read_rfid_tag_text()}")
    except KeyboardInterrupt:
        GPIO.cleanup()  # Reset GPIO settings when user interrupts with Ctrl+C
        print("Exiting...")
