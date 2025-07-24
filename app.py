import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="Wurks Resume Formatter", layout="centered")
st.title("📄 Wurks Resume Formatter")
st.markdown("Enter your details below and download your formatted resume.")

# Resume inputs
with st.form("resume_form"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    linkedin = st.text_input("LinkedIn URL")
    summary = st.text_area("Professional Summary")
    skills = st.text_area("Skills")
    experience = st.text_area("Professional Experience")
    education = st.text_area("Education")
    certifications = st.text_area("Certifications")
    submitted = st.form_submit_button("Generate Resume")

if submitted:
    template = Document("Wurks_Resume_Template_Streamlit.docx")

    def replace_placeholder(doc, placeholder, value):
        for para in doc.paragraphs:
            if placeholder in para.text:
                for run in para.runs:
                    run.text = run.text.replace(placeholder, value)

    replacements = {
        "{Name}": name,
        "{Phone}": phone,
        "{Email}": email,
        "{LinkedIn}": linkedin,
        "{Summary}": summary,
        "{Skills}": skills,
        "{Experience}": experience,
        "{Education}": education,
        "{Certifications}": certifications
    }

    for key, val in replacements.items():
        replace_placeholder(template, key, val)

    output = io.BytesIO()
    template.save(output)
    st.success("✅ Resume generated successfully!")
    st.download_button(
        label="📥 Download Resume",
        data=output.getvalue(),
        file_name=f"{name.replace(' ', '_')}_Formatted.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
