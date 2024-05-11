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

    def update_name(self, tag_id: str, new_name: str) -> None:
        """Allows user to update value from the required keys-values
        on file and have it updated in database
        SEE TO:
            - [Python - Handle Data in Firestore Database](https://www.youtube.com/watch?v=-jWD-vIyirw&ab_channel=BytesOfCode)
        """
        # Query Firestore for documents with the given tagID
        docs_ref = self._database.collection(
            u'your_collection').where(u'tagID', u'==', tag_id).limit(1)
        docs = docs_ref.stream()

        # Update the 'Name' field of the first matching document
        for doc in docs:
            doc_ref = self._database.collection(
                u'authorized_personnel').document(doc.id)
            doc_ref.update({u'Name': new_name})  # the 'u' allows for unicode
            print(f"Document with tagID '{tag_id}' updated successfully.")

    def delete_user_based_on_tag_id(self, tag_id: str) -> None:
        """Allows user to delete a document from the database
        SEE TO:
            - [Python - Handle Data in Firestore Database](https://www.youtube.com/watch?v=-jWD-vIyirw&ab_channel=BytesOfCode)
        """
        # Query Firestore for documents with the given tagID
        docs_ref = self._database.collection(
            u'authorized_personnel').where(u'tagID', u'==', tag_id).limit(1)
        docs = docs_ref.stream()

        # Delete the first matching document
        for doc in docs:
            doc_ref = self._database.collection(
                u'authorized_personnel').document(doc.id)
            doc_ref.delete()
            print(f"Document with tagID '{tag_id}' deleted successfully.")


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
