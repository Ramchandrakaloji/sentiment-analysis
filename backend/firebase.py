import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase/firebase_setup.json")  # Ensure this file is correct
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_to_firebase(review, sentiment, confidence):
    db.collection("classified_reviews").add({
        "review": review,
        "sentiment": sentiment,
        "confidence": confidence
    })
