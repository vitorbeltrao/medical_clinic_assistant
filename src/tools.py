TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_available_slots",
            "description": "Consulta horários disponíveis",
            "parameters": {
                "type": "object",
                "properties": {
                    "doctor": {"type": "string"}
                },
                "required": ["doctor"]
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
                    "doctor": {"type": "string"},
                    "slot": {"type": "string"}
                },
                "required": ["doctor", "slot"]
            }
        }
    }
]