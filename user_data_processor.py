from mfrc522_client import RfidReader
from firebase_client import FirebaseClient


class UserDataProcessor:
    def __init__(self):
        self.rfid: RfidReader = RfidReader()
        self.firebase_client = FirebaseClient()
        self.required_keys = [
            'Name',
            'e-mail',
            'Phone number',
            'tagID',
            'userStatus',
        ]
        self.user_data = {}

    def enroll_user(self) -> None:
        for key in self.required_keys:
            self._prompt_user_data_entry(key)

        print("Scan RFID tag")
        self.rfid.scan_and_set_rfid_tag_id()
        self.user_data['tagID'] = self.rfid.get_rfid_tag_id()
        self.user_data['userStatus'] = 'active'  # Default value on enrollment
        print("RFID tag scanned")

    def _prompt_user_data_entry(self, key: str) -> None:
        if key not in ['tagID', 'userStatus']:
            self.user_data[key] = input(f"Enter {key}: ")

    def _is_user_data_populated(self) -> bool:
        """Ensures all required keys are populated by
        checking for any missing keys.

        Raises:
            ValueError: If any required keys are missing from the user data

        Returns:
            bool: True if there are missing keys,
                and False if all required keys are present.
        """
        missing_keys: list[str] = [
            key for key in self.required_keys if key not in self.user_data
        ]
        if missing_keys:
            raise ValueError(
                f"Missing required keys: {', '.join(missing_keys)}")
        return True

    def _input_missing_keys(self, missing_keys: list[str]) -> None:
        while missing_keys:
            for key in missing_keys:
                self.user_data[key] = input(f"Enter your {key}: ")
            missing_keys = [
                key for key in self.required_keys if key not in self.user_data
            ]

    def process_user_data(self):
        try:
            self._is_user_data_populated()
            print("All required keys are populated.")
            print("Scan RFID tag again")
            self.firebase_client._collection.set(self.user_data)
            self.rfid.write_to_rfid_tag_text(
                self.firebase_client._collection.id)
            print("User data is set and saved to database.")
        except ValueError as e:
            print(f"Validation failed: {e}")


if __name__ == "__main__":
    processor = UserDataProcessor()
    processor.process_user_data()
