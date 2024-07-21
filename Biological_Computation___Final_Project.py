import tkinter as tk
from tkinter import ttk
from itertools import product
import pandas as pd
from tabulate import tabulate
from termcolor import colored

def is_monotonic(function):
    # Ensure (1, 1, 0, 0) is always 1
    if function[2] != 1:
        return False
    
    # Ensure (0, 0, 1, 1) is always 0
    if function[6] != 0:
        return False
    
    for i in range(len(function)):
        for j in range(len(function)):
            if is_less_or_equal(unique_scenarios[i], unique_scenarios[j]) and function[i] > function[j]:
                return False
    return True

#check if scenario1 is less then or equal scenario2
def is_less_or_equal(scenario1, scenario2): 
    #if all inhibitors the same check 
    if(scenario1[2]==scenario2[2] and scenario1[3]==scenario2[3]):
        if (scenario1[0]<=scenario2[0] and scenario1[1]<=scenario2[1]):
            return True

    #if all activators the same check         
    if(scenario1[0]==scenario2[0] and scenario1[1]==scenario2[1]):
        if(scenario1[2]>=scenario2[2] and scenario1[3]>=scenario2[3]):
            return True
    return False

# Define unique scenarios (inputs) considering monotonic constraints
#(act1, act2, inh1, inh2)
unique_scenarios = [
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 1, 0),
    (0, 0, 1, 1),
    (1, 0, 1, 1),
    (1, 1, 1, 1),
]

# Generate all possible Boolean functions for these scenarios
all_functions = list(product([0, 1], repeat=len(unique_scenarios)))

# Filter functions that are monotonic
monotonic_functions = [f for f in all_functions if is_monotonic(f)]



######################################################################## print
data = []
for function in monotonic_functions:
    row = [colored('1', 'red') if x == 1 else colored('0', 'white') for x in function]
    data.append(row)

df = pd.DataFrame(data, columns=[str(sc) for sc in unique_scenarios])

def show_table():
    new_window = tk.Tk()
    new_window.title("Monotonic Functions Table")

    tree = ttk.Treeview(new_window, columns=list(df.columns), show='headings')
    
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(expand=True, fill='both')
    new_window.mainloop()

# Print the console output
print(tabulate(df, headers='keys', tablefmt='pretty'))
print(f"Number of monotonic functions: {len(monotonic_functions)}")
print("Monotonic functions:")
for function in monotonic_functions:
    print(function)

# Show the table in a new window
show_table()

######################################################################## print
