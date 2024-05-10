from mfrc522_client import RfidReader

class UserDataProcessor:
    def __init__(self):
        self.rfid: RfidReader = RfidReader()
        self.required_keys = [
            'name',
            'email',
            'phoneNumber',
            'tagID'
            'userStatus',
        ]
        self.user_data = {}

    def enroll_user(self) -> None:
        for key in self.required_keys:
            self._prompt_user_data_entry(key)

        self.user_data['userStatus'] = 'active'  # Default value for userStatus
        print("Scan RFID tag for tagID: ")
        self.user_data['tagID'] = input(self.rfid.read_rfid_tag_id())


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
            raise ValueError(f"Missing required keys: {', '.join(missing_keys)}")
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
            self._is_user_data_validated()
            print("All required keys are populated.")
        except ValueError as e:
            print(f"Validation failed: {e}")

if __name__ == "__main__":
    processor = UserDataProcessor()
    processor.process_user_data()
