"""
scripts/generate_formatted_report.py
Master script to assemble the professionally formatted MCA Technical Seminar Report:
seminar_submission/Report/Technical_Seminar_Report_Formatted.docx

Formatting Specifications:
- Paper Size: A4 (210mm x 297mm, 8.27in x 11.69in)
- Margins: Left 1.25" (for binding), Right 1.0", Top 1.0", Bottom 1.0"
- Printable Text Width: 6.02" (all tables & figures fit within 6.0")
- Typography: Times New Roman throughout
- Body Text: 12 pt, 1.5 line spacing, Fully Justified, 6 pt space after
- Chapter Headings: 18 pt Bold, Uppercase, 24 pt before, 12 pt after, keep_with_next
- Section Headings: 14 pt Bold, 14 pt before, 4 pt after, keep_with_next
- Subsection Headings: 12 pt Bold, 10 pt before, 3 pt after, keep_with_next
- Bullet / List: 12 pt, 1.5 line spacing, 3 pt space after
- Figures: Centered, width 5.9", 300 DPI high-contrast images, 10.5 pt italic caption
- Tables: Centered, max width 6.0", tblHeader, cantSplit, cell padding, alternating rows
- Front Matter: Section 1 with Roman numerals (i, ii, iii...), unnumbered title page
- Main Body: Section 2 with Arabic numerals (1, 2, 3...) starting at 1, running header
- References: 44 peer-reviewed citations with hanging indentation
- Student Name: Kshitij Kejriwal (Department of Computer Applications, VJTI Mumbai)
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Add report_sections to path
sys.path.append(os.path.join(os.path.dirname(__file__), "report_sections"))

from preliminary import add_preliminary_pages
from ch1_intro import add_chapter_1
from ch2_problem import add_chapter_2
from ch3_foundations import add_chapter_3
from ch4_literature import add_chapter_4
from ch5_comparison import add_chapter_5
from ch6_gap import add_chapter_6
from ch7_framework import add_chapter_7
from ch8_topologies import add_chapter_8
from ch9_metrics import add_chapter_9
from ch10_methodology import add_chapter_10
from ch11_implementation import add_chapter_11
from ch12_results import add_chapter_12
from ch13_limitations import add_chapter_13
from ch14_conclusion import add_chapter_14
from references_appendices import add_references_and_appendices


def set_run_font(run, font_name="Times New Roman", size_pt=None, bold=None, italic=None, color_rgb=None):
    """Strictly set font properties including OpenXML rFonts."""
    run.font.name = font_name
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    if color_rgb is not None:
        run.font.color.rgb = color_rgb
    
    # Ensure XML rFonts is also set for full compatibility
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)


def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def build_formatted_report(out_docx_path=None):
    doc = Document()

    # ----------------------------------------------------
    # Base Style Configuration
    # ----------------------------------------------------
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = RGBColor(30, 41, 59) # Slate-800
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    style_normal.paragraph_format.space_before = Pt(0)
    style_normal.paragraph_format.space_after = Pt(6)

    # Color Palette
    C_NAVY = RGBColor(26, 54, 93)     # #1A365D - Deep Academic Navy
    C_TEAL = RGBColor(13, 148, 136)   # #0D9488 - Accent Teal
    C_DARK = RGBColor(30, 41, 59)     # #1E293B - Off-black Charcoal
    C_MUTED = RGBColor(100, 116, 139) # #64748B - Muted Slate

    figures_dir = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Figures")

    # ----------------------------------------------------
    # SECTION 1: Preliminary Pages (Front Matter)
    # ----------------------------------------------------
    sec_front = doc.sections[0]
    sec_front.page_width = Inches(8.27)
    sec_front.page_height = Inches(11.69)
    sec_front.top_margin = Inches(1.0)
    sec_front.bottom_margin = Inches(1.0)
    sec_front.left_margin = Inches(1.25)
    sec_front.right_margin = Inches(1.0)
    sec_front.different_first_page_header_footer = True

    # Section 1 Numbering Format: lowerRoman (i, ii, iii...)
    sectPr1 = sec_front._sectPr
    pgNumType1 = sectPr1.find(qn('w:pgNumType'))
    if pgNumType1 is None:
        pgNumType1 = OxmlElement('w:pgNumType')
        sectPr1.append(pgNumType1)
    pgNumType1.set(qn('w:fmt'), 'lowerRoman')
    pgNumType1.set(qn('w:start'), '1')

    # Front matter footer (for pages 2+ of preliminary matter)
    # The title page is page 1 and uses the empty first_page_footer
    fp_front = sec_front.footer.paragraphs[0]
    fp_front.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp_front.paragraph_format.space_before = Pt(0)
    fp_front.paragraph_format.space_after = Pt(0)
    frun_f = fp_front.add_run()
    set_run_font(frun_f, font_name="Times New Roman", size_pt=9.5, color_rgb=C_MUTED)
    fld1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    ins1 = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fld2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fld3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    frun_f._r.append(fld1)
    frun_f._r.append(ins1)
    frun_f._r.append(fld2)
    frun_f._r.append(fld3)

    # ----------------------------------------------------
    # Helper Functions for Academic Formatting
    # ----------------------------------------------------
    def style_table(table, widths, headers, data, header_bg="1A365D", alt_row_bg="F8FAFC"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Max printable width is 6.0 inches
        max_total_in = 6.0
        orig_total_in = sum([w.inches for w in widths]) if widths else 6.0
        
        # Scale widths if necessary
        scale = 1.0
        if orig_total_in > max_total_in:
            scale = max_total_in / orig_total_in
        
        scaled_widths = [Inches(w.inches * scale) for w in widths]
        
        # Determine appropriate font size based on column count
        num_cols = len(headers)
        if num_cols >= 8:
            hdr_size = 8.5
            cell_size = 8.0
        elif num_cols >= 6:
            hdr_size = 9.0
            cell_size = 8.5
        else:
            hdr_size = 9.5
            cell_size = 9.0

        # Header row (row 0)
        header_row = table.rows[0]
        trPr = header_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        for c_idx, heading_text in enumerate(headers):
            cell = header_row.cells[c_idx]
            if c_idx < len(scaled_widths):
                cell.width = scaled_widths[c_idx]
            set_cell_background(cell, header_bg)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            tcPr = cell._tc.get_or_add_tcPr()
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')
            tcPr.append(tcMar)
            
            p = cell.paragraphs[0]
            p.text = heading_text
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.05
            for run in p.runs:
                set_run_font(run, font_name="Times New Roman", size_pt=hdr_size, bold=True, color_rgb=RGBColor(255, 255, 255))
        
        # Data rows
        for r_idx, row_values in enumerate(data):
            row = table.add_row()
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            
            bg_color = "FFFFFF" if r_idx % 2 == 0 else alt_row_bg
            for c_idx, val in enumerate(row_values):
                cell = row.cells[c_idx]
                if c_idx < len(scaled_widths):
                    cell.width = scaled_widths[c_idx]
                set_cell_background(cell, bg_color)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                
                tcPr = cell._tc.get_or_add_tcPr()
                tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="90" w:type="dxa"/><w:bottom w:w="90" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')
                tcPr.append(tcMar)
                
                p = cell.paragraphs[0]
                p.text = str(val)
                p.paragraph_format.space_before = Pt(1)
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.line_spacing = 1.1
                if len(str(val)) <= 15:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    set_run_font(run, font_name="Times New Roman", size_pt=cell_size, color_rgb=C_DARK)
        
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(6)

    def add_chapter_heading(chapter_num, title):
        # Do not add page break for Chapter 1 as it begins immediately after section break
        if chapter_num > 1:
            doc.add_page_break()
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(24)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.keep_with_next = True
        
        r_num = p.add_run(f"CHAPTER {chapter_num}\n")
        set_run_font(r_num, font_name="Times New Roman", size_pt=13, bold=True, color_rgb=C_TEAL)
        
        r_title = p.add_run(title.upper())
        set_run_font(r_title, font_name="Times New Roman", size_pt=18, bold=True, color_rgb=C_NAVY)

    def add_sec(num, title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        prefix = f"{num}  " if num else ""
        r = p.add_run(f"{prefix}{title}")
        set_run_font(r, font_name="Times New Roman", size_pt=14, bold=True, color_rgb=C_NAVY)

    def add_subsec(num, title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        prefix = f"{num}  " if num else ""
        r = p.add_run(f"{prefix}{title}")
        set_run_font(r, font_name="Times New Roman", size_pt=12, bold=True, color_rgb=C_TEAL)

    def add_p(text, bold=False, italic=False, **kwargs):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        set_run_font(r, font_name="Times New Roman", size_pt=12, bold=bold, italic=italic, color_rgb=C_DARK)
        return p

    def add_bullet(text, bold=False, italic=False, **kwargs):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        set_run_font(r, font_name="Times New Roman", size_pt=12, bold=bold, italic=italic, color_rgb=C_DARK)
        return p

    def add_callout(title, text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(5.9)
        set_cell_background(cell, "F0FDF4") # Subtle light green/slate tint
        
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="0D9488"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(tcBorders)
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        r_title = p.add_run(f"Takeaway / Key Insight: {title}\n")
        set_run_font(r_title, font_name="Times New Roman", size_pt=11, bold=True, color_rgb=C_TEAL)
        
        r_text = p.add_run(text)
        set_run_font(r_text, font_name="Times New Roman", size_pt=10.5, color_rgb=C_DARK)
        
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(4)

    def add_fig(filename, caption):
        fig_path = os.path.join(figures_dir, filename)
        if os.path.exists(fig_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(12)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(fig_path, width=Inches(5.9))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(caption)
            set_run_font(r_cap, font_name="Times New Roman", size_pt=10.5, italic=True, color_rgb=C_MUTED)
        else:
            p_err = doc.add_paragraph(f"[Figure '{filename}' not found at {fig_path}]")
            p_err.paragraph_format.space_after = Pt(8)

    helpers = {
        'add_chapter_heading': add_chapter_heading,
        'add_sec': add_sec,
        'add_subsec': add_subsec,
        'add_p': add_p,
        'add_bullet': add_bullet,
        'add_callout': add_callout,
        'add_fig': add_fig,
        'set_cell_background': set_cell_background,
        'style_table': style_table,
        'set_run_font': set_run_font,
        'FONT_NAME': 'Times New Roman',
        'C_NAVY': C_NAVY,
        'C_TEAL': C_TEAL,
        'C_DARK': C_DARK,
        'C_MUTED': C_MUTED
    }

    # ----------------------------------------------------
    # Step 1: Render Front Matter (Section 1)
    # ----------------------------------------------------
    print("[1/17] Adding Preliminary Pages (Front Matter)...")
    add_preliminary_pages(doc, helpers)

    # ----------------------------------------------------
    # SECTION 2: Main Body & Appendices
    # ----------------------------------------------------
    print("\n[Section Break] Transitioning to Main Body (Section 2)...")
    sec_body = doc.add_section()
    sec_body.page_width = Inches(8.27)
    sec_body.page_height = Inches(11.69)
    sec_body.top_margin = Inches(1.0)
    sec_body.bottom_margin = Inches(1.0)
    sec_body.left_margin = Inches(1.25)
    sec_body.right_margin = Inches(1.0)
    sec_body.different_first_page_header_footer = False

    # Unlink headers & footers from Section 1
    sec_body.header.is_linked_to_previous = False
    sec_body.footer.is_linked_to_previous = False

    # Section 2 Numbering Format: decimal (1, 2, 3...) starting at 1
    sectPr2 = sec_body._sectPr
    pgNumType2 = sectPr2.find(qn('w:pgNumType'))
    if pgNumType2 is None:
        pgNumType2 = OxmlElement('w:pgNumType')
        sectPr2.append(pgNumType2)
    pgNumType2.set(qn('w:fmt'), 'decimal')
    pgNumType2.set(qn('w:start'), '1')

    # Main Body Running Header
    hp_body = sec_body.header.paragraphs[0]
    hp_body.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp_body.paragraph_format.space_after = Pt(0)
    hrun_b = hp_body.add_run("MCA Technical Seminar Report | MultiAgentTopologyEval | VJTI Mumbai")
    set_run_font(hrun_b, font_name="Times New Roman", size_pt=8.5, color_rgb=RGBColor(148, 163, 184))

    # Main Body Running Footer: "Page X"
    fp_body = sec_body.footer.paragraphs[0]
    fp_body.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp_body.paragraph_format.space_before = Pt(0)
    fp_body.paragraph_format.space_after = Pt(0)
    frun_b1 = fp_body.add_run("Page ")
    set_run_font(frun_b1, font_name="Times New Roman", size_pt=9.5, color_rgb=C_MUTED)
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    frun_b1._r.append(fldChar1)
    frun_b1._r.append(instrText)
    frun_b1._r.append(fldChar2)
    frun_b1._r.append(fldChar3)

    # ----------------------------------------------------
    # Render Chapters 1 to 14
    # ----------------------------------------------------
    print("[2/17] Adding Chapter 1 (Introduction)...")
    add_chapter_1(doc, helpers)

    print("[3/17] Adding Chapter 2 (Problem Statement)...")
    add_chapter_2(doc, helpers)

    print("[4/17] Adding Chapter 3 (Theoretical Foundations)...")
    add_chapter_3(doc, helpers)

    print("[5/17] Adding Chapter 4 (Literature Review)...")
    add_chapter_4(doc, helpers)

    print("[6/17] Adding Chapter 5 (Taxonomy & Comparative Analysis)...")
    add_chapter_5(doc, helpers)

    print("[7/17] Adding Chapter 6 (Research Gaps & Contributions)...")
    add_chapter_6(doc, helpers)

    print("[8/17] Adding Chapter 7 (Proposed Framework)...")
    add_chapter_7(doc, helpers)

    print("[9/17] Adding Chapter 8 (Multi-Agent Topologies)...")
    add_chapter_8(doc, helpers)

    print("[10/17] Adding Chapter 9 (Metrics & Evaluation Engine)...")
    add_chapter_9(doc, helpers)

    print("[11/17] Adding Chapter 10 (Experimental Methodology)...")
    add_chapter_10(doc, helpers)

    print("[12/17] Adding Chapter 11 (Implementation & Testing)...")
    add_chapter_11(doc, helpers)

    print("[13/17] Adding Chapter 12 (Empirical Results & Analysis)...")
    add_chapter_12(doc, helpers)

    print("[14/17] Adding Chapter 13 (Limitations & Threats to Validity)...")
    add_chapter_13(doc, helpers)

    print("[15/17] Adding Chapter 14 (Conclusion & Future Work)...")
    add_chapter_14(doc, helpers)

    print("[16/17] Adding References (44 Peer-Reviewed) & Appendices A, B, C...")
    add_references_and_appendices(doc, helpers)

    # ----------------------------------------------------
    # Global Verification Pass: Enforce Times New Roman Everywhere
    # ----------------------------------------------------
    print("[17/17] Running Global Typography Enforcement Pass...")
    all_runs_count = 0
    non_tnr_fixed = 0
    
    def process_paragraph(p):
        nonlocal all_runs_count, non_tnr_fixed
        for run in p.runs:
            all_runs_count += 1
            if run.font.name != "Times New Roman":
                run.font.name = "Times New Roman"
                non_tnr_fixed += 1
            rPr = run._r.get_or_add_rPr()
            rFonts = rPr.find(qn('w:rFonts'))
            if rFonts is None:
                rFonts = OxmlElement('w:rFonts')
                rPr.append(rFonts)
            rFonts.set(qn('w:ascii'), 'Times New Roman')
            rFonts.set(qn('w:hAnsi'), 'Times New Roman')
            rFonts.set(qn('w:cs'), 'Times New Roman')

    # Main paragraphs
    for p in doc.paragraphs:
        process_paragraph(p)
    
    # Table paragraphs
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    process_paragraph(p)
                    
    # Header / footer paragraphs
    for s in doc.sections:
        for p in s.header.paragraphs:
            process_paragraph(p)
        for p in s.footer.paragraphs:
            process_paragraph(p)

    print(f"Total runs inspected: {all_runs_count}, Non-TNR runs unified: {non_tnr_fixed}")

    # ----------------------------------------------------
    # Save Formatted Document
    # ----------------------------------------------------
    if out_docx_path is None:
        out_docx_path = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Report", "Technical_Seminar_Report_Formatted.docx")
    
    doc.save(out_docx_path)
    print(f"\n[SUCCESS] Professionally formatted DOCX saved to:\n  {out_docx_path}")
    print(f"File size: {os.path.getsize(out_docx_path):,} bytes")
    return out_docx_path


if __name__ == "__main__":
    build_formatted_report()

