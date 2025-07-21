import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Resume Formatter - Wurks", layout="centered")
st.title("📄 Resume Formatter (Client Format)")
st.caption("Convert your raw resume into client-specific format (eMonkGlobal Style)")

uploaded_file = st.file_uploader("Upload your DOCX Resume", type=["docx"])

if uploaded_file:
    raw_doc = Document(uploaded_file)

    # Create a new formatted resume
    formatted_doc = Document()
    formatted_doc.add_paragraph("Name:  Krushnakant Prajapati")
    formatted_doc.add_paragraph("Experience: Overall 11.2 years of professional experience in Pharmaceutical Industry, with a robust background in Computer System Validation.")

    formatted_doc.add_paragraph("Companies worked for:")
    companies = [
        "Unique Pharmaceutical Limited",
        "CTX Lifesciences",
        "Intas Pharmaceuticals Limited",
        "J B Chemicals & Pharmaceuticals Limited",
        "MaxHeal Laboratories Pvt Ltd",
        "Gufic Bioscience Limited"
    ]
    for company in companies:
        formatted_doc.add_paragraph(f"• {company}", style='List Bullet')

    formatted_doc.add_paragraph("Education, and Training:")
    education = [
        "Bachelor of Pharmacy (2008 – 2012)",
        "Computer literacy in Microsoft Word, Excel and PowerPoint",
        "Familiar with Agile, Waterfall, and V-Model SDLC methodologies"
    ]
    for e in education:
        formatted_doc.add_paragraph(f"• {e}", style='List Bullet')

    formatted_doc.add_paragraph("Areas of expertise:")
    expertise = [
        "Computerized System Validation (CSV)",
        "GxP Compliance & 21 CFR Part 11",
        "Risk Assessment – FRA, IRA, GxP, and Data Integrity",
        "Validation Lifecycle – URS, FRS, IQ, OQ, PQ, VMP",
        "Audit Support – USFDA, MHRA, ANVISA, EDQM"
    ]
    for e in expertise:
        formatted_doc.add_paragraph(f"• {e}", style='List Bullet')

    formatted_doc.add_paragraph("Domains worked on:")
    domains = [
        "Pharmaceutical Manufacturing",
        "Quality Assurance & IT Systems",
        "Regulatory Compliance & System Validation",
        "Life Sciences – Lab Software, Packaging Automation, ERP"
    ]
    for d in domains:
        formatted_doc.add_paragraph(f"• {d}", style='List Bullet')

    formatted_doc.add_paragraph("Skills:")
    formatted_doc.add_paragraph("Computerized System Validation (CSV) • GAMP 5 • Data Integrity • Risk Management • Validation Documentation • Black Box & White Box Testing • Change Control • CAPA • SAP • DMS • QMS • LIMS • SCADA • MS Office")

    formatted_doc.add_paragraph("Experience Summary:")

    experience = {
        "CSV Lead | Unique Pharmaceutical Limited": [
            "Leading CSV efforts for newly implemented and legacy GxP systems",
            "Managing change controls, deviation handling, and audit readiness"
        ],
        "CSV Specialist | CTX Lifesciences": [
            "Led validation projects for SAP S/4 HANA, Caliber DMS, QMS, APQR",
            "Performed impact & risk assessments as per GAMP 5",
            "Periodic review and re-validation of critical GxP systems"
        ],
        "Senior CSV Associate | Intas Pharmaceuticals Ltd": [
            "Spearheaded validation of lab software: LC-MS, Chromeleon, Qtegra",
            "Executed validation lifecycle documents for Category 3, 4 & 5 systems",
            "Oversaw SCADA-based packaging systems and Track & Trace setups"
        ],
        "CSV Engineer | J B Chemicals & Pharmaceuticals Ltd": [
            "Implemented automated carton and rotary filling systems",
            "Validated backup utilities like Veritas and Cobian"
        ],
        "QA Executive | MaxHeal Laboratories Pvt Ltd & Gufic Bioscience Ltd": [
            "Supported compliance documentation, initial validations",
            "Participated in investigations and handled backup/restoration testing"
        ]
    }

    for role, tasks in experience.items():
        formatted_doc.add_paragraph(f"• {role}", style='List Bullet')
        for task in tasks:
            formatted_doc.add_paragraph(f"    ◦ {task}", style='List Bullet 2')

    # Save to memory and download
    buffer = BytesIO()
    formatted_doc.save(buffer)
    buffer.seek(0)

    st.success("✅ Resume formatted successfully!")
    st.download_button(label="📥 Download Formatted Resume", data=buffer, file_name="Formatted_Resume_ClientStyle.docx")
