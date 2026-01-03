# 📊 CSV Cleaner & Report Generator

A lightweight utility to tidy messy CSV files and produce a quick text report. It removes duplicate rows, fills missing values, standardizes date columns, saves a cleaned CSV, and writes a summary report.

## ✨ Features
- Load a CSV and drop exact duplicate rows
- Fill missing values (text -> "N/A", numeric -> 0)
- Standardize detected date-like columns to a consistent format (default: YYYY-MM-DD)
- Save the cleaned CSV to a path you choose
- Generate a text report summarizing rows processed, duplicates removed, missing values filled, and which columns were touched

## 📦 Requirements
- Python 3.9+ (tested on Windows)
- Packages: pandas (and its dependencies)

If you are using the provided `CSV/` virtual environment, activate it first:
- PowerShell: `./CSV/Scripts/Activate.ps1`
- Command Prompt: `CSV\Scripts\activate.bat`

## 🚀 Usage
Run from the project folder:

```bash
python csv_cleaner.py <input_file> [output_file]
```

- `input_file`: path to the CSV you want to clean (e.g., `messy_data.csv`)
- `output_file` (optional): where to save the cleaned CSV. If omitted, it saves as `cleaned_<input_name>` next to the script.

Example:

```bash
python csv_cleaner.py messy_data.csv cleaned.csv
```

What happens:
- Loads the CSV
- Drops duplicate rows
- Detects date-like columns and formats them to the chosen pattern (default `YYYY-MM-DD`)
- Fills missing text with `N/A` and missing numbers with `0`
- Saves the cleaned CSV
- Writes a report next to the output (e.g., `cleaned_report.txt`)

## ⚙️ Customizing date format or report path (from Python)

```python
from csv_cleaner import clean_csv_file

clean_csv_file(
    input_file="messy_data.csv",
    output_file="cleaned.csv",
    report_file="reports/run1.txt",  # optional; defaults to cleaned_report.txt
    date_format="%Y-%m-%d %H:%M:%S",  # optional
)
```

## 💡 Tips
- Keep backups of your raw CSVs before overwriting.
- If a column has mixed types, the date standardization will only affect values that can be parsed as dates; others become `NaT` and then fill with `N/A`.
- The report lists which columns were treated as dates and which had missing values filled.

## 👤 Author
- Name: Amir Aeini
- GitHub: https://github.com/DarkOracle10
