# 📊 CSV Cleaner & Report Generator

> Automated Python utility for cleaning messy CSV data with duplicate removal, missing value handling, and comprehensive report generation.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/pandas-latest-150458?style=for-the-badge)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

## ✨ Features

- 🧹 **Remove Duplicates** - Automatically detect and remove duplicate rows
- 🔧 **Fill Missing Values** - Smart filling with mean/median/mode or custom values
- 📅 **Date Standardization** - Auto-detect and format date columns consistently
- 📝 **Report Generation** - Detailed text reports with before/after statistics
- 🎯 **Column Filtering** - Clean specific columns or entire dataset
- ⚡ **Fast Processing** - Pandas-powered for large datasets
- 🔍 **Data Quality Checks** - Identify data quality issues

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/DarkOracle10/CSV-Cleaner---Report-Generator.git
cd CSV-Cleaner---Report-Generator

# Install dependencies
pip install pandas numpy python-dateutil

# Or use requirements.txt
pip install -r requirements.txt
```

### Basic Usage

```bash
# Clean a CSV file
python csv_cleaner.py input_data.csv

# Clean and generate report
python csv_cleaner.py input_data.csv --report

# Remove duplicates only
python csv_cleaner.py input_data.csv --remove-duplicates

# Fill missing values with mean
python csv_cleaner.py input_data.csv --fill-missing mean
```

## 📖 Usage Examples

### Example 1: Basic Cleaning

```bash
python csv_cleaner.py messy_data.csv
# Output: messy_data_cleaned.csv
```

### Example 2: Full Cleaning with Report

```bash
python csv_cleaner.py sales_data.csv --report --output cleaned_sales.csv
# Output: cleaned_sales.csv + cleaning_report.txt
```

### Example 3: Python API

```python
from csv_cleaner import CSVCleaner

# Initialize cleaner
cleaner = CSVCleaner('data.csv')

# Remove duplicates
cleaner.remove_duplicates()

# Fill missing values
cleaner.fill_missing_values(strategy='mean')

# Standardize dates
cleaner.standardize_dates()

# Generate report
report = cleaner.generate_report()
print(report)

# Save cleaned data
cleaner.save('cleaned_data.csv')
```

## 🎯 Features in Detail

### Duplicate Removal
- Identifies exact duplicate rows
- Option to keep first/last occurrence
- Reports number of duplicates removed

### Missing Value Handling
Strategies:
- **mean** - Fill with column mean (numeric only)
- **median** - Fill with column median
- **mode** - Fill with most frequent value
- **forward** - Forward fill from previous row
- **backward** - Backward fill from next row
- **Custom value**

### Date Standardization
- Auto-detects date columns
- Converts to ISO 8601 format (YYYY-MM-DD)
- Handles multiple date formats:
  - MM/DD/YYYY
  - DD-MM-YYYY
  - YYYY/MM/DD
  - And more...

### Report Generation
Includes:
- Original dataset statistics
- Cleaning operations performed
- Before/after comparison
- Data quality metrics
- Processing time

## 📁 Examples

See the `examples/` directory for sample data:

```
examples/
├── messy_data.csv          # Input: Dataset with issues
├── cleaned_data.csv        # Output: After cleaning
├── cleaning_report.txt     # Report: Operations performed
└── example_notebook.ipynb  # Jupyter: Interactive demo
```

## 🛠️ CLI Reference

```
usage: csv_cleaner.py [-h] [--remove-duplicates] [--fill-missing {mean,median,mode,forward,backward}]
                      [--standardize-dates] [--report] [--output OUTPUT] [--columns COLUMNS]
                      input_file

positional arguments:
  input_file            Path to input CSV file

optional arguments:
  -h, --help            Show this help message and exit
  --remove-duplicates   Remove duplicate rows
  --fill-missing STRATEGY
                        Fill missing values with strategy
  --standardize-dates   Standardize date formats
  --report              Generate cleaning report
  --output OUTPUT       Output file path (default: input_cleaned.csv)
  --columns COLUMNS     Comma-separated columns to clean (default: all)

examples:
  python csv_cleaner.py data.csv --remove-duplicates --fill-missing mean
  python csv_cleaner.py data.csv --report --output clean.csv
  python csv_cleaner.py data.csv --columns "Name,Email,Date"
```

## 📊 Sample Report

```
=== CSV Cleaning Report ===
Generated: 2026-02-05 10:30:45

Input File: messy_data.csv
Output File: messy_data_cleaned.csv

Dataset Statistics:
- Original Rows: 1,000
- Original Columns: 15
- Final Rows: 847
- Final Columns: 15

Operations Performed:
1. Removed 153 duplicate rows (15.3%)
2. Filled 45 missing values in column 'Age' with mean (35.2)
3. Filled 12 missing values in column 'Email' with 'N/A'
4. Standardized 1,000 dates in column 'Registration Date'

Data Quality Metrics:
- Completeness: 98.5% (before: 92.1%)
- Duplicates: 0% (before: 15.3%)
- Date Format Consistency: 100% (before: 78.4%)

Processing Time: 0.34 seconds
```

## 🧪 Testing

```bash
# Run tests
pytest tests/

# With coverage
pytest --cov=csv_cleaner tests/
```

## 🤝 Contributing

Contributions welcome! Ideas for improvement:

- [ ] GUI interface
- [ ] Excel file support (.xlsx)
- [ ] Data type inference and conversion
- [ ] Outlier detection and handling
- [ ] Column rename suggestions
- [ ] Data validation rules

## 📄 License

MIT License - See [LICENSE](LICENSE) file

## 👤 Author

**Amir Aeiny**

- GitHub: [@DarkOracle10](https://github.com/DarkOracle10)
- Email: amir.aeiny10@gmail.com

---

⭐ **Found this useful? Star the repo!**
