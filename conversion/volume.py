
units = {
    "kiloliter": 1000,
    "liter": 1,
    "milliliter": 0.001,
    "microliter": 1e-6,
    "cubic_meter": 1000,
    "cubic_centimeter": 0.001,  
    # US customary
    "gallon": 3.78541,
    "quart": 0.946353,
    "pint": 0.473176,
    "cup": 0.236588,
    "fluid_ounce": 0.0295735,
    "tablespoon": 0.0147868,
    "teaspoon": 0.00492892,
}

measurements = list(units.keys())

def show_menu():
    print("\nAvailable units:\n")
    for i, name in enumerate(measurements, start=1):
        print(f" {i}. {name}")
    print()


def get_choice(prompt):
    while True:
        try:
            n = int(input(prompt))
            if 1 <= n <= len(measurements):
                return measurements[n - 1]
        except ValueError:
            pass
        print("Invalid selection. Try again.")

def convert(start_unit, amount, target_unit):
    litres = amount * units[start_unit]
    return litres / units[target_unit]

def run():
    print("=" * 30)
    print("Measurement Converter")
    print("=" * 30)

    show_menu()

    start_unit = get_choice("Choose starting unit #: ")
    amount = float(input("Enter quantity: "))
    target_unit = get_choice("Convert to unit #: ")

    result = convert(start_unit, amount, target_unit)

    print(f"\n{amount} {start_unit} = {result:.6g} {target_unit}")

if __name__ == "__main__":
    run()