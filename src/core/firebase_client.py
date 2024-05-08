import firebase_admin  # Firebase Admin SDK for Python
from firebase_admin import credentials  # Firebase Admin SDK credentials
from firebase_admin import firestore  # Firebase's Firestore database client

from ..config import settings

class FirebaseClient:
    """Handles Firebase Firestore database operations for authorized personnel 
    """

    def __init__(self) -> None:
        try:
            firebase_admin.get_app()
        except ValueError:  # If Firebase app is not initialized yet
            firebase_admin.initialize_app(
                credentials.Certificate(
                    # Path to private key file
                    settings.FIREBASE_ADMIN_SDK_KEY_FILE
                )
            )  # Initialize Firebase app with credentials

        # Initialize Firestore database client
        self._database: firestore.Client = firestore.client()
        self._collection: firestore.CollectionReference = self._database.collection(
            "authorized_personnel"
        )

    def get_authorized_personnel(self) -> list:
        """
        Get all authorized personnel from Firestore database
        """
        personnel = self._collection.get()
        return [person.to_dict() for person in personnel]

    def add_authorized_personnel(self, personnel: dict) -> None:
        """
        Add authorized personnel to Firestore database
        """
        self._collection.add(personnel)

    def delete_authorized_personnel(self, personnel_id: str) -> None:
        """
        Delete authorized personnel from Firestore database
        """
        self._collection.document(personnel_id).delete()
