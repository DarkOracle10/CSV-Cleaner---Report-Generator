# CSV Cleaner Examples

## Sample Files

### messy_data.csv
Example input file with common data quality issues:
- **3 duplicate rows** (rows 8-10 duplicate earlier entries)
- **Missing values** in Age, Email, Salary, and Department columns
- **Inconsistent data types** that need standardization
- Sample dataset with 15 rows total

### cleaned_data.csv
Output after running cleaner with default settings:
- Duplicates removed (12 rows remaining)
- Missing numeric values filled with 0
- Missing text values filled with "N/A"
- Dates standardized to YYYY-MM-DD format

### cleaning_report.txt
Sample report generated during cleaning process showing:
- Rows before and after deduplication
- Number of duplicates removed
- Missing values filled
- Columns that were processed

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
1. **Duplicate removal**: Rows 8-10 are exact duplicates of rows 5, 6, and 2 respectively
2. **Missing value handling**: 
   - Empty Age cells filled with 0
   - Empty Email cells filled with "N/A"
   - Empty Salary cells filled with 0
   - Empty Department cells filled with "N/A"
3. **Date standardization**: All dates converted to YYYY-MM-DD format
4. **Data consistency**: Ensures all data types are properly formatted

## Try It Yourself

Edit `messy_data.csv` to add your own data quality issues and run the cleaner to see how it handles them!
