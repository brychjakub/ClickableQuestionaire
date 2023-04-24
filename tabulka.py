import tkinter as tk
from tkinter import ttk
import random

# Define the label values
labels = ["VN", "SN", "N", "SV", "UV"]
root = tk.Tk()

# Create a canvas with a scrollbar
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

# Pack the scrollbar and canvas to the window
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Attach the frame to the canvas
canvas.create_window((0, 0), window=frame, anchor="nw")

# Generate the labels for each row
rows = []
hidden_values = [
    [random.randint(1, 10) for _ in range(5)] for _ in range(240)
]
hidden_values = [
     [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [4, 3, 2, 1, 0],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]]

for i in range(240):
    row = []
    # Add a label with the row number
    tk.Label(frame, text=str(i+1)).grid(row=i, column=0)
    # Add labels for each column
    for j in range(5):
        # Get the label value for this column
        label_value = labels[j]
        # Add a clickable label with a white background color and the label value
        cell = tk.Label(frame, text=label_value, bg="white", name=f"label{i+1}-{j+1}")
        cell.grid(row=i, column=j+1, padx=5, pady=5)
        cell.bind("<Button-1>", lambda event, row=i, col=j: on_cell_click(row, col))
        row.append(cell)
    rows.append(row)
    
current_row_selection = [-1] * len(rows)


# Create the click event handler for the cells
def on_cell_click(row, col):
    global current_row_selection
    # Reset the color of the current selection in this row
    current_col_selection = current_row_selection[row]
    if current_col_selection != -1:
        rows[row][current_col_selection].config(bg="white")
    # Update the current selection for this row
    current_row_selection[row] = col
    # Set the clicked cell to green
    rows[row][col].config(bg="green")

# Create a button to count the total hidden value of green cells
def count_hidden_values():
    total_hidden_value1 = 0
    total_hidden_value2 = 0
    
    rows_to_check1 = [0, 30, 60, 90, 120, 150, 180, 210]
    rows_to_check2 = [i+1 for i in rows_to_check1]

    letter_counts = {'N': 0, 'E': 0, 'O': 0, 'P': 0, 'S': 0}
    letters = 'NEOPS'

    for j in range(1, 31):
        total_hidden_value = 0
        rows_to_check = [i + (j-1) for i in rows_to_check1]
        rows_to_check2 = [i + (j-1) for i in rows_to_check1]
        for i, row in enumerate(rows):
            current_col_selection = current_row_selection[i]
            if i in rows_to_check and current_col_selection != -1:
                total_hidden_value += hidden_values[i][current_col_selection]
            elif i in rows_to_check2 and current_col_selection != -1:
                total_hidden_value += hidden_values[i][current_col_selection]

        letter = letters[(j-1) % len(letters)]
        letter_counts[letter] += total_hidden_value

        print(f"Value {', '.join([str(r+1) for r in rows_to_check])}: {total_hidden_value} ({letter})")

    

# Print the combined value for each letter
    print('Combined values:')
    for letter, count in letter_counts.items():
        print(f'{letter}: {count}')


# add more print statements for the remaining rows_to_check lists
# Create a button to count the total hidden value of green cells
count_button = tk.Button(frame, text="Count hidden values", command=count_hidden_values)
count_button.grid(row=241, column=0, columnspan=6, pady=10)

# Resize the canvas scroll region to fit the frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Create the main window
root.mainloop()
