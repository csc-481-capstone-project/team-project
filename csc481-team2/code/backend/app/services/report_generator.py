from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def create_experiment_report(
    output_path: str | Path,
    carrier_type: str,
    operation: str,
    result: str,
    detection_result: dict[str, float | int | str],
) -> Path:
    """Create a PDF summary for one steganography experiment."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    document = SimpleDocTemplate(
        str(output_file),
        pagesize=letter,
        rightMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    story = [
        Paragraph("Steganography Experiment Report", styles["Title"]),
        Spacer(1, 0.25 * inch),
    ]

    report_rows = [
        ["Field", "Result"],
        ["Carrier Type", carrier_type],
        ["Operation", operation],
        [
            "Experiment Time",
            datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        ],
        ["Result", result],
        ["Detection Score", str(detection_result.get("balance_score", "N/A"))],
        ["Suspicion Level", str(detection_result.get("suspicion", "N/A"))],
        [
            "Bits Analyzed",
            str(detection_result.get("total_bits_analyzed", "N/A")),
        ],
    ]

    report_table = Table(
        report_rows,
        colWidths=[2.0 * inch, 4.5 * inch],
    )

    report_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    story.append(report_table)
    document.build(story)

    return output_file