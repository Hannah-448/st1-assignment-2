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

#Patient Class
class Patient: #starts a new class
    """Represents a patient.""" #docstring

    def __init__(self, patient_id, patient_name): #refers to the specific object
        self.__patient_id = patient_id #store the id on this object as private
        if patient_name == "":
            print("Error: patient_name cannot be empty. Using 'Unknown'.")
            self.__patient_name = "Unknown"
        else:
            self.__patient_name = patient_name
#If blank on name give warning sign and if fine then store it
    def get_patient_id(self):
        return self.__patient_id
#Lets the outside code read the private ids but not able to change it
    def get_patient_name(self):
        return self.__patient_name
#same but for the name
    def set_patient_name(self, patient_name):
        if patient_name == "":
            print("Error: patient_name cannot be empty.")
            return False
        else:
            self.__patient_name = patient_name
            return True
#If the name is blank then it cant be chnaged and is false but otherwise it returns true and the name is updated
    def __str__(self):
        return "Patient " + self.__patient_id + ": " + self.__patient_name
#Shows what gets shown if you print a patient object

#Practitioner Class
class Practitioner:
    """Represents a practitioner."""
#same as patient but added specialty
    def __init__(self, practitioner_id, practitioner_name, specialty):
        self.__practitioner_id = practitioner_id #store the id any id is accepted
        if practitioner_name == "":
            print("Error: practitioner_name cannot be empty. Using 'Unknown'.")
            self.__practitioner_name = "Unknown"
        else:
            self.__practitioner_name = practitioner_name
            #same as patient if left empty
        if specialty == "":
            print("Error: specialty cannot be empty. Using 'General'.")
            self.__specialty = "General"
        else:
            self.__specialty = specialty
#Goes to general if left empty
    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_specialty(self):
        return self.__specialty
#each for a private attribute so the outside code can read
    def set_specialty(self, specialty):
        if specialty == "":
            print("Error: specialty cannot be empty.")
            return False
        else:
            self.__specialty = specialty
            return True
#Same as set patient name it checks it first
    def __str__(self):
        return "Practitioner " + self.__practitioner_id + ": " + self.__practitioner_name + " (" + self.__specialty + ")"
#makes print a practitioner show something

#Appointment class
class Appointment:
    """Links one Patient to one Practitioner at a given time."""

    def __init__(self, appointment_id, patient, practitioner, appointment_time):#whole patient and practitioner objects
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__appointment_time = appointment_time
        self.__status = "SCHEDULED"
#stores all the values as private attributes on the appointment
    #self status is automatically started as scheduled so no way to be invalid at the start
    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient(self):
        return self.__patient

    def get_practitioner(self):
        return self.__practitioner

    def get_appointment_time(self):
        return self.__appointment_time

    def get_status(self):
        return self.__status
#One for each private attribute and all read only
    def set_appointment_time(self, appointment_time):
        if self.__status == "SCHEDULED":
            self.__appointment_time = appointment_time
            return True
        else:
            print("Cannot reschedule an appointment that is", self.__status)
            return False
#Can reschedule the time
    def complete(self):
        if self.__status == "SCHEDULED":
            self.__status = "COMPLETED"
            return True
        else:
            print("Cannot complete an appointment that is", self.__status)
            return False
#Can only be completed if the current status is scheduled
    def cancel(self):
        if self.__status == "SCHEDULED":
            self.__status = "CANCELLED"
            return True
        else:
            print("Cannot cancel an appointment that is", self.__status)
            return False
#same as complete but changes status to cancelled
    def __str__(self):
        return "Appointment " + self.__appointment_id + ": " + self.__status + \
            " (" + self.__patient.get_patient_name() + " with " + \
            self.__practitioner.get_practitioner_name() + ")"
#Builds a readable summary