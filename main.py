from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin
from shapes.shapes import area_circle, area_rectangle, area_triangle

def main():
    print("=== MAIN MENU ===")
    print("1. Temperature Conversion")
    print("2. Area Calculation")

    choice = input("Enter choice: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))
        print("Kelvin:", celsius_to_kelvin(c))

    elif choice == "2":
        r = float(input("Enter radius: "))
        print("Circle Area:", area_circle(r))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
