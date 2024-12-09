"""
OpenAI-compatible implementation for extracting structured pet data from text using Ollama.
Demonstrates using OpenAI's client library directly with Ollama.
"""
from typing import List, Optional
from openai import OpenAI
from pydantic import BaseModel

# Initialize OpenAI client pointing to Ollama
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

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

try:
    # Use OpenAI's parse method for structured output
    completion = client.beta.chat.completions.parse(
        temperature=0,
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": """
                I have two pets.
                A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                I also have a 2 year old black cat named Loki who loves tennis balls.
                """
            }
        ],
        response_format=PetList,
    )

    # Handle the response
    pet_response = completion.choices[0].message
    if pet_response.parsed:
        print("Extracted Pet Data:", pet_response.parsed)
    elif pet_response.refusal:
        print("Model refused to parse:", pet_response.refusal)

except (ValueError, AttributeError, RuntimeError) as e:
    print("Error processing response:", e)
