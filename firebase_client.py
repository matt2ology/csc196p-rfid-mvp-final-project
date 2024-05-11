from firebase_admin import credentials  # Firebase Admin SDK credentials
from firebase_admin import firestore  # Firebase's Firestore database client
# UserWarning: Detected filter using positional arguments. Prefer using the 'filter' keyword argument instead.
from google.cloud.firestore_v1.base_query import FieldFilter
import firebase_admin  # Firebase Admin SDK for Python


from config import Settings  # Used for getting the Firebase Admin SDK key file


class FirebaseClient:
    """Handles Firebase Firestore database operations for authorized personnel 
    """

    def __init__(self) -> None:
        """
        Initialize Firestore database client and get collection reference for
        authorized personnel in Firestore database
        - _database (firestore.Client): Firestore database client instance
        - _collection (firestore.CollectionReference): Collection reference for
             authorized personnel in Firestore database
        """
        self._initialize_firestore_with_credentials()
        self._database: firestore.Client = firestore.client()
        # Get collection reference, so that each document will have a unique ID
        self._collection: firestore.CollectionReference = self._database.\
            collection("authorized_personnel").document()

    def _initialize_firestore_with_credentials(self) -> None:
        """
        Initialize Firebase app with credentials from,
        a Google service account certificate, JSON file: Firebase Admin SDK key
        """
        try:
            firebase_admin.get_app()
        except ValueError:  # If Firebase app is not yet initialized
            firebase_admin.initialize_app(
                credentials.Certificate(
                    Settings().get_firebase_admin_sdk_key_file()
                )
            )

    def find_firestore_by_tag_id_and_print_data(self, id: str) -> None:
        """
        Find a document in Firestore by its tag ID and
        print the document data

        Args:
            document_id (str): The document ID to find in Firestore
        """
        query = self._database.collection("authorized_personnel").where(
            filter=FieldFilter("tagID", "in", [id])
        )
        documents = query.stream()
        for doc in documents:
            print("Document ID:", doc.id)
            print("Data:")
            data_dict = doc.to_dict()
            for key, value in data_dict.items():
                print(f"\t{key}: {value}")


if __name__ == "__main__":
    """Driver code to test the FirebaseClient class
    SEE TO: https://www.youtube.com/watch?v=qsFYq_1BQdk&ab_channel=BytesOfCode
    """
    firebase_client = FirebaseClient()
    data = {"name": "John Doe", "email": "test@email.com", "status": "active"}
    firebase_client._collection.set(data)
    # Get the document ID of the newly added document
    print(f"Document ID: {firebase_client._collection.id}")
    # Get the document data
    print(f"Document Data: {firebase_client._collection.get().to_dict()}")
    # Delete the document
    firebase_client._collection.delete()
    print("Document deleted")
