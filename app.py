import streamlit as st

st.set_page_config(page_title="Generador de Prompts", layout="centered")

# Estilos CSS personalizados para modo dark con tipografía Montserrat
def set_dark_theme():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');
            body { background-color: #121212; color: #e0e0e0; font-family: 'Montserrat', sans-serif; }
            .stTextArea, .stSelectbox { background-color: #1e1e1e !important; color: #e0e0e0 !important; font-family: 'Montserrat', sans-serif; }
            .stButton>button { background-color: #6200ea; color: white; border-radius: 8px; font-family: 'Montserrat', sans-serif; }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_dark_theme()

def generate_prompt(purpose, scope, sources, format_output, audience, depth):
    prompt = f"""
    **Propósito del análisis:** {purpose}
    **Alcance del contenido:** {scope}
    **Fuentes o referencias:** {sources}
    **Formato de salida:** {format_output}
    **Audiencia:** {audience}
    **Nivel de profundidad:** {depth}
    """
    return prompt

st.title("Generador de Prompts para Deep Research")

purpose = st.text_area("Propósito del análisis", "Quiero un análisis detallado sobre...")
scope = st.text_area("Alcance del contenido", "Incluye ejemplos de... Evita...")
sources = st.text_area("Fuentes o referencias", "Proporcióname datos basados en estudios recientes de...")
format_output = st.selectbox("Formato de salida", ["Informe estructurado", "Lista de puntos clave", "Otro (especificar en texto)"])
audience = st.selectbox("Audiencia", ["Técnico", "Ejecutivo", "General", "Otro (especificar en texto)"])
depth = st.selectbox("Nivel de profundidad", ["Resumen ejecutivo + Análisis profundo", "Solo resumen ejecutivo", "Solo análisis detallado"])

if st.button("Generar Prompt"):
    result = generate_prompt(purpose, scope, sources, format_output, audience, depth)
    st.text_area("Prompt generado", result, height=200)
