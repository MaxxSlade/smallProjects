units = {
    "metric_ton": 1_000_000,
    "kilogram": 1000,
    "gram": 1,
    "milligram": 0.001,
    "microgram": 1e-6,
    "pound": 453.592,
    "ounce": 28.3495,
    "stone": 6350.29
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
    grams = amount * units[start_unit]
    return grams / units[target_unit]

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