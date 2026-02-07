import requests

# URL local de tu contenedor Docker
url = "https://agente-de-riesgos-1069673789450.us-central1.run.app/procesar-reunion"

# Transcripción de prueba basada en tus éxitos de hoy
payload = {
    "transcripcion": """
    Reunión de Diseño: Pipeline de Datos para el proyecto Chatbase - Proyecto iagen-gcp-cwmi.
    Participantes: Christian Molina (Arquitecto de Datos).
    Objetivo: Definir la arquitectura para el procesamiento de documentos legales en la nube.
    
    Puntos tratados:
    1. Usaremos Azure Data Factory para la ingesta desde el repositorio local hacia un Data Lake en Azure (capa Bronze).
    2. El procesamiento se hará con Databricks para limpiar los datos y moverlos a la capa Silver.
    3. Riesgos: Se detectó que el volumen de documentos PDF escaneados es muy alto (50GB), lo que podría elevar los costos de procesamiento en Azure si no se optimizan los clusters.
    4. Acuerdos: Christian validará el uso de OCR de Azure antes del viernes para asegurar que el texto extraído sea de alta calidad para el modelo RAG.
    """
}

print("🚀 Enviando transcripción a la tripulación de agentes...")

try:
    response = requests.post(url, json=payload, timeout=60)
    if response.status_code == 200:
        print("\n✅ RESPUESTA DE LOS AGENTES:")
        print(response.json()['resultado'])
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"❌ Error de conexión: {e}")