import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Prompt Optimizer", layout="centered")

def set_dark_theme():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

            /* Estilo general */
            body {
                background-color: #121212;
                color: #e0e0e0;
                font-family: 'Montserrat', sans-serif;
                margin: 0;
                padding: 0;
            }
            
            /* Encabezados */
            h1, h2, h3, h4 {
                color: #f2f2f2;
                margin: 0.5em 0;
                font-weight: 600;
            }

            /* Contenedor para centrar el logo */
            .center-logo {
                display: flex;
                justify-content: center;
                margin: 1em 0;
            }

            /* Línea separadora personalizada */
            .separator {
                border: 0;
                border-top: 4px solid #CEFF08; /* Más gruesa y color #CEFF08 */
                margin: 1em 0;
            }

            /* Campos de texto (TextArea, SelectBox, TextInput) */
            .stTextArea label, .stSelectbox label, .stTextInput label {
                font-size: 1.1em;
                font-weight: 400;        
                color: #FFFFFF;
                margin-bottom: 0.3em;
            }
            .stTextArea>div>textarea, .stTextInput>div>input {
                background-color: #1e1e1e;
                border: 1px solid #CEFF08;
                color: #FFFFFF;
            }
            .stTextArea, .stTextInput, .stSelectbox {
                margin-bottom: 1em;
            }
            
            /* Botón en #CEFF08 */
            .stButton>button {
                background-color: #CEFF08;
                color: #121212;
                border: none;
                border-radius: 6px;
                padding: 0.6em 1.2em;
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                font-size: 1em;
                cursor: pointer;
            }
            .stButton>button:hover {
                background-color: #e3ff5f;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Aplicamos el estilo
set_dark_theme()

# LOGO CENTRADO (ajusta el nombre y ruta de tu gif/logo si no coincide)
st.markdown("<div class='center-logo'>", unsafe_allow_html=True)
st.image("images/anim-logo-1fps-verde.gif", width=150)  
st.markdown("</div>", unsafe_allow_html=True)

# TÍTULO PRINCIPAL
st.title("Prompt Optimizer")

# LÍNEA SEPARADORA
st.markdown("<hr class='separator'>", unsafe_allow_html=True)

# Descripción
st.markdown("#### Generador de prompts optimizados para **Deep Research** en ChatGPT")
st.write("Completa los campos a continuación y obtendrás un prompt bien estructurado de forma automática.")

# Texto aclaratorio antes de las preguntas
st.markdown("**Puedes dejar en blanco alguna de las respuestas si no tienes clara la respuesta.**")

# --------------------------------------------------------------------------
# CAMPOS PARA EL FORMULARIO (todos opcionales)
purpose = st.text_area("1. Propósito del análisis", 
    placeholder="Ejemplo: 'Quiero un análisis detallado sobre las tendencias de inversión en AI-driven innovation en Europa para 2025-2030.'")

scope = st.text_area("2. Alcance del contenido", 
    placeholder="Ejemplo: 'Incluye ejemplos de empresas que han implementado AI-driven innovation...'")

sources = st.text_area("3. Fuentes o referencias",
    placeholder="Ejemplo: 'Proporcióname datos basados en estudios recientes de 2023-2024...'")

format_output = st.text_area("4. Formato de salida", 
    placeholder="Ejemplo: 'Responde en formato de informe estructurado con introducción, análisis y conclusión.'")

audience = st.text_area("5. Audiencia", 
    placeholder="Ejemplo: 'Redacta la respuesta de manera técnica para un público especializado...'")

depth = st.text_area("6. Nivel de profundidad", 
    placeholder="Ejemplo: 'Dame un resumen ejecutivo de 200 palabras y luego un análisis profundo de 1000 palabras.'")

# --------------------------------------------------------------------------
# FUNCIÓN PARA GENERAR EL PROMPT
def generate_prompt(purpose, scope, sources, format_output, audience, depth):
    prompt = f\"\"\"  
**Propósito del análisis:** {purpose}

**Alcance del contenido:** {scope}

**Fuentes o referencias:** {sources}

**Formato de salida:** {format_output}

**Audiencia:** {audience}

**Nivel de profundidad:** {depth}
\"\"\"
    return prompt.strip()

# BOTÓN PARA GENERAR
if st.button("Generar Prompt"):
    result = generate_prompt(purpose, scope, sources, format_output, audienc
