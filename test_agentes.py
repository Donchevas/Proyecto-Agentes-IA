import requests

# URL local de tu contenedor Docker
url = "http://localhost:8080/procesar-reunion"

# Transcripción de prueba basada en tus éxitos de hoy
payload = {
    "transcripcion": """
    Reunión de Cierre Financiero - Christian Molina. 
    Hoy 6 de febrero de 2026 se completó el pago de S/ 13,900 a Scotiabank para la condonación de deuda. 
    Se confirmó la apertura de un plazo fijo por S/ 90,000 en Interbank con tasa del 4%.
    Acuerdos: Esperar carta de no adeudo en 48 horas.
    Riesgos: El reporte de Infocorp puede tardar hasta 45 días en reflejar la deuda como cancelada.
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