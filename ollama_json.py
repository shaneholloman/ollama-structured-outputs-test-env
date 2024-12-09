"""
Direct API implementation for retrieving structured city data from Ollama.
Uses the raw HTTP API to demonstrate low-level interaction with the service.
"""
import json
import requests
from requests.exceptions import RequestException

try:
    response = requests.post(
        'http://localhost:11434/api/chat',
        json={
            "model": "llama3.2:latest",
            "messages": [
                {
                    "role": "user",
                    "content": "List 5 cities from around the world and their countries"
                }
            ],
            "format": "json",
            "stream": False
        },
        timeout=30  # 30 second timeout
    )

    print("Status Code:", response.status_code)
    print("Full Response:", json.dumps(json.loads(response.text), indent=2))

    if response.status_code == 200:
        result = json.loads(response.content)
        # Parse the nested JSON string in content
        content_json = json.loads(result['message']['content'])

        # Transform into our desired format
        cities_list = {
            "cities": [
                {"name": name.strip(), "country": country.strip()}
                for name, country in content_json.items()
            ]
        }

        print("\nFormatted Cities:", json.dumps(cities_list, indent=2))
    else:
        print("Error: Non-200 status code")

except (RequestException, json.JSONDecodeError) as e:
    print(f"Error occurred: {str(e)}")
