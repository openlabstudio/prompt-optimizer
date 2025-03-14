import streamlit as st

# Configuramos la página
st.set_page_config(page_title="Test de evaluación", layout="centered")

# Función para inyectar estilos CSS en modo oscuro con detalles en #CEFF08
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
            
            /* Línea horizontal */
            hr {
                border: 2px solid #CEFF08; /* Color de la línea */
                margin: 1em 0;
            }
            
            /* Campos de texto (TextArea) */
            .stTextArea label {
                font-size: 1.2em;        /* Tamaño de la etiqueta (pregunta) */
                font-weight: 400;        
                color: #FFFFFF;
                margin-bottom: 0.3em;
            }
            .stTextArea>div>textarea {
                background-color: #1e1e1e;  /* Fondo oscuro */
                border: 1px solid #CEFF08;  /* Borde en #CEFF08 */
                color: #FFFFFF;             /* Texto blanco */
            }
            .stTextArea {
                margin-bottom: 1em;         /* Espacio entre campos */
            }
            
            /* Botón */
            .stButton>button {
                background-color: #CEFF08;
                color: #121212;      /* Contraste de texto sobre fondo #CEFF08 */
                border: none;
                border-radius: 6px;
                padding: 0.6em 1.2em;
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                font-size: 1em;
                cursor: pointer;
            }
            .stButton>button:hover {
                background-color: #e3ff5f; /* Cambia un poco el tono al pasar el mouse */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Aplicamos el estilo
set_dark_theme()

# Título principal
st.title("Test de evaluación")

# Línea de acento
st.markdown("<hr>", unsafe_allow_html=True)

# Las preguntas en campos de texto (sin 'help' para que no aparezca texto adicional)
q1 = st.text_area("¿En qué áreas del negocio ven potencial para IA?")
q2 = st.text_area("¿Qué resultados esperan obtener con IA?")
q3 = st.text_area("¿La empresa ya usa datos para la toma de decisiones?")
q4 = st.text_area("¿Tienen un equipo dedicado a usar la IA para la automatización de procesos?")

# Botón para enviar
if st.button("Enviar respuestas"):
    st.write("¡Gracias por tu participación!")
