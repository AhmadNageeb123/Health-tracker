import firebase_admin
from firebase_admin import credentials, firestore
import tkinter as tk


print("⏳ Startar Firebase...")




# Ladda Firebase credentials
if not firebase_admin:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://your-database-name.firebaseio.com/'})

# Anslut till Firestore
    db = firestore.client()

print("Firebase-anslutning lyckades!")
