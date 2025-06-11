import csv
from fpdf import FPDF
from datetime import date

ingredients = [
    ["Date", "Dish Name", "Ingredient", "Quantity", "Unit"],
    [str(date.today()), "Paneer Bhurji", "Onion", "1", "piece"],
    [str(date.today()), "Paneer Bhurji", "Paneer", "200", "grams"],
    [str(date.today()), "Paneer Bhurji", "Salt", "1", "tsp"],
    [str(date.today()), "Paneer Bhurji", "Tomato", "2", "pieces"]
]

nutrition = [
    ["Date", "Dish Name", "Calories", "Protein (g)", "Fat (g)", "Carbs (g)"],
    [str(date.today()), "Paneer Bhurji", "280", "18", "20", "6"]
]

with open("ingredients_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(ingredients)

with open("nutrition_log.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(nutrition)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, "Kitchen Data Collection Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, """
This report documents the data collected from a home kitchen as part of Week 1 of the Ashoka Horizons course.

Why these fields were chosen:
- We tracked ingredients to monitor consumption and manage inventory.
- Quantities and units were included for precision.
- A separate nutrition file was created to summarize health-related data (calories, protein, etc.).

Why split the data:
- Ingredients and nutritional values represent different levels of granularity.
- Keeping them separate allows for easier analysis (e.g., linking many ingredients to one dish in the nutrition file).

Environment Setup:
- WSL (Windows Subsystem for Linux) was installed via Microsoft Store.
- Miniconda was downloaded from the official site and installed in WSL.
- A conda environment was created using:
  conda create -n horizons python=3.11
  conda activate horizons

All files have been generated automatically and stored for review in the 'week-01' folder.
""")

pdf.output("report.pdf")

print("✅ Files generated: ingredients_log.csv, nutrition_log.csv, report.pdf")
