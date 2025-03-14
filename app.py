import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Prompt Optimizer", layout="centered")

# Función para inyectar estilos en modo oscuro con detalles en #CEFF08
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
            
            /* Línea horizontal (más gruesa y en #CEFF08) */
            hr {
                border: 4px solid #CEFF08;
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

            /* Contenedor para centrar imagen del logo */
            .center-logo {
                display: flex;
                justify-content: center;
                margin: 1em 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Aplicamos el estilo
set_dark_theme()

# --------------------------------------------------------------------------
# Centra el logo en la parte superior
st.markdown("<div class='center-logo'>", unsafe_allow_html=True)
st.image("images/anim-logo-1fps-verde.gif", width=200)
st.markdown("</div>", unsafe_allow_html=True)

# TÍTULO PRINCIPAL
st.title("Prompt Optimizer")

# Línea de acento
st.markdown("<hr>", unsafe_allow_html=True)

# EJEMPLO DE CAMPOS DE TEXTO (¡PON TUS PROPIOS CAMPOS AQUÍ!)
q1 = st.text_area("¿En qué áreas del negocio ven potencial para IA?")
q2 = st.text_area("¿Qué resultados esperan obtener con IA?")

# BOTÓN
if st.button("Enviar respuestas"):
    st.write("¡Gracias! Pronto revisaremos tus respuestas.")
