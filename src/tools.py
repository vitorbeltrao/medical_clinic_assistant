import json

def listar_especialidades():
    return [
        "Cardiologia",
        "Dermatologia",
        "Ortopedia",
        "Pediatria",
        "Clínica Geral"
    ]


def consultar_horarios(medico: str):
    agenda = {
        "Dr. João": ["09:00", "10:00", "14:00"],
        "Dra. Maria": ["08:00", "11:00", "15:00"]
    }

    return agenda.get(medico, [])


def faq_clinica(pergunta: str):

    pergunta = pergunta.lower()

    if "telefone" in pergunta:
        return "(11) 99999-9999"

    if "endereço" in pergunta or "endereco" in pergunta:
        return "Rua Exemplo, 123"

    if "convênio" in pergunta or "convenio" in pergunta:
        return "Unimed, Bradesco Saúde e SulAmérica"

    return "Informação não encontrada."


AVAILABLE_TOOLS = {
    "listar_especialidades": listar_especialidades,
    "consultar_horarios": consultar_horarios,
    "faq_clinica": faq_clinica
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "consultar_horarios",
            "description": "Consulta os horários disponíveis para um médico específico.",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "medico": {
                        "type": "string",
                        "description": "Exemplo: 'Dr. João', 'Dra. Maria'"
                    }
                },
                "required": ["medico"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "faq_clinica",
            "description": "Consulta as perguntas frequentes sobre a clínica.",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "pergunta": {
                        "type": "string",
                        "description": "Exemplo: 'Qual é o endereço da clínica?', 'Quais convênios vocês aceitam?', 'Qual é o telefone para contato?'"
                    }
                },
                "required": ["pergunta"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_especialidades",
            "description": "Lista as especialidades disponíveis na clínica.",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        }
    },
]
