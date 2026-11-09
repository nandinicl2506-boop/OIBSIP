"""A simple command-line BMI (Body Mass Index) calculator."""

import math

# Sanity limits to catch common slips, such as entering height in cm.
WEIGHT_RANGE_KG = (1, 500)
HEIGHT_RANGE_M = (0.3, 2.8)


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI for a weight in kilograms and a height in meters."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Return the standard adult BMI category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def read_number(prompt: str, label: str, unit: str,
                low: float, high: float, hint: str = "") -> float:
    """Keep asking until the user enters a finite number within [low, high]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if not math.isfinite(value):  # rejects "nan" and "inf"
                raise ValueError
        except ValueError:
            print(f"Invalid input! Please enter a valid number for {label}.")
            continue

        if not low <= value <= high:
            message = f"Your {label} should be between {low} and {high} {unit}."
            print(f"{message} {hint}".strip())
            continue

        return value


def main() -> None:
    print("=== Welcome to the Python BMI Calculator ===")

    try:
        weight = read_number(
            "Enter your weight in kg (e.g., 65): ",
            "weight", "kg", *WEIGHT_RANGE_KG,
        )
        height = read_number(
            "Enter your height in meters (e.g., 1.75): ",
            "height", "m", *HEIGHT_RANGE_M,
            hint="If you entered centimeters, convert first (175 cm = 1.75 m).",
        )
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled. Goodbye!")
        return

    # Round first so the category always matches the BMI shown on screen.
    bmi = round(calculate_bmi(weight, height), 2)

    print("\n--- Results ---")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {classify_bmi(bmi)}")
    print("\nNote: BMI is a general screening measure, not a medical diagnosis.")


if __name__ == "__main__":
    main()
  
