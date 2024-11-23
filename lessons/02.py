# Calculates the number of days until next birthday

from datetime import datetime

birth_date = input("Enter your birthdate (MM-DD): ")
current_year = datetime.now().year
next_birthday = datetime.strptime(f"{current_year}-{birth_date}", "%Y-%m-%d")
if next_birthday < datetime.now():
    next_birthday = next_birthday.replace(year=current_year + 1)

days_left = (next_birthday - datetime.now()).days
print(f"Your next birthday is in {days_left} days!")