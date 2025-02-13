import firebase_admin
from firebase_admin import credentials, firestore

print("⏳ Startar Firebase...")

# Ladda Firebase credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Anslut till Firestore
db = firestore.client()

print("Firebase-anslutning lyckades!")
