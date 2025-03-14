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

            /* Campos de texto (TextArea) */
            .stTextArea label {
                font-size: 1.2em;
                font-weight: 400;        
                color: #FFFFFF;
                margin-bottom: 0.3em;
            }
            .stTextArea>div>textarea {
                background-color: #1e1e1e;
                border: 1px solid #CEFF08;
                color: #FFFFFF;
            }
            .stTextArea {
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

# Aplica el estilo
set_dark_theme()

# LOGO CENTRADO
st.markdown("<div class='center-logo'>", unsafe_allow_html=True)
st.image("images/anim-logo-1fps-verde.gif", width=150)  # Ajusta el width si necesitas
st.markdown("</div>", unsafe_allow_html=True)

# TÍTULO
st.title("Prompt Optimizer")

# LÍNEA SEPARADORA
st.markdown("<hr class='separator'>", unsafe_allow_html=True)

# PREGUNTAS (4 TEXT AREAS)
q1 = st.text_area("¿En qué áreas del negocio ven potencial para IA?")
q2 = st.text_area("¿Qué resultados esperan obtener con IA?")
q3 = st.text_area("¿La empresa ya usa datos para la toma de decisiones?")
q4 = st.text_area("¿Tienen un equipo dedicado a usar la IA para la automatización de procesos?")

# BOTÓN
if st.button("Enviar respuestas"):
    st.success("¡Gracias! Pronto revisaremos tus respuestas.")
