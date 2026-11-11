"""
Generates docs/literature_review.pdf from docs/literature_review.md using ReportLab.
Uses high-contrast academic styling matching university seminar standards.
"""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print total page count."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))

        # Running header on pages 2+
        if self._pageNumber > 1:
            self.drawString(
                54, 750,
                "MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework"
            )
            self.drawRightString(
                612 - 54, 750,
                "Technical Seminar Literature Review"
            )
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(54, 744, 612 - 54, 744)

        # Running footer on all pages
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.drawString(54, 36, "MCA Technical Seminar Review — Confidential & Academic Submission")
        self.drawRightString(612 - 54, 36, page_str)
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(54, 46, 612 - 54, 46)

        self.restoreState()


def format_inline_markdown(text: str) -> str:
    """Convert common markdown and math formatting to ReportLab XML tags."""
    # Convert math expressions to clean text representations
    text = text.replace(r'$A_1 \rightarrow A_2 \rightarrow \dots \rightarrow A_n$', 'A<sub>1</sub> &rarr; A<sub>2</sub> &rarr; ... &rarr; A<sub>n</sub>')
    text = text.replace(r'$A_1, A_2, \dots, A_k$', 'A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>k</sub>')
    text = text.replace(r'$A_c \leftrightarrow A_i$', 'A<sub>c</sub> &harr; A<sub>i</sub>')
    text = text.replace(r'$A_i$', 'A<sub>i</sub>')
    text = text.replace(r'$A_{i+1}$', 'A<sub>i+1</sub>')
    text = text.replace(r'$A_c$', 'A<sub>c</sub>')
    text = text.replace(r'$G = (V, E)$', '<i>G</i> = (<i>V</i>, <i>E</i>)')
    text = text.replace(r'$V$', '<i>V</i>')
    text = text.replace(r'$E$', '<i>E</i>')
    text = text.replace(r'$', '')  # Remove any remaining raw math signs

    # Convert bold-italic, bold, italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = text.replace('—', '&mdash;').replace('–', '&ndash;')
    text = text.replace('&', '&amp;') if '&amp;' not in text else text
    # Clean up double escapes if any
    text = text.replace('&amp;mdash;', '&mdash;').replace('&amp;ndash;', '&ndash;')
    text = text.replace('&amp;rarr;', '&rarr;').replace('&amp;harr;', '&harr;')

    return text


def build_pdf(md_path: str, pdf_path: str):
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    usable_width = 612 - 108  # 504 pt

    styles = getSampleStyleSheet()

    # Custom palette
    C_PRIMARY = colors.HexColor("#1A365D")    # Dark navy
    C_SECONDARY = colors.HexColor("#2B6CB0")  # Blue
    C_TEXT = colors.HexColor("#2D3748")       # Charcoal
    C_MUTED = colors.HexColor("#4A5568")      # Medium slate
    C_ACCENT = colors.HexColor("#0D9488")     # Teal

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=C_PRIMARY,
        spaceAfter=4,
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=C_MUTED,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=C_PRIMARY,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=C_SECONDARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=C_TEXT,
        alignment=4,  # Justified
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13,
        textColor=C_TEXT,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=3
    )

    ref_style = ParagraphStyle(
        'Ref_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_TEXT,
        leftIndent=24,
        firstLineIndent=-24,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=C_TEXT,
        alignment=0
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=C_PRIMARY,
        alignment=0
    )

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    story = []

    i = 0
    in_references = False

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # Document Title
        if line.startswith('# '):
            title_text = line[2:].strip()
            story.append(Paragraph(title_text, title_style))
            story.append(Paragraph("Technical Seminar Literature Review & Systematic Framework Survey", subtitle_style))
            story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=2, spaceAfter=8))
            i += 1
            continue

        # Heading 1 (e.g. ## 1. Introduction)
        if line.startswith('## '):
            heading_text = line[3:].strip()
            if heading_text.lower() == 'references':
                in_references = True
            story.append(Paragraph(heading_text, h1_style))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CBD5E0"), spaceBefore=2, spaceAfter=6))
            i += 1
            continue

        # Heading 2 (e.g. ### 6.1 Single-Agent)
        if line.startswith('### '):
            subheading_text = line[4:].strip()
            story.append(Paragraph(subheading_text, h2_style))
            i += 1
            continue

        # Markdown Table
        if line.startswith('|') and line.endswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            # Parse markdown table
            raw_headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
            # Skip separator line (table_lines[1])
            raw_rows = []
            for r in table_lines[2:]:
                raw_rows.append([c.strip() for c in r.split('|')[1:-1]])

            num_cols = len(raw_headers)

            # Determine column widths based on table structure
            if num_cols == 7 and 'Research' in raw_headers[0]:  # Table 1
                col_widths = [75, 28, 68, 72, 115, 72, 74]
            elif num_cols == 5 and 'Architecture' in raw_headers[0]:  # Table 2
                col_widths = [74, 80, 125, 140, 85]
            elif num_cols == 7 and 'Evaluation Framework' in raw_headers[0]:  # Table 3
                col_widths = [84, 44, 44, 46, 42, 178, 66]
            else:
                w = usable_width / num_cols
                col_widths = [w] * num_cols

            table_data = []
            # Header row
            hdr_cells = [Paragraph(format_inline_markdown(h), table_header_style) for h in raw_headers]
            table_data.append(hdr_cells)

            # Body rows
            for row in raw_rows:
                cells = []
                for idx, cell in enumerate(row):
                    style_to_use = table_cell_bold if idx == 0 else table_cell_style
                    cells.append(Paragraph(format_inline_markdown(cell), style_to_use))
                table_data.append(cells)

            tbl = Table(table_data, colWidths=col_widths, repeatRows=1)
            tbl.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), C_PRIMARY),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
                ('TOPPADDING', (0, 0), (-1, 0), 4),
                ('LEFTPADDING', (0, 0), (-1, -1), 3),
                ('RIGHTPADDING', (0, 0), (-1, -1), 3),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
                ('TOPPADDING', (0, 1), (-1, -1), 3),
            ]))
            story.append(Spacer(1, 4))
            story.append(tbl)
            story.append(Spacer(1, 6))
            continue

        # In References section
        if in_references and re.match(r'^\[\d+\]', line):
            formatted_ref = format_inline_markdown(line)
            story.append(Paragraph(formatted_ref, ref_style))
            i += 1
            continue

        # Bullet list items (- or *)
        if line.startswith('- ') or line.startswith('* '):
            item_text = line[2:].strip()
            bullet_p = Paragraph(f"&bull; {format_inline_markdown(item_text)}", bullet_style)
            story.append(bullet_p)
            i += 1
            continue

        # Numbered list items (1. , 2. )
        num_match = re.match(r'^(\d+)\.\s+(.*)', line)
        if num_match:
            num = num_match.group(1)
            item_text = num_match.group(2)
            num_p = Paragraph(f"<b>{num}.</b> {format_inline_markdown(item_text)}", bullet_style)
            story.append(num_p)
            i += 1
            continue

        # Standard paragraph
        p_text = format_inline_markdown(line)
        story.append(Paragraph(p_text, body_style))
        i += 1

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully compiled {pdf_path}")

if __name__ == '__main__':
    md_file = os.path.join("docs", "literature_review.md")
    pdf_file = os.path.join("docs", "literature_review.pdf")
    build_pdf(md_file, pdf_file)

