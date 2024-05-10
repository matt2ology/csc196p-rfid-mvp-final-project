class MemberData:
    """MemberData class is a data class for data kept on members enrolled
    """
    def __init__(self):
        self.keys = ['name', 'status', 'email', 'phoneNumber', 'tagID']
        self.data = {key: '' for key in self.keys}


    def get_data_entry_form(self) -> dict:
        """Return the data entry form for personnel data

        Returns:
            dict: The data entry form for personnel data
        """
        return self.data_entry_form
    
    def _enroll_personnel(self) -> None:
        """Enroll personnel into the database using the RFID tag's ID and text
        """
        for key in self.keys:
            value = input(f"Enter {key}: ")
            while not value:  # Check if value is empty
                print(f"{key} cannot be empty.")
                value = input(f"Enter {key}: ")
            self.personnel_data.data[key] = value
    
    def set_data_entry_form(self, data: dict) -> None:
        """Set the data entry form for personnel data

        Args:
            data (dict): The data entry form for personnel data
        """
        self.data_entry_form = data

    def get_name(self) -> str:
        """Return the name of the personnel

        Returns:
            str: The name of the personnel
        """
        return self.data_entry_form['name']

    def set_name(self, name: str) -> None:
        """Set the name of the personnel

        Args:
            name (str): The name of the personnel
        """
        self.data_entry_form['name'] = name

    def get_status(self) -> str:
        """Return the status of the personnel

        Returns:
            str: The status of the personnel
        """
        return self.data_entry_form['status']
    
    def set_status(self, status: str) -> None:
        """Set the status of the personnel

        Args:
            status (str): The status of the personnel
        """
        self.data_entry_form['status'] = status

