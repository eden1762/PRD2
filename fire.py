import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_user(user_data):
    doc_ref = db.collection("users").document(user_data["line_id"])
    doc_ref.set(user_data)

def get_user_by_line_id(line_id):
    doc = db.collection("users").document(line_id).get()
    return doc.to_dict() if doc.exists else None

def save_message(line_id, text, reply):
    db.collection("messages").add({
        "line_id": line_id,
        "text": text,
        "reply": reply
    })
