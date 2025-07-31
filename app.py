import streamlit as st
from utils import extract_text_from_pdf, generate_questions

st.set_page_config(page_title="Azure PDF Quiz Generator", layout="wide")
st.title("📘 PDF to Quiz Generator using Azure AI")

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")

# Session variables
if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = None

if uploaded_file:
    pdf_bytes = uploaded_file.read()

    # Extract Text Section
    st.subheader("📄 Text Extraction")
    if st.button("🔍 Extract Text from PDF"):
        try:
            st.session_state.extracted_text = extract_text_from_pdf(pdf_bytes)
            st.success("✅ Text extracted successfully.")
        except Exception as e:
            st.error(f"❌ Failed to extract text: {e}")

    if st.session_state.extracted_text:
        with st.expander("🔎 View Extracted Text"):
            st.write(st.session_state.extracted_text)

    # Question Generation Section
    st.subheader("❓ Question Generator")
    if st.button("🧩 Generate Questions"):
        st.session_state.show_q_options = True

    if st.session_state.get("show_q_options", False):
        col1, col2 = st.columns(2)
        
        with col1:
            qtype = st.selectbox("📌 Select question type", 
                               ["MCQ", "True/False", "Fill in the Blanks", "Short Answer"])
        
        with col2:
            num_questions = st.number_input("🔢 Number of questions", 
                                          min_value=1, max_value=10, value=3)
            
        if st.button("🚀 Generate Now"):
            source_text = st.session_state.extracted_text
            if source_text:
                try:
                    questions = generate_questions(source_text, qtype, num_questions)
                    st.success("✅ Questions generated successfully!")
                    
                    # Format output nicely
                    st.markdown(f"### 📚 {qtype} Questions ({num_questions})")
                    
                    if qtype == "MCQ":
                        # Split questions and format with line breaks for options
                        q_list = questions.split('\n\n')
                        for i, q in enumerate(q_list, 1):
                            q_lines = q.split('\n')
                            if len(q_lines) >= 2:
                                st.markdown(f"**Q{i}:** {q_lines[0]}")
                                for line in q_lines[1:]:
                                    if line.startswith("Correct answer:"):
                                        st.success(line)
                                    else:
                                        st.markdown(line)
                    else:
                        # Format other question types normally
                        st.markdown(questions.replace('\n', '\n\n'))
                        
                except Exception as e:
                    st.error(f"❌ Failed to generate questions: {e}")
            else:
                st.warning("⚠️ Please extract text before generating questions.")
