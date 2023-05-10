
import csv

data = open("Data\\EmpRecords.csv" , "r")

for line in data:

    info = line.split(",")
    print(info)

data.close()