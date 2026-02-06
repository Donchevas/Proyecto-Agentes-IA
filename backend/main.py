import os
from flask import Flask, request, jsonify
from crewai import Agent, Task, Crew, Process
from langchain_google_vertexai import VertexAI

app = Flask(__name__)

# Configuración técnica validada
PROJECT_ID = "iagen-gcp-cwmi"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-flash-lite"

# Inicialización del modelo de Vertex AI
llm = VertexAI(
    project=PROJECT_ID,
    location=LOCATION,
    model_name=MODEL_NAME
)

# Definición de Agentes
secretario = Agent(
    role='Secretario Ejecutivo Senior',
    goal='Crear un acta de reunión precisa y estructurada.',
    backstory='Experto en gestión de proyectos con 20 años de experiencia redactando actas ejecutivas.',
    allow_delegation=False,
    llm=llm
)

analista_riesgos = Agent(
    role='Especialista en Gestión de Riesgos',
    goal='Identificar riesgos y amenazas en la transcripción de la reunión.',
    backstory='Auditor experto capaz de detectar puntos críticos y proponer mitigaciones.',
    allow_delegation=False,
    llm=llm
)

@app.route('/procesar-reunion', methods=['POST'])
def procesar():
    data = request.json
    transcripcion = data.get('transcripcion', '')
    
    if not transcripcion:
        return jsonify({"error": "No se proporcionó una transcripción"}), 400

    # Definición de Tareas dinámicas
    tarea_acta = Task(
        description=f"Genera un acta detallada de esta reunión: {transcripcion}",
        expected_output="Acta con: Asistentes, Acuerdos y Tareas.",
        agent=secretario
    )

    tarea_riesgos = Task(
        description="Analiza la transcripción anterior y detecta 3 riesgos críticos del proyecto.",
        expected_output="Lista de riesgos con sugerencia de mitigación.",
        agent=analista_riesgos
    )

    # Orquestación de la tripulación
    crew = Crew(
        agents=[secretario, analista_riesgos],
        tasks=[tarea_acta, tarea_riesgos],
        process=Process.sequential
    )

    result = crew.kickoff()
    
    return jsonify({
        "status": "exitoso",
        "resultado": str(result)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)