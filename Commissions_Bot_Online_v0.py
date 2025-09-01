import streamlit as st
import google.generativeai as genai
import os
import csv
from datetime import datetime

# --- CONFIGURATION ---
# Now we get the API key from Streamlit's secret management
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Error de configuración: No se pudo encontrar la clave de API. Asegúrate de haberla configurado en los secretos de Streamlit.")
    st.stop()


LOG_FILE = 'log.csv'

# --- KNOWLEDGE BASE ---
DOCUMENT_CONTEXT = """
PASTE THE ENTIRE TEXT OF YOUR COMMISSIONS DOCUMENT HERE.
"""

# --- HELPER FUNCTION ---
def log_interaction(question, answer):
    # This logging method will only work if the hosting platform allows writing files.
    # On Streamlit Community Cloud, this log will be temporary and reset on each deploy.
    # For persistent logging, a database would be needed in the future.
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'question', 'answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'question': question,
            'answer': answer
        })

# --- MAIN APP LOGIC ---
model = genai.GenerativeModel('gemini-1.5-pro-latest')

st.title("🤖 Asistente de Comisiones")

user_question = st.text_area("Escribe tu pregunta aquí:")

if st.button("Consultar"):
    if user_question:
        with st.spinner("Buscando la mejor respuesta..."):
            prompt = f"""
              Eres un asistente experto en el plan de comisiones de la empresa.
              Tu única fuente de verdad es el siguiente documento de reglas. No inventes información.
              --- DOCUMENTO DE REGLAS ---
              {DOCUMENT_CONTEXT}
              --- FIN DEL DOCUMENTO ---
              PREGUNTA DEL USUARIO: "{user_question}"
              RESPUESTA:
            """
            response = model.generate_content(prompt)
            ai_answer = response.text
            # log_interaction(user_question, ai_answer) # Logging to a file might be restricted
            st.markdown(ai_answer)
    else:
        st.warning("Por favor, escribe una pregunta.")