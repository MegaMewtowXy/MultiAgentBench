"""
scripts/generate_full_report.py
Master script to assemble the complete MCA Technical Seminar Report in DOCX format:
seminar_submission/Report/Technical_Seminar_Report.docx
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

def build_full_report():
    doc = Document()

    # Configure Margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True
        
        # Configure Header & Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("MCA Technical Seminar Report | MultiAgentTopologyEval | VJTI Mumbai")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(148, 163, 184) # Slate-400

        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Page ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(9.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)
        # Add dynamic page number field
        fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
        fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        frun._r.append(fldChar1)
        frun._r.append(instrText)
        frun._r.append(fldChar2)
        frun._r.append(fldChar3)
        
        frun2 = fp.add_run(" of ")
        frun2.font.name = "Calibri"
        frun2.font.size = Pt(9.5)
        frun2.font.color.rgb = RGBColor(100, 116, 139)
        fldChar4 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instrText2 = parse_xml(r'<w:instrText %s xml:space="preserve"> NUMPAGES </w:instrText>' % nsdecls('w'))
        fldChar5 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fldChar6 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        frun2._r.append(fldChar4)
        frun2._r.append(instrText2)
        frun2._r.append(fldChar5)
        frun2._r.append(fldChar6)

    # Color Palette
    C_NAVY = RGBColor(26, 54, 93)     # #1A365D - Deep Academic Navy
    C_TEAL = RGBColor(13, 148, 136)   # #0D9488 - Accent Teal
    C_DARK = RGBColor(30, 41, 59)     # #1E293B - Off-black Charcoal
    C_MUTED = RGBColor(100, 116, 139) # #64748B - Muted Slate

    figures_dir = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Figures")

    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def style_table(table, widths, headers, data, header_bg="1A365D", alt_row_bg="F8FAFC"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Header row is row 0
        header_row = table.rows[0]
        trPr = header_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        for c_idx, heading_text in enumerate(headers):
            cell = header_row.cells[c_idx]
            if c_idx < len(widths):
                cell.width = widths[c_idx]
            set_cell_background(cell, header_bg)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            tcPr = cell._tc.get_or_add_tcPr()
            tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
            tcPr.append(tcMar)
            
            p = cell.paragraphs[0]
            p.text = heading_text
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            for run in p.runs:
                run.font.bold = True
                run.font.name = "Calibri"
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(255, 255, 255)
        
        # Data rows
        for r_idx, row_values in enumerate(data):
            row = table.add_row()
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            
            bg_color = "FFFFFF" if r_idx % 2 == 0 else alt_row_bg
            for c_idx, val in enumerate(row_values):
                cell = row.cells[c_idx]
                if c_idx < len(widths):
                    cell.width = widths[c_idx]
                set_cell_background(cell, bg_color)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                
                tcPr = cell._tc.get_or_add_tcPr()
                tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="100" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:right w:w="140" w:type="dxa"/></w:tcMar>')
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
                    run.font.name = "Calibri"
                    run.font.size = Pt(9.0)
                    run.font.color.rgb = C_DARK
        
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(6)

    def add_chapter_heading(chapter_num, title):
        doc.add_page_break()
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(28)
        p.paragraph_format.space_after = Pt(14)
        p.paragraph_format.keep_with_next = True
        
        r_num = p.add_run(f"CHAPTER {chapter_num}\n")
        r_num.font.name = "Calibri"
        r_num.font.size = Pt(13)
        r_num.font.bold = True
        r_num.font.color.rgb = C_TEAL
        
        r_title = p.add_run(title.upper())
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(19)
        r_title.font.bold = True
        r_title.font.color.rgb = C_NAVY

    def add_sec(num, title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{num}  {title}")
        r.font.name = "Calibri"
        r.font.size = Pt(13.5)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

    def add_subsec(num, title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{num}  {title}")
        r.font.name = "Calibri"
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = C_TEAL

    def add_p(text, bold=False, italic=False, **kwargs):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5.5)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.font.color.rgb = C_DARK
        if bold:
            r.font.bold = True
        if italic:
            r.font.italic = True
        return p

    def add_bullet(text, bold=False, italic=False, **kwargs):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.font.color.rgb = C_DARK
        if bold:
            r.font.bold = True
        if italic:
            r.font.italic = True
        return p

    def add_callout(title, text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        set_cell_background(cell, "F0FDF4") # subtle light green/slate tint
        # Left border highlight
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="0D9488"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
        tcPr.append(tcBorders)
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(f"Takeaway / Key Insight: {title}\n")
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(10.5)
        r_title.font.bold = True
        r_title.font.color.rgb = C_TEAL
        
        r_text = p.add_run(text)
        r_text.font.name = "Calibri"
        r_text.font.size = Pt(10)
        r_text.font.color.rgb = C_DARK
        
        # Add tiny spacing after table
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(4)

    def add_fig(filename, caption):
        fig_path = os.path.join(figures_dir, filename)
        if os.path.exists(fig_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(fig_path, width=Inches(5.6))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(9.0)
            r_cap.font.italic = True
            r_cap.font.color.rgb = C_MUTED
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
        'C_NAVY': C_NAVY,
        'C_TEAL': C_TEAL,
        'C_DARK': C_DARK,
        'C_MUTED': C_MUTED
    }

    print("Step 1: Adding Preliminary Pages...")
    add_preliminary_pages(doc, helpers)

    print("Step 2: Adding Chapter 1 (Introduction)...")
    add_chapter_1(doc, helpers)

    print("Step 3: Adding Chapter 2 (Problem Statement)...")
    add_chapter_2(doc, helpers)

    print("Step 4: Adding Chapter 3 (Theoretical Foundations)...")
    add_chapter_3(doc, helpers)

    print("Step 5: Adding Chapter 4 (Literature Review)...")
    add_chapter_4(doc, helpers)

    print("Step 6: Adding Chapter 5 (Taxonomy & Comparative Analysis)...")
    add_chapter_5(doc, helpers)

    print("Step 7: Adding Chapter 6 (Research Gaps & Contributions)...")
    add_chapter_6(doc, helpers)

    print("Step 8: Adding Chapter 7 (Proposed Framework)...")
    add_chapter_7(doc, helpers)

    print("Step 9: Adding Chapter 8 (Multi-Agent Topologies)...")
    add_chapter_8(doc, helpers)

    print("Step 10: Adding Chapter 9 (Metrics & Evaluation Engine)...")
    add_chapter_9(doc, helpers)

    print("Step 11: Adding Chapter 10 (Experimental Methodology)...")
    add_chapter_10(doc, helpers)

    print("Step 12: Adding Chapter 11 (Implementation & Testing)...")
    add_chapter_11(doc, helpers)

    print("Step 13: Adding Chapter 12 (Empirical Results & Analysis)...")
    add_chapter_12(doc, helpers)

    print("Step 14: Adding Chapter 13 (Limitations & Threats to Validity)...")
    add_chapter_13(doc, helpers)

    print("Step 15: Adding Chapter 14 (Conclusion & Future Work)...")
    add_chapter_14(doc, helpers)

    print("Step 16: Adding References & Appendices...")
    add_references_and_appendices(doc, helpers)

    out_path = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Report", "Technical_Seminar_Report.docx")
    doc.save(out_path)
    print(f"\n[SUCCESS] Master Technical Seminar Report saved to: {out_path}")
    print(f"File size: {os.path.getsize(out_path):,} bytes")

if __name__ == "__main__":
    build_full_report()
