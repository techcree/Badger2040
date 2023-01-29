# Micropython-Skript to make a input in a var file for using to read with an ourther py-script
text = input("Geben Sie den Text ein: ")

with open("text_file.py", "w") as f:
    f.write("text = '" + text + "'")

