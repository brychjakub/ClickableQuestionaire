#  coding: utf-8 

from reportlab.lib.colors import black
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
import tkinter as tk
import tabulka


def generate_pdf(name, surname, age, date, sex, evaluation, q1, q2, q3, counts):
    canvas = Canvas(f"{name}_{surname}_info.pdf", pagesize=LETTER)
    canvas.setFont("Courier", 12)

    # Draw black text one inch from the left and ten
    # inches from the bottom
    canvas.setFillColor(black)
    canvas.drawString(1 * inch, 9.75 * inch, f"Jméno: {name} {surname}")
    canvas.drawString(1 * inch, 9.25 * inch, f"Vek: {age}")
    canvas.drawString(1 * inch, 8.75 * inch, f"Datum: {date}")
    canvas.drawString(1 * inch, 8.25 * inch, f"Pohlaví: {sex}")
    canvas.drawString(1 * inch, 7.75 * inch, f"Posouzení: {evaluation}")
    canvas.drawString(1 * inch, 7.25 * inch, f"Snažil(a) jsem se odpovídat upřímně: {q1}")
    canvas.drawString(1 * inch, 6.75 * inch, f"Odpověděl(a) jsem na všechny výroky: {q2}")
    canvas.drawString(1 * inch, 6.25 * inch, f"Zaznamenal(a) jste své odpovědi na správné místo?: {q3}")
    canvas.drawString(2 * inch, 4 * inch, f"{counts}")

    canvas.save()

def get_user_info():
    name = input_name.get()
    surname = input_surname.get()
    age = input_age.get()
    date = input_date.get()
    sex = input_sex.get()
    evaluation = input_evaluation.get()
    q1 = input_q1.get()
    q2 = input_q2.get()
    q3 = input_q3.get()

    generate_pdf(name, surname, age, date, sex, evaluation, q1, q2, q3, counts)
    root.destroy()

root = tk.Tk()
root.title("Osobní informace")

# Add input fields for user to enter their information
name_label = tk.Label(root, text="Jméno (bez interpunkce):")
name_label.grid(row=0, column=0)
input_name = tk.Entry(root)
input_name.grid(row=0, column=1)

surname_label = tk.Label(root, text="Příjmení (bez interpunkce):")
surname_label.grid(row=1, column=0)
input_surname = tk.Entry(root)
input_surname.grid(row=1, column=1)

age_label = tk.Label(root, text="Věk:")
age_label.grid(row=2, column=0)
input_age = tk.Entry(root)
input_age.grid(row=2, column=1)

date_label = tk.Label(root, text="Datum:")
date_label.grid(row=3, column=0)
input_date = tk.Entry(root)
input_date.grid(row=3, column=1)

surname_label = tk.Label(root, text="Pohlaví:")
surname_label.grid(row=4, column=0)
input_sex = tk.Entry(root)
input_sex.grid(row=4, column=1)

age_label = tk.Label(root, text="Posouzení (sebeposuzování / posouzení jiného):")
age_label.grid(row=5, column=0)
input_evaluation = tk.Entry(root)
input_evaluation.grid(row=5, column=1)

date_label = tk.Label(root, text="Snažil(a) jsem se odpovídat upřímně (VN | SN | N | SV | UV):")
date_label.grid(row=6, column=0)
input_q1 = tk.Entry(root)
input_q1.grid(row=6, column=1)

age_label = tk.Label(root, text="Odpověděl(a) jsem na všechny výroky (Ano | Ne):")
age_label.grid(row=7, column=0)
input_q2 = tk.Entry(root)
input_q2.grid(row=7, column=1)

date_label = tk.Label(root, text="Zaznamenal(a) jste své odpovědi na správné místo? (Ano | Ne):")
date_label.grid(row=8, column=0)
input_q3 = tk.Entry(root)
input_q3.grid(row=8, column=1)

counts = tabulka.count_hidden_values()

# Add a button to generate the PDF
generate_button = tk.Button(root, text="Generate PDF", command=get_user_info)
generate_button.grid(row=9, column=0, columnspan=2)

root.mainloop()
