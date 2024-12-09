"""
Ollama client implementation for retrieving structured city data.
Uses the official Ollama Python package with Pydantic for type validation.
"""
from typing import List

from ollama import chat
from pydantic import BaseModel


class City(BaseModel):
    """Represents a city with its country."""
    name: str
    country: str


class Cities(BaseModel):
    """Collection of cities."""
    cities: List[City]


# Get structured response from Ollama
response = chat(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "List 5 cities from around the world and their countries",
        }
    ],
    format=Cities.model_json_schema(),
)

# Parse and validate response
city_list: Cities = Cities.model_validate_json(response.message.content)

print(city_list)
