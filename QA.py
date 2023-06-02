import streamlit as st
from docquery import document, pipeline
p = pipeline('document-question-answering')

def read_pdf(pdf_file):
  #print(pdf_file)
  doc = document.load_document(pdf_file.name)
  #patient_info =  ["What is the patient’s name?","Gender?","Age?","Is the patient a registered sex offender? Any other recent convictions/offenses?""Payer source(s)?","Discharge plan/address?"]
  
  patient_info = ["What is the patient’s name?","Gender?","Age?","MRN?","Height?","Weight","Contact Number/Phone?"]
  data = {}
  for q in patient_info:
    print(q, p(question=q, **doc.context)[0]['answer'])
    data[q] = p(question=q, **doc.context)[0]['answer']

  return str(data)

# def read_pdf(file):
   
#     return "Working"

st.title('Q/A PDF')

uploaded_file = st.file_uploader('Upload a PDF file', type='pdf')

if uploaded_file is not None:
    if st.button('Extract Questions'):
        try:
            text = read_pdf(uploaded_file)
            st.write('Text extracted:')
            st.write(text)
        except:
            st.write('This file cannot be processed. Please upload another PDF file.')
