# Monotonic Function Checker

# the github contain PDF explanation in Hebrew 

## Code Description
This Python program evaluates Boolean functions across several scenarios, checking whether they are monotonic. A function is considered monotonic if it maintains a consistent order between its inputs and outputs, meaning that if one input is less than or equal to another, then its output must also be less than or equal to the output of the other input.

Components of the Code:
Defining Unique Scenarios:
Various scenarios represent combinations of two activators and two inhibitors, where each can be either on (1) or off (0). Scenarios are chosen to reflect significant differences in their impact on a central gene, thus reducing the number of scenarios from 16 to 9.

Functions for Checking Monotonicity:

is_monotonic: Checks if a given function is monotonic. It does this using helper functions that check if one scenario is less than or equal to another and compares the values in the function accordingly.

is_less_or_equal: Checks if one scenario is less than or equal to another. A scenario is considered less or equal if it has a similar impact on the central gene.

Generating Functions:
Uses the itertools library to create all possible combinations of Boolean functions based on the unique scenarios, then filters out non-monotonic functions.

Outputting Results and Graphical Display:

Uses the pandas and tabulate libraries to print the monotonic functions in a tabular format in the console.
Uses tkinter to create a graphical interface that displays the functions in a table.
The code also includes functions for coloring the text in the console to enhance data visibility.
## Features
- **Generate Functions**: Automatically generates all possible Boolean functions for given scenarios.
- **Check Monotonicity**: Filters and identifies functions that are monotonic based on defined constraints.
- **Visual Representation**: Outputs the monotonic functions in a visually appealing table format in the console and via a Tkinter GUI.

## Dependencies
Before running this script, make sure to install the following Python libraries:
- `tkinter` for the GUI.
- `itertools` for generating combinations of Boolean functions.
- `pandas` for managing and displaying data efficiently.

You can install the necessary libraries with pip:

```bash
pip install pandas tabulate termcolor

How to Run
To run this program, execute the Python script using your preferred Python environment. If all dependencies are installed, the script will generate a console output and a separate window for the Tkinter GUI:

bash
Copy code
python monotonic_function_checker.py
