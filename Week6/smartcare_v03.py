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