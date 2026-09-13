import json

DATA_FILE = 'patient_data.json'


def load_patients():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_patients(patients):
    with open(DATA_FILE, 'w') as f:
        json.dump(patients, f, indent=2)


def add_patients():
    patients = load_patients()
    patient_num = int(input('Enter Patient S.no: '))
    for patient in patients:
        if patient['Serial_Num'] == patient_num:
            print('Patient Already Existed!')
            return

    new_patient = {
        'Serial_Num': patient_num,
        'Patient_Name': input('Enter Patient Name: '),
        'Patient_ID': input('Enter Patient ID: '),
        'Heart_Rate_BPM': int(input('Enter Patient HR: ')),
        'High_BP_Systolic': int(input('Enter Patient Systolic Pressure: ')),
        'Low_BP_Diastolic': int(input('Enter Patient Diastolic Pressure: ')),
    }
    patients.append(new_patient)
    save_patients(patients)
    print('Patient Added Successfully!')


def show_all_patients():
    patients = load_patients()
    if not patients:
        print('No Patients Found!')
        return
    for patient in patients:
        print(
            f"Patient_Num: {patient['Serial_Num']}, "
            f"Name: {patient['Patient_Name']}, "
            f"ID: {patient['Patient_ID']}, "
            f"HR: {patient['Heart_Rate_BPM']}, "
            f"BP: {patient['High_BP_Systolic']}/{patient['Low_BP_Diastolic']}"
        )


def search_patients():
    patients = load_patients()
    patient_num = int(input('Enter Patient S.no: '))
    for patient in patients:
        if patient['Serial_Num'] == patient_num:
            print(
                f"Patient_Num: {patient['Serial_Num']}, "
                f"Name: {patient['Patient_Name']}, "
                f"ID: {patient['Patient_ID']}, "
                f"HR: {patient['Heart_Rate_BPM']}, "
                f"BP: {patient['High_BP_Systolic']}/{patient['Low_BP_Diastolic']}"
            )
            return
    print('Patient Not Found!')


def edit_patients():
    patients = load_patients()
    patient_num = int(input('Enter Patient S.no: '))
    for patient in patients:
        if patient['Serial_Num'] == patient_num:
            patient['Patient_Name'] = input("Enter Patient's new Name: ")
            patient['Patient_ID'] = input("Enter Patient's new ID: ")
            patient['Heart_Rate_BPM'] = int(input("Enter Patient's new HR: "))
            patient['High_BP_Systolic'] = int(input("Enter Patient's new Systole: "))
            patient['Low_BP_Diastolic'] = int(input("Enter Patient's new Diastole: "))
            save_patients(patients)
            print("Patient's Data Updated Successfully!")
            return
    print('Patient Not Found!')


def remove_patients():
    patients = load_patients()
    patient_num = int(input('Enter Patient S.no: '))
    for i, patient in enumerate(patients):
        if patient['Serial_Num'] == patient_num:
            del patients[i]
            save_patients(patients)
            print('Patient Removed Successfully!')
            return
    print('Patient Not Found!')


def hr_report():
    patients = load_patients()
    high_hr = [f"{p['Patient_Name']}: {p['Heart_Rate_BPM']} bpm" for p in patients if p['Heart_Rate_BPM'] > 79]
    low_hr = [f"{p['Patient_Name']}: {p['Heart_Rate_BPM']} bpm" for p in patients if p['Heart_Rate_BPM'] < 75]

    print(f'High HR Patients: {len(high_hr)}')
    for entry in high_hr:
        print(entry)

    print(f'Low HR Patients: {len(low_hr)}')
    for entry in low_hr:
        print(entry)


def bp_report():
    patients = load_patients()
    high_bp = []
    low_bp = []
    for patient in patients:
        if patient['High_BP_Systolic'] > 120:
            high_bp.append(f"{patient['Patient_Name']} has high systole: {patient['High_BP_Systolic']} mmHg")
        elif 100 < patient['High_BP_Systolic'] < 120:
            high_bp.append(f"{patient['Patient_Name']} has low systole: {patient['High_BP_Systolic']} mmHg")
        if patient['Low_BP_Diastolic'] < 80:
            low_bp.append(f"{patient['Patient_Name']} has low diastole: {patient['Low_BP_Diastolic']} mmHg")
        elif 80 < patient['Low_BP_Diastolic'] <= 100:
            low_bp.append(f"{patient['Patient_Name']} has high diastole: {patient['Low_BP_Diastolic']} mmHg")

    print(f'High BP Patients: {len(high_bp)}')
    for entry in high_bp:
        print(entry)

    print(f'Low BP Patients: {len(low_bp)}')
    for entry in low_bp:
        print(entry)


def main():
    while True:
        print('======== PATIENTS RECORD ========')
        print('1. Add Patients')
        print('2. Display Patients')
        print('3. Search Patients')
        print('4. Remove Patients')
        print('5. Edit Patients')
        print('6. HR Report')
        print('7. BP Report')
        print('8. Exit')

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_patients()
        elif choice == 2:
            show_all_patients()
        elif choice == 3:
            search_patients()
        elif choice == 4:
            remove_patients()
        elif choice == 5:
            edit_patients()
        elif choice == 6:
            hr_report()
        elif choice == 7:
            bp_report()
        elif choice == 8:
            print("Thanks for using service!")
            break
        else:
            print("Invalid Choice!")


if __name__ == '__main__':
    main()
