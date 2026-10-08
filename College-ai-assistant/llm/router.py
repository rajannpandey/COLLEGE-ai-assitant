import os
import json
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN was not found. Check your .env file.")
client = InferenceClient(
    token=HF_TOKEN
)
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate attendance percentage using classes attended and total classes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "classes_attended": {
                        "type": "number",
                        "description": "Number of classes attended"
                    },
                    "total_classes": {
                        "type": "number",
                        "description": "Total number of classes"
                    }
                },
                "required": [
                    "classes_attended",
                    "total_classes"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "attendance",
            "description": "Mark a student's attendance for a particular date and subject.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_id": {
                        "type": "string",
                        "description": "Student ID"
                    },
                    "date": {
                        "type": "string",
                        "description": "Attendance date in YYYY-MM-DD format"
                    },
                    "subject": {
                        "type": "string",
                        "description": "Subject name"
                    },
                    "status": {
                        "type": "string",
                        "enum": [
                            "present",
                            "absent"
                        ],
                        "description": "Attendance status"
                    }
                },
                "required": [
                    "student_id",
                    "date",
                    "subject",
                    "status"
                ]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "timetable",
            "description": "Analyze a college timetable and answer questions about classes and schedules.",
            "parameters": {
                "type": "object",
                "properties": {
                    "document": {
                        "type": "string",
                        "description": "Timetable document content"
                    },
                    "question": {
                        "type": "string",
                        "description": "Question about the timetable"
                    }
                },
                "required": [
                    "document",
                    "question"
                ]
            }
        }
    }
]
def choose_tool(user_input):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a College AI Assistant. "
                "Choose the appropriate tool for the student's request. "
                "Use calculator for attendance percentage calculations. "
                "Use attendance for marking attendance. "
                "Use timetable for timetable questions."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=300
    )
    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        return {
            "tool": tool_call.function.name,
            "arguments": json.loads(
                tool_call.function.arguments
            )
        }
    return {
        "tool": "none",
        "arguments": {}
    }
