import json

AVAILABLE = {
    "Dra Ana": ["14:00", "16:00"],
    "Dr Carlos": ["10:00", "15:00"]
}


def get_slots(doctor):
    return AVAILABLE.get(doctor, [])


def schedule(doctor, slot):
    if slot in AVAILABLE.get(doctor, []):
        AVAILABLE[doctor].remove(slot)
        return True
    return False


def save_patient(data):
    with open("patients.json", "a") as f:
        f.write(json.dumps(data) + "\n")