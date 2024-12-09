"""
Instructor-enhanced implementation for retrieving structured city data from Ollama.
Uses the Instructor package to provide OpenAI-compatible interface with Pydantic integration.
"""
from typing import List

import instructor
from openai import OpenAI
from pydantic import BaseModel


class City(BaseModel):
    """Represents a city with its country."""
    name: str
    country: str


class Cities(BaseModel):
    """Collection of cities."""
    cities: List[City]


# Initialize OpenAI-compatible client with Instructor
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

# Get structured response using Instructor
city_list: Cities = client.chat.completions.create(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": "List 5 cities from around the world and their countries",
        }
    ],
    response_model=Cities,
)

print(city_list)
