# Program that asks for numbers,
# handles invalid input gracefully,
# and calculates their sum.

numbers = []
while True:
    try:
        num = input("Enter a number (or type 'done'): ")
        if num.lower() == "done":
            break
        numbers.append(float(num))
    except ValueError:
        print("Invalid input, please enter a number.")

print(f"The sum of the numbers is {sum(numbers)}")
