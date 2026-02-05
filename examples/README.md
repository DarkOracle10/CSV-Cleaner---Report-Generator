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
python ../csv_cleaner.py messy_data.csv --report
```
