import json
import os


ATTENDANCE_FILE = "data/attendance.json"


def load_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return []

    with open(ATTENDANCE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_attendance(records):
    os.makedirs("data", exist_ok=True)

    with open(ATTENDANCE_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


def mark_attendance(student_id, date, subject, status):
    records = load_attendance()

    record = {
        "student_id": student_id,
        "date": date,
        "subject": subject,
        "status": status
    }

    records.append(record)

    save_attendance(records)

    return {
        "success": True,
        "message": "Attendance marked successfully.",
        "record": record
    }


def get_attendance(student_id):
    records = load_attendance()

    student_records = [
        record
        for record in records
        if record["student_id"] == student_id
    ]

    return student_records