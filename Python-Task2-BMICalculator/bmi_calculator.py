"""A simple command-line BMI (Body Mass Index) calculator."""

import math

# Realistic limits, to catch common slips such as typing height in cm.
MIN_WEIGHT_KG, MAX_WEIGHT_KG = 1, 500
MIN_HEIGHT_M, MAX_HEIGHT_M = 0.3, 2.8


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI for a weight in kilograms and a height in meters."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Return the standard adult BMI category for a BMI value."""
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return category


def read_number(prompt: str, name: str, unit: str,
                minimum: float, maximum: float, hint: str = "") -> float:
    """Keep asking until the user enters a valid number between minimum and maximum."""
    while True:
        text = input(prompt).strip()

        # 1. It must be a real number (rejects letters, empty input, "nan" and "inf").
        try:
            value = float(text)
        except ValueError:
            print(f"Invalid input! Please enter a valid number for {name}.")
            continue
        if not math.isfinite(value):
            print(f"Invalid input! Please enter a valid number for {name}.")
            continue

        # 2. It must be greater than zero (rejects negative values and zero).
        if value <= 0:
            print(f"Invalid input! {name.capitalize()} must be greater than zero "
                  "(negative values are not allowed). Please try again.")
            continue

        # 3. It must be realistic.
        if not minimum <= value <= maximum:
            print(f"Please enter a realistic {name} between {minimum} and {maximum} {unit}. "
                  f"{hint}".strip())
            continue

        return value


def main() -> None:
    print("=== Welcome to the Python BMI Calculator ===")

    try:
        weight = read_number(
            "Enter your weight in kg (e.g., 65): ",
            "weight", "kg", MIN_WEIGHT_KG, MAX_WEIGHT_KG,
        )
        height = read_number(
            "Enter your height in meters (e.g., 1.75): ",
            "height", "m", MIN_HEIGHT_M, MAX_HEIGHT_M,
            hint="If you entered centimeters, convert first (175 cm = 1.75 m).",
        )
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled. Goodbye!")
        return

    # Round first so the category always matches the BMI shown on screen.
    bmi = round(calculate_bmi(weight, height), 2)
    category = classify_bmi(bmi)

    print("\n--- Results ---")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    print("\nNote: BMI is a general screening measure, not a medical diagnosis.")


if __name__ == "__main__":
    main()
  
