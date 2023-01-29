import os 

setroom = input("Room Numer? ")
with open("setroom_file.py", "w") as f:
    f.write("setroom = '" + setroom + "'")

settext = input("Employee Name? ")
with open("settext_file.py", "w") as f:
    f.write("settext = '" + settext + "'")

setcompany = input("Job Title? ")
with open("setcompany_file.py", "w") as f:
    f.write("setcompany = '" + setcompany + "'")


print (Eingabe wurde gespeichert!)
