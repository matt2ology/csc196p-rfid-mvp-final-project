import os

# The root directory of the project
_BASE_DIR_SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIREBASE_ADMIN_SDK_KEY_FILE = os.path.normpath(
        "src/config/firebase_private_key.json"
)  # Path to Firebase Admin SDK private key file (JSON)
