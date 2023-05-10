
import subprocess


print("Welcome to PyDatabase v1")
print("To get started please type your ID and your passcod")

ID = input("Enter your ID here:")
passcode = input("Enter your passcode:")

temp = open("temp.txt", "w")
temp.write(ID)
temp.close()

if ID == "User" or "UserAdmin" or "Admin":
    print("Hello",ID)
else: 
    print("The ID you provided is invalid.")

if ID == "User":
    if passcode =="Thisisapasscode":
        print("welcome to the database!")

        subprocess.Popen("python Database.py")
    else: 
        print("The passcode is incorrect.")
        print("You have two more attempts.")
        passcode = input("Passcode:")

        if passcode == "Thisisapasscode":
            print("Welcome to the database!")

            subprocess.Popen("python Database.py")
        else:
            print("You have one more attempt:")
            passcode = input("Passcode:")

            if passcode == "Thisisapasscode":
                print("Welcome to the database!")

                subprocess.Popen("python Database.py")
            else:
                print("The passcode you provided is incorrect. Database access denied!") 
                exit

elif ID == "UserAdmin":
    if passcode =="ThisisapasscodeUA":
        print("welcome to the database!")

        subprocess.Popen("python Database.py")
    else: 
        print("The passcode is incorrect.")
        print("You have two more attempts.")
        passcode = input("Passcode:")

        if passcode == "ThisisapasscodeUA":
            print("Welcome to the database!")

            subprocess.Popen("python Database.py")
        else:
            print("You have one more attempt:")
            passcode = input("Passcode:")

            if passcode == "ThisisapasscodeUA":
                print("Welcome to the database!")

                subprocess.Popen("python Database.py")
            else:
                print("The passcode you provided is incorrect. Database access denied!") 
                exit

elif ID == "Admin":
    if passcode =="ThisisapasscodeA":
        print("welcome to the database!")

        subprocess.Popen("python Database.py")
    else: 
        print("The passcode is incorrect.")
        print("You have 2 more attempts.")
        passcode = input("Passcode:")

        if passcode == "ThisisapasscodeA":
            print("Welcome to the database!")

            subprocess.Popen("python Database.py")
        else:
            print("You have one more attempt:")
            passcode = input("Passcode:")

            if passcode == "ThisisapasscodeA":
                print("Welcome to the database!")

                subprocess.Popen("python Database.py")
            else:
                print("The passcode you provided is incorrect. Database access denied!") 
                exit