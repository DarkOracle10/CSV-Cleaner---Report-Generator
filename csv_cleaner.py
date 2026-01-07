import sys
import os
import pandas as pd
from pathlib import Path
from datetime import datetime
from colorama import Fore, Back, Style, init
from tqdm import tqdm
import time

init(autoreset=True)


def clean_csv_file(input_file, output_file, report_file=None, date_format="%Y-%m-%d", show_progress=True):
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

    if show_progress:
        print(f"{Fore.CYAN}[Loading]{Style.RESET_ALL} Reading CSV from {input_path}...")
    df = pd.read_csv(input_path)
    original_rows = len(df)

    # Drop exact duplicate rows to avoid double counting
    if show_progress:
        print(f"{Fore.YELLOW}[Deduplicating]{Style.RESET_ALL} Removing duplicate rows...")
    for _ in tqdm(range(1), desc="Deduplication", unit=" pass", ncols=70):
        time.sleep(0.2)
    df = df.drop_duplicates()
    deduped_rows = len(df)

    # Standardize date-like columns to the requested format
    if show_progress:
        print(f"{Fore.GREEN}[Standardizing]{Style.RESET_ALL} Processing date columns...")
    date_columns = []
    candidate_date_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in tqdm(candidate_date_cols, desc="Date columns", unit=" col", ncols=70):
        parsed = pd.to_datetime(df[col], errors="coerce", utc=False, infer_datetime_format=True)
        if parsed.notna().any():
            df[col] = parsed.dt.strftime(date_format)
            date_columns.append(col)
        time.sleep(0.1)

    text_cols = df.select_dtypes(include=["object", "string"]).columns
    num_cols = df.select_dtypes(include=["number"]).columns

    missing_before = int(df.isna().sum().sum())

    if show_progress:
        print(f"{Fore.BLUE}[Filling]{Style.RESET_ALL} Handling missing values...")
    for _ in tqdm(range(1), desc="Missing values", unit=" pass", ncols=70):
        time.sleep(0.2)

    if len(text_cols) > 0:
        df[text_cols] = df[text_cols].fillna("N/A")

    if len(num_cols) > 0:
        df[num_cols] = df[num_cols].fillna(0)

    missing_after = int(df.isna().sum().sum())
    filled_missing = missing_before - missing_after

    if show_progress:
        print(f"{Fore.MAGENTA}[Saving]{Style.RESET_ALL} Writing cleaned CSV...")
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

    if show_progress:
        print(f"\n{Fore.GREEN}[✓ Complete]{Style.RESET_ALL} Cleaning finished!")
        print(f"\n{Fore.CYAN}Summary:{Style.RESET_ALL}")
        print(f"  Rows processed: {original_rows} → {deduped_rows}")
        print(f"  Duplicates removed: {original_rows - deduped_rows}")
        print(f"  Missing values filled: {filled_missing}")
        print(f"  Date columns: {len(date_columns)}")
        print(f"\n{Fore.MAGENTA}Output:{Style.RESET_ALL}")
        print(f"  CSV: {output_path}")
        print(f"  Report: {report_path}")

    return df


if __name__ == "__main__":
    print(f"\n{Back.BLUE}{Fore.WHITE}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}║    CSV Cleaner & Data Processing Tool      ║{Style.RESET_ALL}")
    print(f"{Back.BLUE}{Fore.WHITE}╚════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}No arguments provided. Showing interactive menu...{Style.RESET_ALL}\n")
        
        # Interactive menu
        input_csv = input(f"{Fore.CYAN}Enter input CSV file path (e.g., messy_data.csv): {Style.RESET_ALL}").strip()
        if not input_csv:
            input_csv = "messy_data.csv"
        
        output_csv = input(f"{Fore.CYAN}Enter output file path [{Fore.GREEN}cleaned_{Path(input_csv).name}{Fore.CYAN}]: {Style.RESET_ALL}").strip()
        if not output_csv:
            output_csv = f"cleaned_{Path(input_csv).name}"
        
        date_fmt = input(f"{Fore.CYAN}Enter date format [{Fore.GREEN}%Y-%m-%d{Fore.CYAN}]: {Style.RESET_ALL}").strip()
        if not date_fmt:
            date_fmt = "%Y-%m-%d"
        
        print()
    else:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2] if len(sys.argv) > 2 else f"cleaned_{Path(input_csv).name}"
        date_fmt = sys.argv[3] if len(sys.argv) > 3 else "%Y-%m-%d"

    if not Path(input_csv).exists():
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File not found: {input_csv}")
        sys.exit(1)

    print(f"{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}\n")
    clean_csv_file(input_csv, output_csv, date_format=date_fmt)
    print(f"\n{Fore.CYAN}═══════════════════════════════════════════{Style.RESET_ALL}\n")
