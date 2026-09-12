# Patient Management System

A console-based Python application to manage patient health records — add,
search, edit, remove patients, and generate heart rate / blood pressure
reports. Data is stored persistently in a JSON file.

## Features
- Add / search / edit / remove patient records
- JSON-based storage (`patient_data.json`)
- Heart rate report (flags high/low HR patients)
- Blood pressure report (flags high/low systolic and diastolic readings)
- Simple menu-driven console interface

## Requirements
- Python 3.10+

## How to run
```bash
python patient_manager.py
```

## Menu options
1. Add Patients
2. Display Patients
3. Search Patients
4. Remove Patients
5. Edit Patients
6. HR Report
7. BP Report
8. Exit

## Data format
Each patient record is stored as a JSON object:
```json
{
  "Serial_Num": 101,
  "Patient_Name": "Aisha",
  "Patient_ID": "P001",
  "Heart_Rate_BPM": 85,
  "High_BP_Systolic": 125,
  "Low_BP_Diastolic": 78
}
```

## Notes
This project was built as part of a Python learning journey. Earlier versions
used raw text-file parsing; this version was refactored to use JSON for more
reliable data storage.