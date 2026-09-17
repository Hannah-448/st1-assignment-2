# task 1
# Create and run a simple Python file with basic input,output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# Use lists, dictionaries and functions to enhance the Python file

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")


print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()

#Week6:

class Patient:
    #"""Represents a patient in the SmartCare system."""

    def __init__(self, patient_name: str) -> None:
        self.patient_name: str = patient_name

    def add_patient(self) -> None:
        """Add this patient to the system."""
        pass

    def find_patient(self) -> "Patient":
        #"""Find and return a patient record."""
        pass


class Practitioner:
    #"""Represents a practitioner in the SmartCare system."""

    def __init__(self, practitioner_name: str) -> None:
        self.practitioner_name: str = practitioner_name

    def add_practitioner(self) -> None:
       # """Add this practitioner to the system."""
        pass

    def view_appointments(self) -> list["Appointment"]:
        #"""Return a list of this practitioner's appointments."""
        pass


class Appointment:
    #"""Represents an appointment linking one patient to one practitioner."""

    def __init__(
        self,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str,
        status: str,
    ) -> None:
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.appointment_time: str = appointment_time
        self.status: str = status

    def create(self) -> None:
       # """Create a new appointment."""
        pass

    def update(self) -> None:
       # """Update details of this appointment."""
        pass

    def cancel(self) -> None:
       # """Cancel this appointment."""
        pass