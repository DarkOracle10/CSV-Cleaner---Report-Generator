from __future__ import annotations

import io
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)


# -----------------------------
# Configuration and Data Inputs
# -----------------------------

NAME = "Amir Aeiny"
TITLE = "Python Developer | Automation · Data Processing"
GITHUB = "https://github.com/DarkOracle10"
LINKEDIN = "https://www.linkedin.com/in/amir-aeiny-dev"

PROJECT_NAME = "CSV Data Cleaner & Automation Suite"
PROJECT_TYPE = "Python Automation Tool - Data Processing & File Management System"

TECH_STACK = [
    ("Backend", "Python 3.11+"),
    ("Data Processing", "pandas, numpy"),
    ("Excel/CSV", "openpyxl, xlrd, xlsxwriter, csv"),
    ("File Operations", "os, pathlib, shutil, glob"),
    ("Data Validation", "validators, regex, dateutil"),
    ("CLI", "argparse, click"),
    ("Progress Tracking", "tqdm, colorama"),
    ("Reporting", "matplotlib, reportlab"),
    ("Date Handling", "dateutil.parser, datetime"),
    ("Testing", "pytest, unittest"),
    ("Logging", "Python logging module"),
    ("VCS", "Git, GitHub"),
]

PROJECT_STATS = [
    ("Lines of Code", "1,800+"),
    ("Automation Functions", "15+ (dedupe, dates, merge, split, etc.)"),
    ("File Format Support", "5 (CSV, XLSX, XLS, TXT, JSON)"),
    ("Data Cleaning Operations", "10+ (duplicates, missing values, validation)"),
    ("Report Generation", "3 formats (TXT, Excel, PDF optional)"),
    ("Test Coverage", "85%+ with pytest"),
    ("Processing Speed", "10,000+ rows/second"),
    ("Error Handling", "Comprehensive with user-friendly messages"),
    ("Project Status", "Production Ready"),
]

PROJECT_OVERVIEW = (
    "A robust Python automation suite for cleaning, transforming, and processing CSV/Excel files, "
    "designed to save hours of manual data work. Features intelligent duplicate removal with configurable "
    "criteria, smart date standardization that handles multiple input formats, missing value handling with "
    "multiple strategies (fill, drop, interpolate), data validation with custom rules, and automated report "
    "generation. Built with pandas for high-performance data processing, supports batch operations on multiple "
    "files, includes comprehensive error handling and logging, and provides clear progress tracking. Ideal for "
    "businesses processing customer data, sales reports, inventory management, or any repetitive spreadsheet tasks."
)

KEY_FEATURES = [
    "Intelligent Duplicate Removal — configurable columns and matching strategies",
    "Smart Date Standardization — auto-detects and harmonizes many formats",
    "Missing Value Handling — forward/backward fill, mean/median, defaults",
    "Data Type Validation — text, numbers, dates, emails, phones",
    "File Merging — combine many files with dedupe and alignment",
    "File Splitting — chunk by row count or target size",
    "Column Operations — rename, reorder, add/remove, bulk mappings",
    "Automated Reporting — TXT/Excel/PDF with stats and quality metrics",
    "Batch Processing — whole folders, filters, optional parallelism",
    "User-Friendly CLI — argparse/click, colors, progress bars, help",
]

SKILLS = {
    "Python Programming": [
        "Python 3.11+ best practices",
        "OOP and functional patterns",
        "Exception handling and recovery",
        "File I/O and path handling",
        "Regex for pattern matching",
    ],
    "Data Processing": [
        "pandas DataFrame ops (filter/group/aggregate)",
        "numpy for numerics",
        "Cleaning and transformation pipelines",
        "Memory-efficient large datasets",
        "Type inference and conversion",
    ],
    "File Format Handling": [
        "CSV with varied delimiters/encodings",
        "Excel (XLSX, XLS) multi-sheet",
        "JSON import/export",
        "TXT processing",
        "Encoding detection, UTF-8",
    ],
    "Automation & Scripting": [
        "CLI design (argparse/click)",
        "Batch processing",
        "Schedulable tasks",
        "tqdm progress bars",
        "Colorama terminal output",
    ],
    "Data Validation": [
        "Custom rules and constraints",
        "Type checking and conversion",
        "Regex pattern checks",
        "Business rule enforcement",
        "Actionable error reporting",
    ],
    "Professional": [
        "Clean, modular code",
        "Comprehensive error handling",
        "Logging and monitoring",
        "Unit tests (85%+ coverage)",
        "Docstrings and Git discipline",
    ],
}

