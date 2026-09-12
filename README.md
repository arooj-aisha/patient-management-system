# Patient Management System

A command-line Python application for managing patient health records —
add, search, edit, and remove patients, with automated heart rate and
blood pressure reporting. Data is stored persistently in JSON.

## Features

- **Add, search, edit, and remove** patient records
- **Persistent storage** using JSON (`patient_data.json`)
- **Heart rate report** — automatically flags patients with high or low BPM
- **Blood pressure report** — flags abnormal systolic/diastolic readings
- Simple, menu-driven console interface

## Tech Stack

- Python 3.10+
- Standard library only (`json`) — no external dependencies

## Getting Started

### Prerequisites
- Python 3.10 or higher installed

### Installation
```bash
git clone https://github.com/arooj-aisha/patient-management-system.git
cd patient-management-system
```

### Run
```bash
python patient_manager.py
```

## Usage

On launch, you'll see a menu:

```
======== PATIENTS RECORD ========
1. Add Patients
2. Display Patients
3. Search Patients
4. Remove Patients
5. Edit Patients
6. HR Report
7. BP Report
8. Exit
```

Enter the number corresponding to the action you want, and follow the prompts.

## Data Format

Each patient is stored as a JSON object in `patient_data.json`:

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

## Project Structure

```
patient-management-system/
├── patient_manager.py   # Main application logic
├── README.md            # Project documentation
└── .gitignore           # Excludes generated data files
```

## Roadmap / Future Improvements

- [ ] Input validation for non-numeric entries
- [ ] Export reports to CSV
- [ ] Search by patient name, not just serial number
- [ ] Unit tests

## Background

This project started as a text-file-based prototype and was refactored to
use JSON for more reliable, structured data storage — part of an ongoing
Python learning journey.

## License

This project is open source and available under the [MIT License](LICENSE).