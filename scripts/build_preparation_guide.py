"""
scripts/build_preparation_guide.py
Master script to assemble the complete Seminar Preparation & Viva Voce Master Guide:
seminar_submission/Preparation/SEMINAR_PREPARATION_GUIDE.docx
and automatically convert to PDF.
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.path.append(os.path.join(os.path.dirname(__file__), "prep_sections"))

from sec_a_first_principles import add_section_a
from sec_b_models_working import add_section_b
from sec_c_agent_frameworks import add_section_c
from sec_d_topologies import add_section_d
from sec_e_literature_notes import add_section_e
from sec_f_project_implementation import add_section_f
from sec_g_viva_questions import add_section_g
from sec_h_presentation_defense import add_section_h

def build_prep_guide():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.different_first_page_header_footer = True

        # Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("MCA Technical Seminar | Master Preparation & Viva Guide | VJTI Mumbai")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(148, 163, 184)

        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Page ")
        frun.font.name = "Calibri"
        frun.font.size = Pt(9.5)
        frun.font.color.rgb = RGBColor(100, 116, 139)
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

    C_NAVY = RGBColor(26, 54, 93)     # #1A365D
    C_TEAL = RGBColor(13, 148, 136)   # #0D9488
    C_DARK = RGBColor(30, 41, 59)     # #1E293B
    C_MUTED = RGBColor(100, 116, 139) # #64748B

    def set_cell_background(cell, hex_color):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        tcPr.append(shd)

    def style_table(table, widths, headers, data, header_bg="1A365D", alt_row_bg="F8FAFC"):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
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

    def add_main_sec(sec_num, title):
        doc.add_page_break()
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(24)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.keep_with_next = True

        r_num = p.add_run(f"{sec_num}\n")
        r_num.font.name = "Calibri"
        r_num.font.size = Pt(13)
        r_num.font.bold = True
        r_num.font.color.rgb = C_TEAL

        r_title = p.add_run(title.upper())
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(18)
        r_title.font.bold = True
        r_title.font.color.rgb = C_NAVY

    def add_sub_sec(num, title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{num}  {title}")
        r.font.name = "Calibri"
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = C_NAVY

    def add_p(text, bold=False, italic=False, **kwargs):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(5)
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
        set_cell_background(cell, "F0FDF4")
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

        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(4)

    helpers = {
        'add_main_sec': add_main_sec,
        'add_sub_sec': add_sub_sec,
        'add_p': add_p,
        'add_bullet': add_bullet,
        'add_callout': add_callout,
        'style_table': style_table,
        'C_NAVY': C_NAVY,
        'C_TEAL': C_TEAL,
        'C_DARK': C_DARK,
        'C_MUTED': C_MUTED
    }

    # ----------------------------------------------------
    # COVER PAGE
    # ----------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(30)
    p_inst.paragraph_format.space_after = Pt(4)
    r_inst = p_inst.add_run("VEERMATA JIJABAI TECHNOLOGICAL INSTITUTE (VJTI)\n")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(15)
    r_inst.font.bold = True
    r_inst.font.color.rgb = C_NAVY

    r_dept = p_inst.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\nMatunga, Mumbai – 400019\n")
    r_dept.font.name = "Calibri"
    r_dept.font.size = Pt(11)
    r_dept.font.color.rgb = C_MUTED

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(40)
    p_title.paragraph_format.space_after = Pt(10)
    r_t1 = p_title.add_run("MASTER TECHNICAL SEMINAR PREPARATION GUIDE\nAND VIVA VOCE QUESTION BANK\n")
    r_t1.font.name = "Calibri"
    r_t1.font.size = Pt(20)
    r_t1.font.bold = True
    r_t1.font.color.rgb = C_NAVY

    r_sub = p_title.add_run("MultiAgentTopologyEval: A Multi-Agent LLM Architecture Evaluation Framework\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(13)
    r_sub.font.bold = True
    r_sub.font.color.rgb = C_TEAL

    r_desc = p_title.add_run("First-Principles Theory, Step-by-Step Model Working, Agent Topologies, and 100+ Rigorous Viva Questions with Full Technical Answers\n")
    r_desc.font.name = "Calibri"
    r_desc.font.size = Pt(10.5)
    r_desc.font.italic = True
    r_desc.font.color.rgb = C_MUTED

    p_cand = doc.add_paragraph()
    p_cand.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cand.paragraph_format.space_before = Pt(50)
    p_cand.paragraph_format.space_after = Pt(4)
    r_cand = p_cand.add_run("Prepared by:\nKshitij Kejriwal\nDepartment of Computer Applications\nVeermata Jijabai Technological Institute (VJTI)\nMumbai, India\nAcademic Year: 2025–2026\n")
    r_cand.font.name = "Calibri"
    r_cand.font.size = Pt(11)
    r_cand.font.bold = True
    r_cand.font.color.rgb = C_DARK

    # Table of Contents Overview
    p_toc_head = doc.add_paragraph()
    p_toc_head.paragraph_format.space_before = Pt(40)
    p_toc_head.paragraph_format.space_after = Pt(8)
    r_th = p_toc_head.add_run("GUIDE STRUCTURE & SYLLABUS BREAKDOWN")
    r_th.font.name = "Calibri"
    r_th.font.size = Pt(12)
    r_th.font.bold = True
    r_th.font.color.rgb = C_NAVY

    toc_data = [
        ["Section A", "First-Principles AI, ML, DL, and Foundation Concepts", "ANN derivations, backprop, activations (SwiGLU), BPE, attention variance sqrt(d_k), RoPE, RMSNorm, RLHF/DPO"],
        ["Section B", "Step-by-Step Architecture and Working of All Key Models", "BERT (MLM/NSP), T5 (text-to-text span corruption), GPT family (MoE), PaLM, LLaMA-3.3, Gemini 3.1 Flash-Lite"],
        ["Section C", "Multi-Agent Systems, Reasoning Patterns, and Agent Frameworks", "ReAct loop, CoT, ToT, GoT, Reflexion, AutoGen, CAMEL, MetaGPT, ChatDev, and Zhu et al. (ACL 2025 MultiAgentBench)"],
        ["Section D", "Deep Dive into the 5 Multi-Agent Topologies", "SINGLE, CHAIN, STAR, TREE, GRAPH: message passing equations, context accumulation, failure modes, concrete Cloud Migration walkthrough"],
        ["Section E", "Literature Review Reference Notes (44 Peer-Reviewed Papers)", "Audited reference cheat sheet across 5 core research themes (zero blogs, zero GitHub URLs)"],
        ["Section F", "Project Codebase Architecture, Implementation Contracts, and Testing", "Class hierarchy, BaseArchitecture/BaseAgent ABCs, anti-leakage quarantine, Streamlit GUI, 31 pytest cases"],
        ["Section G", "100+ Comprehensive Viva Voce Questions and Model Answers", "100+ rigorous Q&As across 12 categories covering theory, architecture, metrics, empirical results, and defense"],
        ["Section H", "Seminar Presentation Delivery & Viva Defense Masterclass", "25-30 minute time management, slide-by-slide verbal transitions, posture, handling challenging questions"]
    ]
    toc_tbl = doc.add_table(rows=1, cols=3)
    style_table(toc_tbl, [Inches(1.2), Inches(2.3), Inches(3.0)], ["Section", "Title", "Core High-Yield Focus Areas"], toc_data)

    print("Adding Section A (First Principles)...")
    add_section_a(doc, helpers)

    print("Adding Section B (Models Working)...")
    add_section_b(doc, helpers)

    print("Adding Section C (Agent Frameworks)...")
    add_section_c(doc, helpers)

    print("Adding Section D (Topologies)...")
    add_section_d(doc, helpers)

    print("Adding Section E (Literature Notes)...")
    add_section_e(doc, helpers)

    print("Adding Section F (Project Implementation)...")
    add_section_f(doc, helpers)

    print("Adding Section G (100+ Viva Questions)...")
    add_section_g(doc, helpers)

    print("Adding Section H (Presentation Delivery)...")
    add_section_h(doc, helpers)

    out_docx = os.path.join(os.path.dirname(__file__), "..", "seminar_submission", "Preparation", "SEMINAR_PREPARATION_GUIDE.docx")
    doc.save(out_docx)
    print(f"\n[SUCCESS] Seminar Preparation Guide saved to: {out_docx}")
    print(f"File size: {os.path.getsize(out_docx):,} bytes")

if __name__ == "__main__":
    build_prep_guide()