SIMILAR_PROJECTS = {
    "Data Cleaning & Processing": [
        "Customer database cleansing",
        "Sales report automation",
        "Inventory data processing",
        "Survey data formatting",
        "E‑commerce product normalization",
    ],
    "File Automation": [
        "Bulk file renaming",
        "Document format conversion",
        "Automated backups/archiving",
        "Log parsing and analysis",
        "Image/document batch tools",
    ],
    "Report Generation": [
        "Excel report generators",
        "PDF report creation",
        "Dashboard data prep",
        "Email report automation",
        "Scheduled reporting",
    ],
    "Data Integration": [
        "Multi-source merging",
        "API extraction + formatting",
        "Database export processing",
        "ETL pipelines",
        "Data migration utilities",
    ],
    "Business Automation": [
        "Invoice processing",
        "Order fulfillment data",
        "HR data management",
        "Financial reports",
        "Workflow automation",
    ],
}


# -----------------------------
# Styles and Theme
# -----------------------------

THEME_BLUE = colors.Color(22 / 255, 82 / 255, 122 / 255)
THEME_GREEN = colors.Color(24 / 255, 160 / 255, 132 / 255)
THEME_GRAY = colors.Color(90 / 255, 99 / 255, 110 / 255)

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="TitleBig",
        parent=styles["Title"],
        textColor=THEME_BLUE,
        alignment=TA_LEFT,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="Subtitle",
        parent=styles["Normal"],
        fontSize=12,
        textColor=THEME_GRAY,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="H2",
        parent=styles["Heading2"],
        textColor=THEME_BLUE,
        spaceBefore=10,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="H3",
        parent=styles["Heading3"],
        textColor=THEME_GREEN,
        spaceBefore=8,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
    )
)
styles.add(
    ParagraphStyle(
        name="Caption",
        parent=styles["Normal"],
        fontSize=9,
        textColor=THEME_GRAY,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
)


# -----------------------------
# Utilities
# -----------------------------

def find_screenshots(folder: Path, max_count: int = 5) -> List[Path]:
    exts = {".png", ".jpg", ".jpeg", ".webp"}
    if not folder.exists():
        return []
    imgs = [p for p in folder.iterdir() if p.suffix.lower() in exts and p.is_file()]
    imgs.sort()
    return imgs[:max_count]


def compress_image_to_bytes(
    src_path: Path,
    max_width: int = 1100,
    quality: int = 70,
) -> bytes:
    img = PILImage.open(src_path).convert("RGB")
    w, h = img.size
    if w > max_width:
        ratio = max_width / float(w)
        img = img.resize((max_width, int(h * ratio)), PILImage.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", optimize=True, quality=quality)
    return buf.getvalue()


def image_flowable_from_bytes(img_bytes: bytes, width: float) -> Image:
    bio = io.BytesIO(img_bytes)
    img = Image(bio)
    img._restrictSize(width, 8 * cm)  # cap height to keep layout tidy
    return img


def placeholder_box(caption: str, width: float, height: float) -> Flowable:
    class Box(Flowable):
        def __init__(self, w: float, h: float, text: str):
            super().__init__()
            self.w = w
            self.h = h
            self.text = text

        def wrap(self, availWidth, availHeight):
            return self.w, self.h

        def draw(self):
            self.canv.setStrokeColor(THEME_BLUE)
            self.canv.setFillColor(colors.whitesmoke)
            self.canv.rect(0, 0, self.w, self.h, stroke=1, fill=1)
            self.canv.setFillColor(THEME_GRAY)
            self.canv.setFont("Helvetica", 10)
            self.canv.drawCentredString(self.w / 2, self.h / 2 - 5, self.text)

    return Box(width, height, caption)


# -----------------------------
# Page decorations
# -----------------------------

def draw_footer(canv: canvas.Canvas, doc):
    canv.setStrokeColor(THEME_BLUE)
    canv.setFillColor(THEME_BLUE)
    canv.setLineWidth(0.5)
    canv.line(doc.leftMargin, 1.9 * cm, doc.width + doc.leftMargin, 1.9 * cm)

    canv.setFont("Helvetica", 9)
    canv.setFillColor(THEME_GRAY)
    footer_text = f"{GITHUB}    |    {LINKEDIN}"
    canv.drawString(doc.leftMargin, 1.3 * cm, footer_text)

    page_num = f"Page {canv.getPageNumber()}"
    canv.drawRightString(doc.leftMargin + doc.width, 1.3 * cm, page_num)


def first_page(canv: canvas.Canvas, doc):
    # Cover accent bar
    canv.setFillColor(THEME_BLUE)
    canv.rect(0, A4[1] - 3.2 * cm, A4[0], 3.2 * cm, stroke=0, fill=1)

    canv.setFillColor(colors.white)
    canv.setFont("Helvetica-Bold", 22)
    canv.drawString(doc.leftMargin, A4[1] - 2.0 * cm, NAME)

    canv.setFont("Helvetica", 12)
    canv.drawString(doc.leftMargin, A4[1] - 2.7 * cm, TITLE)

    draw_footer(canv, doc)


def later_pages(canv: canvas.Canvas, doc):
    draw_footer(canv, doc)


# -----------------------------
# Document Assembly
# -----------------------------

def tech_stack_table() -> Table:
    data = [("Category", "Tools/Libraries")] + TECH_STACK
    tbl = Table(data, colWidths=[4.2 * cm, 11.3 * cm])
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), THEME_GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9.5),
                ("ALIGN", (0, 0), (-1, 0), "LEFT"),
                ("LINEABOVE", (0, 1), (-1, 1), 0.25, THEME_BLUE),
                ("LINEBELOW", (0, -1), (-1, -1), 0.25, THEME_BLUE),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                ("BOX", (0, 0), (-1, -1), 0.5, THEME_BLUE),
            ]
        )
    )
    return tbl


