#!/bin/bash

# Shell script implementation for extracting structured pet data from text using Ollama.
# Uses curl to demonstrate direct API interaction.

# Define the JSON payload with schema
read -r -d '' PAYLOAD << EOM
{
  "model": "llama3.2:latest",
  "messages": [{
    "role": "user",
    "content": "I have two pets.\nA cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.\nI also have a 2 year old black cat named Loki who loves tennis balls."
  }],
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "pets": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "animal": {
              "type": "string"
            },
            "age": {
              "type": "integer"
            },
            "color": {
              "type": "string",
              "nullable": true
            },
            "favorite_toy": {
              "type": "string",
              "nullable": true
            }
          },
          "required": ["name", "animal", "age"]
        }
      }
    },
    "required": ["pets"]
  }
}
EOM

# Make the API request and format the response
curl -X POST http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" | jq '.'
