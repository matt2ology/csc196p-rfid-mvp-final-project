import pytest

from ..user_data_processor import UserDataProcessor


class Test_UserDataProcessor:
    @pytest.fixture
    def user(self):
        """ Create an instance of the Test_UserDataProcessor class before each test function

        Returns:
            Test_UserDataProcessor: An instance of the Test_UserDataProcessor
            class
        """
        return UserDataProcessor

    @pytest.mark.parametrize(
        [{"name": "John Doe",
          "status": "active",
          "email": "example.gmail.com",
          "phoneNumber": "1234567890",
          "tagID": "1234567890"
          }]
    )
    def test_is_user_data_validated(self, user: UserDataProcessor):
        """ Test if the data entry form for personnel data is returned

        Args:
            user (MemberData): An instance of the MemberData class
        """
        user.enroll_member("John Doe", "example.gmail.com", "1234567890", "1234567890")
        assert user.is_user_data_validated() is False