def stats_table() -> Table:
    data = [(k, v) for k, v in PROJECT_STATS]
    tbl = Table(data, colWidths=[5.8 * cm, 9.7 * cm])
    tbl.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9.5),
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, colors.whitesmoke]),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                ("BOX", (0, 0), (-1, -1), 0.5, THEME_BLUE),
            ]
        )
    )
    return tbl


def numbered_list_paragraphs(items: Iterable[str]) -> List[Paragraph]:
    return [Paragraph(f"{i+1}. {text}", styles["Body"]) for i, text in enumerate(items)]


def skills_sections() -> List[Flowable]:
    flows: List[Flowable] = []
    for group, lines in SKILLS.items():
        flows.append(Paragraph(group, styles["H3"]))
        for t in lines:
            flows.append(Paragraph(f"- {t}", styles["Body"]))
        flows.append(Spacer(1, 6))
    return flows


def similar_projects_sections() -> List[Flowable]:
    flows: List[Flowable] = []
    for group, lines in SIMILAR_PROJECTS.items():
        flows.append(Paragraph(group, styles["H3"]))
        for t in lines:
            flows.append(Paragraph(f"- {t}", styles["Body"]))
        flows.append(Spacer(1, 6))
    return flows


def screenshots_section(screenshot_paths: List[Path], doc_width: float) -> List[Flowable]:
    flows: List[Flowable] = []
    # Captions matching numbered screenshot files (1-5)
    captions = [
        "Code Structure — VS Code showing main script, clean classes, pandas operations",
        "CLI Interface — Interactive menu with colorful prompts and options",
        "Processing in Action — tqdm progress bars showing file processing status",
        "Before/After Data — Messy vs. cleaned CSV comparison side-by-side",
        "Generated Reports — File explorer showing cleaned CSV and TXT report outputs",
    ]

    for i in range(5):
        if i < len(screenshot_paths):
            img_bytes = compress_image_to_bytes(screenshot_paths[i])
            img_flow = image_flowable_from_bytes(img_bytes, width=doc_width)
            flows.append(img_flow)
        else:
            flows.append(placeholder_box("Screenshot placeholder", doc_width, 6 * cm))
        flows.append(Paragraph(captions[i], styles["Caption"]))
        flows.append(Spacer(1, 6))

    return flows


