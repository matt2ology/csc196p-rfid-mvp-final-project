from mfrc522 import SimpleMFRC522  # RFID library for the MFRC522 module
import RPi.GPIO as GPIO  # GPIO library for the Raspberry Pi


class RfidReader:
    def __init__(self):
        GPIO.setwarnings(False)  # Disable GPIO warnings - optional
        self.reader = SimpleMFRC522()  # Allows reading and writing RFID tags
        self.rfid_tag_id: str = ""
        self.rfid_tag_text: str = ""

    def read_rfid_tag(self) -> tuple[str, str]:
        """ Read the RFID tag - return the tag's ID and text

        Returns:
            tuple[str, str]: A tuple containing the RFID tag's ID and text
        """
        id, text = self.reader.read()
        return id, text

    def read_rfid_tag_id(self) -> str:
        """Reads the RFID tag's ID number
        If the same element is found twice consecutively, return it

        Returns:
            str: The RFID tag's ID number
        """
        previous_tag_id: str = ""
        while True:
            current_tag_id = self.reader.read_id()
            if current_tag_id == previous_tag_id:
                print(f"Tag ID: {current_tag_id}")
                return current_tag_id

            previous_tag_id = current_tag_id

    def scan_and_set_rfid_tag_id(self) -> None:
        """Scans the RFID tag and sets the RFID tag's ID
        """
        self.rfid_tag_id = self.read_rfid_tag_id()

    def get_rfid_tag_id(self) -> str:
        """Returns the RFID tag's ID

        Returns:
            str: The RFID tag's ID
        """
        return self.rfid_tag_id

    def read_rfid_tag_text(self) -> str:
        """Reads the RFID tag's text

        Returns:
            str: The RFID tag's text
        """
        previous_tag_id: str = ""
        while True:
            current_tag_id = self.reader.read_id()
            if current_tag_id == previous_tag_id:
                print(f"Tag ID: {current_tag_id}")
                return self.reader.read_no_block()[1]

            previous_tag_id = current_tag_id
            print("<", previous_tag_id, ", ", current_tag_id, ">")

    def write_to_rfid_tag_text(self, data: str) -> None:
        """Write data to the RFID tag's text field - 48 characters max

        Args:
            data (str): Data to be written to the RFID tag (48 characters max)
        """
        previous_tag_id: str = ""
        while True:
            current_tag_id = self.reader.read_id()
            if current_tag_id == previous_tag_id:
                print(f"Tag ID: {current_tag_id}")
                break  # break out of the loop if the same tag is found

            previous_tag_id = current_tag_id

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
