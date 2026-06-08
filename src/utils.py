import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from src.tools import TOOLS
from src.tools import AVAILABLE_TOOLS

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_iteration(messages, model="gpt-4o-mini"):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=TOOLS
    )

    assistant_message = response.choices[0].message

    if not assistant_message.tool_calls:
        return assistant_message.content

    messages.append(assistant_message)

    for tool_call in assistant_message.tool_calls:

        function_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        result = AVAILABLE_TOOLS[
            function_name
        ](**arguments)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
        )

    final_response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return final_response.choices[0].message.content
