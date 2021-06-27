import os
import core.patients
import core.employees
import core.admins

clrscr = lambda : os.system('cls||clear') # Clears terminal viewport

def patients() :

    patient = core.patients.Patient()

    clrscr()
    print("\n-----------------|| LOGIN OR SIGNUP ||-----------------")
    patient.name = input("\nENTER YOUR NAME:- ")

    if patient.patient_exists() :

        while True :

            clrscr()
            print(f"\nWELCOME {patient.name}\n\n1. TAKE APPOINTMENT\n2.VIEW APPOINTMENT\n3. FILL PERSONAL INFORMATION\n4. LOGOUT")
            choice = int(input("\nENTER USERS CHOICE(1/ 2/ 3/ 4):- "))
            clrscr()

            if choice == 1 :
                specialization = input("\nWHICH TYPE OF DOCTOR WOULD YOU LIKE TO CONSULT WITH (ORTHO/SURGEON/PHYSICIAN):")
                doctors = patient.get_doctors(specialization)
                if doctors == 0 :
                    print("\nNO OF DOCTORS THAT SPECIALIZATION: ")
                else :
                    print(f"\n\n \tDOCTOR{19 * ' '}SPECIALIZATION\n")
                    for i in range(len(doctors)) :
                        print(f"{i + 1}\t{doctors[i][0]}{(25 - len(doctors[i][0])) * ' '}{doctors[i][1]}")
                    selected_doctor = int(input("\n\nENTER CHOICE OF DOCTOR:- "))
                    while(True) :
                        clrscr()
                        time = int(input("\nWhen would you like to make an appointment?\n\n1. Today\n2. Tomorrow\n3. Day After tomorrow\n\nEnter choice: "))
                        if patient.make_appointment(doctors[selected_doctor-1][0], time) == 1 :
                            break
                        else :
                            print("\nINVALID CHOICE")
                    input("\nAPPOINTMENT MADE SUCCESSFULLY\nPRESS ENTER TO CONTINUE ...")
            
            elif choice == 2 :
                appointments = patient.get_appointments()
                if len(appointments) == 0 :
                    print("\nNo appointments booked")
                else :
                    print(f"\nDOCTOR{19 * ' '}DATE{18 * ' '}PRESCRIPTION\n")
                    for appointment in appointments :
                        if len(appointment) == 3 :
                            print(f"{appointment[0]}{(25 - len(appointment[0])) * ' '}{appointment[2]}{(22 - len(str(appointment[2]))) * ' '}None")
                        else :
                            print(f"{appointment[0]}{(25 - len(appointment[0])) * ' '}{appointment[2]}{(22 - len(str(appointment[2]))) * ' '}{appointment[3]}")
                input("\nPress enter to continue...")

            elif choice == 3 :
                print("\n^^^^^^^^^^^^^^^ Update Personal Information ^^^^^^^^^^^^^^^")
                name = input("\nEnter your name: ")
                age = int(input("Enter your age: "))
                patient.update_user(name, age)
                input("\nDetails updated successfully\nPress enter to continue...")
            
            else :
                del patient
                break
    
    else :

        age = int(input("ENTER AGE:- "))
        gender = input("GENDER ( MALE/FEMALE ): ")
        patient.create_user(age,gender)
        input("\nNew user created successfully. Redirecting to login page.\nPress enter to continue...")
        patients()

def doctors() :

    clrscr()
    name = input("\nLogin\n\nEnter your name: ")
    doctor = core.employees.Doctor(name)

    while doctor != 0 :

        clrscr()
        print(f"\n-----------------WELCOME Dr. {doctor.name}-----------------\n\n1. SEE APPOINTMENTS \n2. PRESCRIBE MEDICINE\n3. LOGOUT")
        choice = int(input("\nEnter your choice: "))
        clrscr()

        if choice == 1 :
            appointments = doctor.get_appointments()
            print(f"\nPATIENT{18 * ' '}DATE\n")
            for appointment in appointments :
                print(appointment["patient_name"], (23 - len(appointment["patient_name"])) * ' ', appointment["date"])
            input("\nPRESS ENTER TO CONTINUE ...")
        
        elif choice == 2 :
            patient_name = input("ENTER NAME OF THE PATIENT: ")
            prescription = input("ENTER PRESCRIPTION FOR THE PATIENT: ")
            doctor.prescribe_medicine(patient_name, prescription)
            input("\npRESCRIPTION SENT\nPRESS ENTER TO CONTINUE ...")

        else :
            del doctor
            break
    
    else :
        print("DOCTOR NAME DOES NOT EXIST")
        input("\nPRESS ENTER TO CONTINUE...")

