
units = {
    "mega": 1_000_000,
    "kilo": 1_000,
    "hecto": 100,
    "deka": 10,
    "meter": 1,
    "deci": 0.1,
    "centi": 0.01,
    "milli": 0.001,
    "micro": 1e-6,
    "nano": 1e-9,
    "feet": 0.3048,
    "miles": 1609.34,
    "inches": 0.0254
}

measurements = list(units.keys())


def show_menu():
    print("\nAvailable units:\n")
    for i, name in enumerate(measurements, start=1):
        print(f"{i:>2}. {name}")
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
    meters = amount * units[start_unit]
    return meters / units[target_unit]


# ---- program flow ----
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