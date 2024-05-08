from .core.firebase_client import FirebaseClient

def main():
    firebase_client = FirebaseClient()  # Initialize FirebaseClient object

    print("Authorized Personnel:")
    for personnel in firebase_client.get_authorized_personnel():
        print(personnel)

    print("\nAdd Authorized Personnel:")
    personnel = {
        "name": "John Doe",
        "rfid_uid": "1020731053017",
        "role": "Admin",
    }

    firebase_client.add_authorized_personnel(personnel)
    print("Authorized personnel added.")

    print("\nAuthorized Personnel:")
    for personnel in firebase_client.get_authorized_personnel():
        print(personnel)


if __name__ == "__main__":
    main()