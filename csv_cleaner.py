import sys
import pandas as pd
from pathlib import Path
from datetime import datetime


def clean_csv_file(input_file, output_file, report_file=None, date_format="%Y-%m-%d"):
    """Load a CSV, remove duplicates, standardize dates, fill missing values, save cleaned file, and write a report.

    Args:
        input_file: Path to the source CSV.
        output_file: Destination path for cleaned CSV.
        report_file: Optional path for the text report. Defaults to `<output>_report.txt`.
        date_format: Desired date string format (default: YYYY-MM-DD).
    """

    input_path = Path(input_file)
    output_path = Path(output_file)
    report_path = (
        Path(report_file)
        if report_file
        else output_path.with_name(f"{output_path.stem}_report.txt")
    )

    df = pd.read_csv(input_path)
    original_rows = len(df)

    # Drop exact duplicate rows to avoid double counting
    df = df.drop_duplicates()
    deduped_rows = len(df)

    # Standardize date-like columns to the requested format
    date_columns = []
    candidate_date_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in candidate_date_cols:
        parsed = pd.to_datetime(df[col], errors="coerce", utc=False, infer_datetime_format=True)
        if parsed.notna().any():
            df[col] = parsed.dt.strftime(date_format)
            date_columns.append(col)

    text_cols = df.select_dtypes(include=["object", "string"]).columns
    num_cols = df.select_dtypes(include=["number"]).columns

    missing_before = int(df.isna().sum().sum())

    if len(text_cols) > 0:
        df[text_cols] = df[text_cols].fillna("N/A")

    if len(num_cols) > 0:
        df[num_cols] = df[num_cols].fillna(0)

    missing_after = int(df.isna().sum().sum())
    filled_missing = missing_before - missing_after

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    report_lines = [
        f"CSV Cleaning Report - {datetime.now().isoformat(timespec='seconds')}",
        f"Input file: {input_path}",
        f"Output file: {output_path}",
        f"Rows before: {original_rows}",
        f"Rows after deduplication: {deduped_rows}",
        f"Duplicate rows removed: {original_rows - deduped_rows}",
        f"Missing values filled: {filled_missing}",
        f"Date columns standardized: {', '.join(date_columns) if date_columns else 'None'}",
        f"Text columns filled with 'N/A': {', '.join(text_cols) if len(text_cols) else 'None'}",
        f"Numeric columns filled with 0: {', '.join(num_cols) if len(num_cols) else 'None'}",
    ]

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv_cleaner.py <input_file> [output_file]")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2] if len(sys.argv) > 2 else f"cleaned_{Path(input_csv).name}"

    print(f"Cleaning {input_csv}...\n")
    cleaned_df = clean_csv_file(input_csv, output_csv)
    print(f"Done. Cleaned file written to {output_csv}")
