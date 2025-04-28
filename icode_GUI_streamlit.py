import streamlit as st
import requests
import json
import ssl
import pypandoc
from doc_formatter import create_formatted_doc
from icode_prompt import get_prompt
import os

# API details
url = "https://aoai-farm.bosch-temp.com/api/openai/deployments/google-gemini-1-5-flash/chat/completions"
api_key = st.secrets["MY_SECRET_API_KEY"]
headers = {
    "genaiplatform-farm-subscription-key": api_key,
    "Content-Type": "application/json"
}

ssl._create_default_https_context = ssl._create_unverified_context
pypandoc.download_pandoc()

def generate_documentation(code_snippet):
    prompt = get_prompt(code_snippet)
    payload = {
        "model": "gemini-1.5-flash",
        "n": 1,
        "messages": [
            {"role": "system", "content": "You are an experienced legacy systems analyst and documentation writer."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}\n{response.text}"

# Streamlit App
st.title("Legacy Documentation Generator")

uploaded_file = st.file_uploader("Upload your Legacy file", type=["cbl"])

if uploaded_file is not None:
    sample_code = uploaded_file.read().decode('utf-8')
    
    if st.button("Generate Documentation"):
        with st.spinner('Generating documentation...'):
            try:
                documentation = generate_documentation(sample_code)

                # Save to .md
                with open("LLM_Response.md", "w", encoding="utf-8") as md_file:
                    md_file.write(documentation)

                base_name = os.path.splitext(os.path.basename(uploaded_file.name))[0]
                final_docx_name = f"{base_name}_Documentation.docx"

                # Convert to .docx
                pypandoc.convert_file('LLM_Response.md', 'docx', outputfile="Doc_LLM_Response.docx", extra_args=['--standalone'])

                create_formatted_doc("Doc_LLM_Response.docx", filename=final_docx_name, logo_path="logo.png")

                st.success("Documentation created successfully!")
                with open(final_docx_name, "rb") as file:
                    st.download_button("Download Documentation", file, file_name=final_docx_name)

            except Exception as e:
                st.error(f"Error: {e}")
