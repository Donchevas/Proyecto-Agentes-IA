import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="AI Agent Meeting Analyzer", page_icon="🤖")

st.title("🚀 Analizador de Reuniones con Agentes de IA")
st.markdown("""
Esta herramienta utiliza una tripulación de **Agentes de IA (CrewAI)** desplegada en **Google Cloud Run** para procesar transcripciones, generar actas y analizar riesgos críticos.
""")

# URL de tu servicio en Cloud Run
API_URL = "https://agente-de-riesgos-1069673789450.us-central1.run.app/procesar-reunion"

# Área de entrada de texto
transcripcion = st.text_area(
    "Pega aquí la transcripción de la reunión:",
    height=250,
    placeholder="Ejemplo: Reunión con Scotiabank para liquidación de deuda..."
)

if st.button("🚀 Ejecutar Análisis de Agentes"):
    if not transcripcion:
        st.warning("Por favor, ingresa una transcripción para continuar.")
    else:
        with st.spinner("La tripulación de agentes está trabajando (Secretario + Analista)..."):
            try:
                # Llamada a tu backend en la nube
                response = requests.post(API_URL, json={"transcripcion": transcripcion}, timeout=60)
                
                if response.status_code == 200:
                    resultado = response.json().get("resultado", "No se recibió resultado.")
                    
                    st.success("✅ Análisis Completado")
                    st.markdown("### 📋 Informe Final de los Agentes")
                    st.info(resultado)
                else:
                    st.error(f"Error en el servidor: {response.status_code}")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error de conexión: {e}")

st.sidebar.markdown("---")
st.sidebar.write("🏠 **Arquitectura:** Cloud Run + CrewAI + Gemini 2.5 Flash Lite")
st.sidebar.write("👨‍💻 **Desarrollado por:** Christian Molina")