# Initialize an empty list to store patient records
patient_records = []

# Function to add a new patient record
def add_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    record = {"ID": patient_id, "Name": name, "Age": age, "Gender": gender}
    patient_records.append(record)
    print("Patient record added successfully!")

# Function to display all patient records
def display_patients():
    if not patient_records:
        print("No patient records found.")
    else:
        print("Patient Records:")
        for record in patient_records:
            print(f"ID: {record['ID']}, Name: {record['Name']}, Age: {record['Age']}, Gender: {record['Gender']}")

# Function to search for a patient by ID
def search_patient_by_id(patient_id):
    for record in patient_records:
        if record["ID"] == patient_id:
            return record
    return None

# Function to delete a patient by ID
def delete_patient_by_id(patient_id):
    for record in patient_records:
        if record["ID"] == patient_id:
            patient_records.remove(record)
            print(f"Patient with ID {patient_id} has been deleted.")
            return
    print(f"Patient with ID {patient_id} not found.")

# Function to update a patient record by ID
def update_patient_by_id(patient_id):
    record = search_patient_by_id(patient_id)
    if record:
        print("Patient Found. Please update the following information:")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        record["Name"] = name
        record["Age"] = age
        record["Gender"] = gender
        print("Patient record updated successfully!")
    else:
        print(f"Patient with ID {patient_id} not found.")

# Main program loop
while True:
    print("\nHospital Management System Menu:")
    print("1. Add a new patient")
    print("2. Display all patients")
    print("3. Search for a patient by ID")
    print("4. Delete a patient by ID")
    print("5. Update a patient's details by ID")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        patient_id = input("Enter patient ID to search: ")
        patient = search_patient_by_id(patient_id)
        if patient:
            print(f"Patient Found: {patient}")
        else:
            print(f"Patient with ID {patient_id} not found.")
    elif choice == "4":
        patient_id = input("Enter patient ID to delete: ")
        delete_patient_by_id(patient_id)
    elif choice == "5":
        patient_id = input("Enter patient ID to update: ")
        update_patient_by_id(patient_id)
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

# method -2

class HospitalManagementSystem:
    def __init__(self):
        self.patient_records = []

    def add_patient(self):
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        gender = input("Enter patient gender: ")
        record = {"ID": patient_id, "Name": name, "Age": age, "Gender": gender}
        self.patient_records.append(record)
        print("Patient record added successfully!")

    def display_patients(self):
        if not self.patient_records:
            print("No patient records found.")
        else:
            print("Patient Records:")
            for record in self.patient_records:
                print(f"ID: {record['ID']}, Name: {record['Name']}, Age: {record['Age']}, Gender: {record['Gender']}")

    def search_patient_by_id(self, patient_id):
        for record in self.patient_records:
            if record["ID"] == patient_id:
                return record
        return None

    def delete_patient_by_id(self, patient_id):
        for record in self.patient_records:
            if record["ID"] == patient_id:
                self.patient_records.remove(record)
                print(f"Patient with ID {patient_id} has been deleted.")
                return
        print(f"Patient with ID {patient_id} not found.")

    def update_patient_by_id(self, patient_id):
        record = self.search_patient_by_id(patient_id)
        if record:
            print("Patient Found. Please update the following information:")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            record["Name"] = name
            record["Age"] = age
            record["Gender"] = gender
            print("Patient record updated successfully!")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def run(self):
        while True:
            print("\nHospital Management System Menu:")
            print("1. Add a new patient")
            print("2. Display all patients")
            print("3. Search for a patient by ID")
            print("4. Delete a patient by ID")
            print("5. Update a patient's details by ID")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.display_patients()
            elif choice == "3":
                patient_id = input("Enter patient ID to search: ")
                patient = self.search_patient_by_id(patient_id)
                if patient:
                    print(f"Patient Found: {patient}")
                else:
                    print(f"Patient with ID {patient_id} not found.")
            elif choice == "4":
                patient_id = input("Enter patient ID to delete: ")
                self.delete_patient_by_id(patient_id)
            elif choice == "5":
                patient_id = input("Enter patient ID to update: ")
                self.update_patient_by_id(patient_id)
            elif choice == "6":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the HospitalManagementSystem class and run the program
if __name__ == "__main__":
    hospital_system = HospitalManagementSystem()
    hospital_system.run()
