"""
Instructor-enhanced implementation for extracting structured pet data from text using Ollama.
Uses the Instructor package to provide OpenAI-compatible interface with Pydantic integration.
"""
from typing import List, Optional

import instructor
from openai import OpenAI
from pydantic import BaseModel


class Pet(BaseModel):
    """Represents a pet with its attributes."""
    name: str
    animal: str
    age: int
    color: Optional[str] = None
    favorite_toy: Optional[str] = None


class PetList(BaseModel):
    """Collection of pets."""
    pets: List[Pet]


# Initialize OpenAI-compatible client with Instructor
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

# Get structured response using Instructor
pet_list: PetList = client.chat.completions.create(
    model="llama3.2:latest",
    messages=[
        {
            "role": "user",
            "content": """
            I have two pets.
            A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
            I also have a 2 year old black cat named Loki who loves tennis balls.
            """,
        }
    ],
    response_model=PetList,
)

print(pet_list)
