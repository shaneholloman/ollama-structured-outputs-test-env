"""
Ollama client implementation for retrieving structured city data.
Uses the official Ollama Python package with Pydantic for type validation.
"""
from typing import List, Dict, Any

from ollama import chat
from pydantic import BaseModel


class City(BaseModel):
    """Represents a city with its country."""
    name: str
    country: str


class Cities(BaseModel):
    """Collection of cities."""
    cities: List[City]


def get_city_list() -> Cities:
    """Retrieve and parse city list from Ollama."""
    # Get structured response from Ollama
    response: Dict[str, Any] = chat(  # type: ignore
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
    return Cities.model_validate_json(response['message']['content'])


if __name__ == "__main__":
    city_list = get_city_list()
    print(city_list)
