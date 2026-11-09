# BMI Calculator (Python)

**Oasis Infobyte SIP: Python Programming, Task 2 (Beginner Tier)**

A simple command-line program that calculates a person's Body Mass Index (BMI) from their weight and height and classifies the result into a standard health category.

## Features

- Prompts for weight (kg) and height (m) in the command line
- Calculates BMI using the formula `BMI = weight / (height²)`
- Displays the BMI rounded to 2 decimal places
- Classifies the result into a standard category
- Input validation with clear error messages:
  - Rejects non-numeric input (including `nan` and `inf`)
  - Rejects zero and negative values
  - Rejects unrealistic values and reminds you to convert centimeters to meters
- Exits cleanly on Ctrl+C / Ctrl+D instead of showing an error

## BMI Categories

| BMI            | Category      |
|----------------|---------------|
| Below 18.5     | Underweight   |
| 18.5 – 24.99   | Normal weight |
| 25 – 29.99     | Overweight    |
| 30 and above   | Obese         |

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only the built-in `math` module)

## How to Run

```bash
python bmi_calculator.py
```

## Sample Output

```
=== Welcome to the Python BMI Calculator ===
Enter your weight in kg (e.g., 65): 65
Enter your height in meters (e.g., 1.75): 1.75

--- Results ---
Your BMI is: 21.22
Category: Normal weight

Note: BMI is a general screening measure, not a medical diagnosis.
```

**Input validation example:**

```
Enter your weight in kg (e.g., 65): abc
Invalid input! Please enter a valid number for weight.
Enter your weight in kg (e.g., 65): -5
Your weight should be between 1 and 500 kg.
Enter your weight in kg (e.g., 65): 65
```

## Code Structure

| Function         | Purpose                                                        |
|------------------|----------------------------------------------------------------|
| `calculate_bmi`  | Returns BMI from weight (kg) and height (m)                    |
| `classify_bmi`   | Returns the BMI category for a given BMI value                 |
| `read_number`    | Keeps asking until the user enters a valid number in range     |
| `main`           | Runs the program: input, calculation and result display        |

## Screenshots

Add your output screenshot here, for example: `![BMI Calculator Output](screenshot.png)`

## Disclaimer

BMI is a general screening measure and not a medical diagnosis. Consult a healthcare professional for health advice.

## Author 

Nandini Datta
Oasis Infobyte Summer Internship Program (OIBSIP), Python Programming Track
