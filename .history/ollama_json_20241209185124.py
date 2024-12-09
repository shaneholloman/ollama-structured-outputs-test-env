import requests
import json

response = requests.post('http://localhost:11434/api/generate', json={
  "model": "llama3.2:latest",
  "prompt": "List 5 cities from around the world and their countries, with a short description",
  "stream": False,
  "format": "json"
})

print(json.loads(response.content)['response'])
