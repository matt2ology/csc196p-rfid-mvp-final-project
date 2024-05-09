import os


class Settings:
    def __init__(self):
        self._BASE_DIR_SRC = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        self.FIREBASE_ADMIN_SDK_KEY_FILE = os.path.normpath(
            "src/configuration/firebase_private_key.json"
        )  # Path to Firebase Admin SDK private key file (JSON)

    def get_base_dir_src(self):
        return self._BASE_DIR_SRC

    def get_firebase_admin_sdk_key_file(self):
        return self.FIREBASE_ADMIN_SDK_KEY_FILE

    def set_base_dir_src(self, base_dir_src):
        self._BASE_DIR_SRC = base_dir_src

    def set_firebase_admin_sdk_key_file(self, firebase_admin_sdk_key_file):
        self.FIREBASE_ADMIN_SDK_KEY_FILE = firebase_admin_sdk_key_file

    def __str__(self):
        return f"Settings: {self._BASE_DIR_SRC}, {self.FIREBASE_ADMIN_SDK_KEY_FILE}"

    def __repr__(self):
        return f"Settings: {self._BASE_DIR_SRC}, {self.FIREBASE_ADMIN_SDK_KEY_FILE}"

# The root directory of the project
# _BASE_DIR_SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# FIREBASE_ADMIN_SDK_KEY_FILE = os.path.normpath(
    # "src/config/firebase_private_key.json"
# )  # Path to Firebase Admin SDK private key file (JSON)
