# CSV Cleaner Examples

## Sample Files

### messy_data.csv
Example input file with common data quality issues:
- Duplicate rows
- Missing values in multiple columns
- Inconsistent date formats
- Extra whitespace

### cleaned_data.csv
Output after running cleaner with default settings

### cleaning_report.txt
Sample report generated with `--report` flag

## Quick Test

```bash
cd examples
python ../csv_cleaner.py messy_data.csv
```

This will create:
- `cleaned_messy_data.csv` - The cleaned output file
- `cleaned_messy_data_report.txt` - A report of operations performed

## What Gets Cleaned?

The example demonstrates:
1. **Duplicate removal**: Rows 8-10 are exact duplicates that get removed
2. **Missing value handling**: Empty cells in numeric columns filled with 0, text columns with "N/A"
3. **Date standardization**: Various date formats (MM/DD/YYYY, DD-MM-YYYY) converted to YYYY-MM-DD
4. **Whitespace cleanup**: Leading/trailing spaces removed

## Try It Yourself

Edit `messy_data.csv` to add your own data quality issues and run the cleaner to see how it handles them!
