import requests
from app.config import settings

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Api-Token": settings.API_KEY
}

def get_contacts():
    response = requests.get(f"{settings.API_URL}/contacts", headers=headers)
    return response.json()

def create_contact(email, first_name, last_name):
    payload = {
        "contact": {
            "email": email,
            "firstName": first_name,
            "lastName": last_name
        }
    }
    response = requests.post(f"{settings.API_URL}/contacts", json=payload, headers=headers)
    return response.json()
    