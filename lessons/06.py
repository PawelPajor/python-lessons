# Program that takes a list of numbers and calculates the average

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
average = sum(numbers) / len(numbers)
print(f"The average is {average:.2f}")
