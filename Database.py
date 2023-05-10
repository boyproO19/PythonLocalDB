
import subprocess

temp = open("temp.txt", "r")
name = temp.read()
print("Welcome to the database!" + "",name)
temp.close()

print ("What data would you like to access?")
print ("Print Data, Add Data, Delete Data File")
print ("Press 1   , Press 2 , Press 3")

Var = int(input("Make your choice:"))

if Var == 1:
    subprocess.Popen("Python DataBaseSofts\\Printer.py")
elif Var == 2:
    subprocess.Popen("Python DataBaseSofts\\Dataappend.py")
elif Var == 3:
    subprocess.Popen("Python DataBaseSofts\\Databasedelete.py")
else:
    print("Your Input is invalid.")
