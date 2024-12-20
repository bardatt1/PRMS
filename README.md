<a id="prms-top"></a>

## PRMS (Patient Record Management System)

### About The Project

![homescreen](https://github.com/user-attachments/assets/fe83bc92-7e89-4d70-a67a-f22fc9ec6b34)

PRMS is a Patient Record Management System designed to streamline the process of managing patient appointments, records, and recent activities within a healthcare setting. With a user-friendly interface, PRMS helps healthcare professionals organize daily tasks, track patient information, and manage schedules efficiently.

### Built With



## **Key Features**

    **Appointments:** Quickly view upcoming appointments or check if there are any scheduled for today.
    **Patient Records:** Access a list of patients and easily view their details.
    **Recent Activities**: Keep track of recent actions, including password changes, document uploads, and appointment settings.

## **Why PRMS?**

    **Efficiency:** Allows healthcare professionals to focus on providing quality care by reducing the time spent on administrative tasks.
    **Ease of Use:** Features a simple, intuitive interface for navigating and managing patient data.
    **Organization:** Provides a comprehensive overview of all appointments, patients, and activities in one convenient location.

<p align="right">(<a href="#prms-top">back to top</a>)</p>

------------------------------------------------------------------------------

## Getting Started
------------------------------------------------------------------------------
To get a local copy up and running, follow these steps:

1. Clone the repository:
   ```sh
   https://github.com/bardatt1/PRMS.git
   ```
2. Navigate to the project directory:
   ```sh
   cd PRMS
   ```
   ```sh
   cd prms
   ```
3. Make sure to do the necessary migrations
   ```sh
   py manage.py makemigrations [app]
   ```
   ```sh
   py manage.py migrate
   ```
4. Start the application:
   ```sh
   py manage.py runserver
   ```

Usage:
View Appointments: See all upcoming and current appointments.
Manage Patients: Add, edit, or remove patient details.
Track Activities: View recent system activities and changes.

<p align="right">(<a href="#prms-top">back to top</a>)</p>

------------------------------------------------------------------------------

## Members: 
1. Arda, Brett Westley A.
2. Queita, Angelo C.
3. Jaca, Luis Miguel A

<a href="https://github.com/bardatt1/PRMS/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bardatt1/PRMS" />
</a>

  
<p align="right">(<a href="#prms-top">back to top</a>)</p>

------------------------------------------------------------------------------

# Functions Overview

This document outlines the key functions and descriptions of the system.

## Key Functions

### User Authentication and Authorization
- **Description**: Ensures that only authorized personnel can access and manage patient records.
  - **Login**: Validate user credentials (username and password) to grant access.
  - **Role-Based Access Control**: Assign permissions based on user roles (e.g., Doctor, Nurse, Administrator) to control access to different system features.
  - **Password Management**: Allow users to reset their passwords securely and update account details.

---

### Patient Record Creation and Management
- **Description**: Allows authorized users to create and manage patient records.
  - **Record Creation**: Input and save patient details, including personal and medical information.
  - **Record Updating**: Edit existing patient records to reflect the latest information.
  - **Change Log**: Maintain a detailed log of all modifications made to patient records for auditing purposes.

---

### Appointment Scheduling
- **Description**: Provides functionality to schedule, view, and manage patient appointments.
  - **Appointment Creation**: Schedule new appointments by selecting a patient, date, time, and healthcare provider.
  - **Availability Check**: Display available time slots and prevent double-booking of appointments.
  - **Appointment Management**: Reschedule or cancel appointments as needed.

---

### Medical History and Documentation
- **Description**: Enables users to document and retrieve a patient’s medical history and associated documents.
  - **Medical History Input**: Add and update a patient’s medical history, including diagnoses, treatments, medications, and allergies.
  - **Chronological Organization**: Organize medical history entries chronologically for easy reference.
  - **Summary Report**: Create a summary report of a patient’s medical history for quick review.

---

### Search and Filtering
- **Description**: Provides search and filtering functionality to locate patient records and appointments.
  - **Basic Search**: Search for patient records using identifiers like patient ID, name, or contact information.
  - **Advanced Filtering**: Filter search results by parameters such as date range, medical condition, or treatment type.
  - **Result Display**: Display search results in a list with relevant details and options to access the full record.


<p align="right">(<a href="#prms-top">back to top</a>)</p>


------------------------------------------------------------------------------


The following are links related for our output.



## ERD (Patient Record Management System)

Link: https://online.visual-paradigm.com/share.jsp?id=333534383939322d31
![image](https://github.com/user-attachments/assets/b2d250de-e43d-474c-912e-4d190ee60fd4)



## Gannt Chart
Link: https://cebuinstituteoftechnology-my.sharepoint.com/:x:/g/personal/angelo_quieta_cit_edu/Ee6RDhXs7u1FvVxjdS4Up_MBmye3_MB2JnvckHyP__cj8g?e=g8jlOg


## UI/UX Design

Link: https://www.figma.com/design/2ObeBWDO744dSD4CGJ69ei/Patient-Record-Management-System?node-id=0-1&t=l5ySHfuMT5Ei0BeN-1

<p align="right">(<a href="#prms-top">back to top</a>)</p>

