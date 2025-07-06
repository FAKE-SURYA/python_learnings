def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Choose conversion (1/2/3/4): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.2f}°C")

elif choice == "3":
    c = float(input("Enter temperature in Celsius: "))
    k = celsius_to_kelvin(c)
    print(f"{c}°C = {k:.2f}K")

elif choice == "4":
    k = float(input("Enter temperature in Kelvin: "))
    c = kelvin_to_celsius(k)
    print(f"{k}K = {c:.2f}°C")

else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
