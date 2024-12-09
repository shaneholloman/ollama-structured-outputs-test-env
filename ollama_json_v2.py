"""
Direct API implementation for extracting structured pet data from text using Ollama.
Uses the raw HTTP API to demonstrate low-level interaction with the service.
"""
import json
import requests
from requests.exceptions import RequestException

# Define the schema for pet data extraction
pet_schema = {
    "type": "object",
    "properties": {
        "pets": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "animal": {"type": "string"},
                    "age": {"type": "integer"},
                    "color": {"type": "string", "nullable": True},
                    "favorite_toy": {"type": "string", "nullable": True}
                },
                "required": ["name", "animal", "age"]
            }
        }
    },
    "required": ["pets"]
}

try:
    response = requests.post(
        'http://localhost:11434/api/chat',
        json={
            "model": "llama3.2:latest",
            "messages": [
                {
                    "role": "user",
                    "content": """
                    I have two pets.
                    A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                    I also have a 2 year old black cat named Loki who loves tennis balls.
                    """
                }
            ],
            "format": pet_schema,
            "stream": False
        },
        timeout=30  # 30 second timeout
    )

    print("Status Code:", response.status_code)
    print("Full Response:", json.dumps(json.loads(response.text), indent=2))

    if response.status_code == 200:
        result = json.loads(response.content)
        # Parse the content as JSON
        pets_data = json.loads(result['message']['content'])
        print("\nExtracted Pet Data:", json.dumps(pets_data, indent=2))
    else:
        print("Error: Non-200 status code")

except (RequestException, json.JSONDecodeError) as e:
    print(f"Error occurred: {str(e)}")
