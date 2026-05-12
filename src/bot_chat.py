import os
import json
from openai import OpenAI
from dotenv import load_dotenv

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "save_patient_info",
            "description": "Salva informações iniciais do paciente",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "endereco": {"type": "string"},
                    "plano_saude": {"type": "string"},
                    "medico": {"type": "string"}
                },
                "required": ["nome"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_appointment",
            "description": "Agenda consulta",
            "parameters": {
                "type": "object",
                "properties": {
                    "medico": {"type": "string"},
                    "data": {"type": "string"},
                    "horario": {"type": "string"}
                },
                "required": ["medico", "data", "horario"]
            }
        }
    }
]

SYSTEM_PROMPT = """
Você é a assistente virtual de uma clínica médica.

Objetivos:
- Coletar nome
- Endereço
- Plano de saúde
- Médico desejado
- Explicar valores quando perguntado
- Consultar horários
- Agendar consulta

Regras:
- Seja educada e objetiva
- Faça uma pergunta por vez
- Nunca invente horários
- Se faltar informação, pergunte naturalmente
- Quando tiver dados suficientes, use as tools
"""

client = os.getenv('OPENAI_API_KEY')

def chat(messages):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    return response.choices[0].message


def execute_tool(tool_call):

    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    if name == "save_patient_info":
        return f"Paciente salvo: {args}"

    elif name == "schedule_appointment":
        return f"Consulta agendada para {args['data']} às {args['horario']} com {args['medico']}"