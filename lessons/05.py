# Function that converts temperatures between Celsius and Fahrenheit

def convert_temperature(temp, to_scale):
    if to_scale == "F":
        return temp * 9/5 + 32
    elif to_scale == "C":
        return (temp - 32) * 5/9

temp = float(input("Enter the temperature: "))
scale = input("Convert to (F/C): ").upper()
converted = convert_temperature(temp, scale)
print(f"The converted temperature is {converted:.2f}°{scale}")
