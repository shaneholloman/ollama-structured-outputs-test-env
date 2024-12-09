import requests
import json

try:
    response = requests.post('http://localhost:11434/api/chat', json={
        "model": "llama3.2:latest",
        "messages": [
            {
                "role": "user",
                "content": "List 5 cities from around the world and their countries"
            }
        ],
        "format": "json",
        "stream": False
    })

    print("Status Code:", response.status_code)
    print("Full Response:", response.text)

    if response.status_code == 200:
        result = json.loads(response.content)
        print("\nParsed Response:", json.dumps(result, indent=2))
    else:
        print("Error: Non-200 status code")

except Exception as e:
    print(f"Error occurred: {str(e)}")