def admins() :

    admin = core.admins.Admin()

    while True :

        clrscr()
        print("\n-----------------ADMIN'S DASHBOARD-----------------\n\n1. VIEW EMPLOYEES\n2. VIEW PATIENTS\n3. ADD EMPLOYEES\n4. UPDATE EMPLOYEE\n5. LOGOUT")
        choice = int(input("\nENTER YOUR CHOICE:- "))
        clrscr()

        if choice == 1 :
            print("\n^^^^^^^^^^^^^^^ Employees ^^^^^^^^^^^^^^^")
            doctors, nurses, pharmacists = admin.view_all_employees()
            print(f"\nDOCTOR{19 * ' '}SPECIALIZATION{9 * ' '}\n")
            for doctor in doctors :
                print(f"{doctor[0]}{(25 - len(doctor[0])) * ' '}{doctor[1]}")
            print(f"\n\nNURSE{20 * ' '}SPECIALIZATION{9 * ' '}\n")
            for nurse in nurses :
                print(f"{nurse[0]}{(25 - len(nurse[0])) * ' '}{nurse[1]}")
            print(f"\n\nPHARMACIST{15 * ' '}SPECIALIZATION{9 * ' '}\n")
            for pharmacist in pharmacists :
                print(f"{pharmacist[0]}{(25 - len(pharmacist[0])) * ' '}{pharmacist[1]}")
            input("\n\nPress enter to continue...")

        elif choice == 2 :
            print("\n^^^^^^^^^^^^^^^ Patients ^^^^^^^^^^^^^^^")
            patients = admin.view_all_patients()
            print(f"\n\nNAME{21 * ' '}AGE{15 * ' '}GENDER\n")
            for patient in patients :
                print(f"{patient[0]}{(25 - len(patient[0])) * ' '}{patient[1]}{(18 - len(str(patient[1]))) * ' '}{patient[2]}")
            input("\n\nPress enter to continue...")

        elif choice == 3 :
            print("\n^^^^^^^^^^^^^^^ Add Employee ^^^^^^^^^^^^^^^")
            name = input("\nENTER NAME:- ")
            role = input("ENTER ROLE (doctor/ nurse/ pharmacist):- ")
            specialization = input("Enter specialization (Ortho/Surgeon/Physician):- ")
            admin.add_employee(name, role, specialization)
            input("\nEmployee Added Successfully\nPress enter to continue...")

        elif choice == 4 :
            print("\n^^^^^^^^^^^^^^^ UPDATE EMPLOYEE ^^^^^^^^^^^^^^^")
            name = input("\nENTER NAME:- ")
            role = input("ENTER ROLE (doctor/ nurse/ pharmacist):- ")
            specialization = input("ENTER SPECIALIZATION (Ortho/Surgeon/Physician):-  ")
            admin.update_employee(name, role, specialization)
            input("\nEMPLOYEE DETAILS UPDATED SUCCESSFULLY \nPRESS ENTER TO CONTINUE ...")

        else :
            del admin
            break

def main() :

    ''' FLow of control starts here '''

    run = True
    while run :

        clrscr()
        print("\n------------------|| LOGIN FOR ||------------------\n\n                  1. PATIENTS\n                  2. DOCTORS \n                  3. MANAGERS \n                  4. EXIT")
        choice = int(input("\nENTER YOUR CHOICE(1/2/3/4):- "))

        if choice == 1 :
            patients()
        
        elif choice == 2 :
            doctors()

        elif choice == 3 :
            admins()
        
        else : 
            clrscr()
            run = False

if __name__ == "__main__" :
    main()