# Program that saves user input (e.g., a diary entry)
# to a text file and reads it back

entry = input("Write your diary entry: ")
with open("diary.txt", "a") as file:
    file.write(entry + "\n")

print("\nYour diary entries:")
with open("diary.txt", "r") as file:
    print(file.read())