def build_pdf(output_path: Path, screenshots_dir: Optional[Path] = None) -> Path:
    output_path = output_path.resolve()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=2.0 * cm,
        rightMargin=2.0 * cm,
        topMargin=2.2 * cm,
        bottomMargin=2.2 * cm,
        title=f"{PROJECT_NAME} — Portfolio",
        author=NAME,
        subject="Python Automation / Data Processing Portfolio",
    )

    story: List[Flowable] = []

    # Cover Page Content (content is minimal; header bar is drawn in first_page)
    story.append(Spacer(1, 2.8 * cm))
    story.append(Paragraph("Python Automation Developer", styles["Subtitle"]))
    story.append(Paragraph(f"<b>Project:</b> {PROJECT_NAME}", styles["TitleBig"]))
    story.append(Paragraph(f"{PROJECT_TYPE}", styles["Body"]))
    story.append(Spacer(1, 18))
    story.append(Paragraph(f"GitHub: <u>{GITHUB}</u>", styles["Body"]))
    story.append(Paragraph(f"LinkedIn: <u>{LINKEDIN}</u>", styles["Body"]))
    story.append(PageBreak())

    # Technology Stack
    story.append(Paragraph("Technology Stack", styles["H2"]))
    story.append(tech_stack_table())
    story.append(Spacer(1, 12))

    # Project Stats
    story.append(Paragraph("Project Statistics", styles["H2"]))
    story.append(stats_table())
    story.append(Spacer(1, 12))

    # Overview
    story.append(Paragraph("Project Overview", styles["H2"]))
    story.append(Paragraph(PROJECT_OVERVIEW, styles["Body"]))
    story.append(PageBreak())

    # Key Features
    story.append(Paragraph("Key Features", styles["H2"]))
    for p in numbered_list_paragraphs(KEY_FEATURES):
        story.append(p)
    story.append(PageBreak())

    # Screenshots
    story.append(Paragraph("Screenshots", styles["H2"]))
    shots = find_screenshots(screenshots_dir or Path("screenshots"))
    story += screenshots_section(shots, doc_width=doc.width)
    story.append(PageBreak())

    # Skills
    story.append(Paragraph("Skills Demonstrated", styles["H2"]))
    story += skills_sections()
    story.append(PageBreak())

    # Similar Projects
    story.append(Paragraph("Similar Projects I Can Build", styles["H2"]))
    story += similar_projects_sections()

    doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
    return output_path


def ensure_under_size(output_path: Path, max_bytes: int = 5 * 1024 * 1024) -> bool:
    try:
        return output_path.stat().st_size <= max_bytes
    except Exception:
        return False


def main(argv: List[str]) -> int:
    # Args: [--screenshots-dir <path>] [--output <file.pdf>]
    out = Path("portfolio_csv_automation.pdf")
    shots_dir: Optional[Path] = None

    i = 0
    while i < len(argv):
        if argv[i] == "--screenshots-dir" and i + 1 < len(argv):
            shots_dir = Path(argv[i + 1])
            i += 2
        elif argv[i] == "--output" and i + 1 < len(argv):
            out = Path(argv[i + 1])
            i += 2
        else:
            i += 1

    # Try generating; if bigger than 5MB, just warn (images already compressed)
    pdf_path = build_pdf(out, shots_dir)
    if not ensure_under_size(pdf_path):
        print(
            "Warning: PDF exceeds 5MB. Consider resizing screenshots or using lower JPEG quality.",
            file=sys.stderr,
        )
    print(f"Wrote {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
