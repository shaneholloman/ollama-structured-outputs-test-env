# ollama-structured-outputs-test-env

> CodeMap Source: GitHub repository: <https://github.com/shaneholloman/ollama-structured-outputs-test-env>

This markdown document provides a comprehensive overview of the directory structure and file contents. It aims to give viewers (human or AI) a complete view of the codebase in a single file for easy analysis.

## Document Table of Contents

The table of contents below is for navigational convenience and reflects this document's structure, not the actual file structure of the repository.

<!-- TOC -->

- [ollama-structured-outputs-test-env](#ollama-structured-outputs-test-env)
  - [Document Table of Contents](#document-table-of-contents)
  - [Repo File Tree](#repo-file-tree)
  - [Repo File Contents](#repo-file-contents)
    - [README.md](#readmemd)
    - [.gitignore](#gitignore)
    - [.python-version](#python-version)
    - [docs/notes.md](#docsnotesmd)
    - [docs/structured-json-outputs.md](#docsstructured-json-outputsmd)
    - [GITHUB\_SETUP.md](#github_setupmd)
    - [instructor\_ollama\_v1.py](#instructor_ollama_v1py)
    - [instructor\_ollama\_v2.py](#instructor_ollama_v2py)
    - [ollama\_json\_v1.py](#ollama_json_v1py)
    - [ollama\_json\_v2.py](#ollama_json_v2py)
    - [ollama\_only\_v1.js](#ollama_only_v1js)
    - [ollama\_only\_v1.py](#ollama_only_v1py)
    - [ollama\_only\_v1.sh](#ollama_only_v1sh)
    - [ollama\_only\_v2.js](#ollama_only_v2js)
    - [ollama\_only\_v2.py](#ollama_only_v2py)
    - [ollama\_only\_v2.sh](#ollama_only_v2sh)
    - [package-lock.json](#package-lockjson)
    - [package.json](#packagejson)
    - [pyproject.toml](#pyprojecttoml)
    - [SETUP.md](#setupmd)
    - [uv.lock](#uvlock)

<!-- /TOC -->

## Repo File Tree

This file tree represents the actual structure of the repository. It's crucial for understanding the organization of the codebase.

```tree
.
├── docs/
│   ├── notes.md
│   └── structured-json-outputs.md
├── .gitignore
├── .python-version
├── GITHUB_SETUP.md
├── README.md
├── SETUP.md
├── instructor_ollama_v1.py
├── instructor_ollama_v2.py
├── ollama_json_v1.py
├── ollama_json_v2.py
├── ollama_only_v1.js
├── ollama_only_v1.py
├── ollama_only_v1.sh
├── ollama_only_v2.js
├── ollama_only_v2.py
├── ollama_only_v2.sh
├── package-lock.json
├── package.json
├── pyproject.toml
└── uv.lock

1 directories, 21 files
```

## Repo File Contents

The following sections present the content of each file in the repository. Large and binary files are acknowledged but their contents are not displayed.

### .gitignore

```ini
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.pytest_cache/
.coverage
htmlcov/

# JavaScript
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Virtual Environment
.env
.venv
env/
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo
.project
.classpath
.settings/

# OS
.DS_Store
Thumbs.db
*.log
```

### .python-version

```txt
3.12
```

### GITHUB_SETUP.md

````markdown
# GitHub Repository Setup

This document outlines how to configure the GitHub repository settings using GitHub CLI (gh).

## Setting Repository Description and Topics

You can configure the repository's description and topics using the following GitHub CLI commands:

```bash
# Set repository description
gh repo edit --description "A demonstration project showing different approaches to getting structured outputs from Ollama using JavaScript and Python implementations"

# Add repository topics/tags
gh repo edit --add-topic ollama --add-topic typescript --add-topic python --add-topic structured-data
```

### Individual Commands

#### Set Description Only

```bash
gh repo edit --description "your description here"
```

#### Add Topics/Tags

```bash
gh repo edit --add-topic topic1 --add-topic topic2
```

#### Remove Topics/Tags

```bash
gh repo edit --remove-topic topic1
```

## Additional Repository Settings

The GitHub CLI also supports configuring other repository settings:

```bash
# Enable features
gh repo edit --enable-issues         # Enable issues
gh repo edit --enable-wiki          # Enable wiki
gh repo edit --enable-discussions   # Enable discussions
gh repo edit --enable-projects      # Enable projects

# Configure pull request settings
gh repo edit --enable-auto-merge              # Enable auto-merge
gh repo edit --allow-update-branch            # Allow updating PR branches
gh repo edit --delete-branch-on-merge         # Auto-delete head branches after merge
gh repo edit --enable-squash-merge           # Enable squash merging
gh repo edit --enable-merge-commit           # Enable merge commits
gh repo edit --enable-rebase-merge           # Enable rebase merging

# Set repository visibility (requires additional confirmation)
gh repo edit --visibility public --accept-visibility-change-consequences
```

For a complete list of available settings, run:

```bash
gh repo edit --help
````

### instructor_ollama_v1.py

```python
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
```

### instructor_ollama_v2.py

```python
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
```

### ollama_json_v1.py

```python
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
```

### ollama_json_v2.py

```python
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
```

### ollama_only_v1.js

```javascript
import ollama from 'ollama';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const City = z.object({
    name: z.string(),
    country: z.string(),
});

const Cities = z.object({
    cities: z.array(City)
})

const response = await ollama.chat({
    model: 'llama3.2:latest',
    messages: [{ role: 'user', content: 'List 5 cities from around the world and their countries' }],
    format: zodToJsonSchema(Cities),
});

const cities = Cities.parse(JSON.parse(response.message.content));

console.log(cities);
```

### ollama_only_v1.py

```python
"""
Ollama client implementation for retrieving structured city data.
Uses the official Ollama Python package with Pydantic for type validation.
"""
import asyncio
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


async def get_city_list() -> Cities:
    """Retrieve and parse city list from Ollama."""
    # Get structured response from Ollama
    async for response in chat(  # type: ignore
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": "List 5 cities from around the world and their countries",
            }
        ],
        format=Cities.model_json_schema(),
    ):
        if 'message' in response:
            # Parse and validate response
            return Cities.model_validate_json(response['message']['content'])

    raise RuntimeError("No valid response received from Ollama")


if __name__ == "__main__":
    city_list = asyncio.run(get_city_list())
    print(city_list)
```

### ollama_only_v1.sh

```bash
#!/bin/bash

curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "llama3.2",
  "messages": [{"role": "user", "content": "Tell me about Wales."}],
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "capital": {
        "type": "string"
      },
      "languages": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "name",
      "capital",
      "languages"
    ]
  }
}'
```

### ollama_only_v2.js

```javascript
/**
 * JavaScript implementation for extracting structured pet data from text using Ollama.
 * Uses Zod for schema validation and type safety.
 */
import ollama from 'ollama';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

// Define the schema using Zod
const Pet = z.object({
    name: z.string(),
    animal: z.string(),
    age: z.number(),
    color: z.string().nullable(),
    favorite_toy: z.string().nullable(),
});

const PetList = z.object({
    pets: z.array(Pet),
});

async function extractPetData() {
    try {
        const response = await ollama.chat({
            model: 'llama3.2:latest',
            messages: [{
                role: 'user',
                content: `
                    I have two pets.
                    A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                    I also have a 2 year old black cat named Loki who loves tennis balls.
                `
            }],
            format: zodToJsonSchema(PetList),
        });

        // Parse and validate the response using Zod
        const petData = PetList.parse(JSON.parse(response.message.content));
        console.log('Extracted Pet Data:', JSON.stringify(petData, null, 2));

        return petData;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Run the example
extractPetData();
```

### ollama_only_v2.py

```python
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
```

### ollama_only_v2.sh

```bash
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
```

### package-lock.json

```json
{
  "name": "ollama-structured-outputs-test-env",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "ollama": "^0.5.11",
        "zod": "^3.23.8",
        "zod-to-json-schema": "^3.23.5"
      }
    },
    "node_modules/ollama": {
      "version": "0.5.11",
      "resolved": "https://registry.npmjs.org/ollama/-/ollama-0.5.11.tgz",
      "integrity": "sha512-lDAKcpmBU3VAOGF05NcQipHNKTdpKfAHpZ7bjCsElkUkmX7SNZImi6lwIxz/l1zQtLq0S3wuLneRuiXxX2KIew==",
      "dependencies": {
        "whatwg-fetch": "^3.6.20"
      }
    },
    "node_modules/whatwg-fetch": {
      "version": "3.6.20",
      "resolved": "https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.6.20.tgz",
      "integrity": "sha512-EqhiFU6daOA8kpjOWTL0olhVOF3i7OrFzSYiGsEMB8GcXS+RrzauAERX65xMeNWVqxA6HXH2m69Z9LaKKdisfg=="
    },
    "node_modules/zod": {
      "version": "3.23.8",
      "resolved": "https://registry.npmjs.org/zod/-/zod-3.23.8.tgz",
      "integrity": "sha512-XBx9AXhXktjUqnepgTiE5flcKIYWi/rme0Eaj+5Y0lftuGBq+jyRu/md4WnuxqgP1ubdpNCsYEYPxrzVHD8d6g==",
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    },
    "node_modules/zod-to-json-schema": {
      "version": "3.23.5",
      "resolved": "https://registry.npmjs.org/zod-to-json-schema/-/zod-to-json-schema-3.23.5.tgz",
      "integrity": "sha512-5wlSS0bXfF/BrL4jPAbz9da5hDlDptdEppYfe+x4eIJ7jioqKG9uUxOwPzqof09u/XeVdrgFu29lZi+8XNDJtA==",
      "peerDependencies": {
        "zod": "^3.23.3"
      }
    }
  }
}
```

### package.json

```json
{
  "dependencies": {
    "ollama": "^0.5.11",
    "zod": "^3.23.8",
    "zod-to-json-schema": "^3.23.5"
  },
  "type": "module",
  "volta": {
    "node": "20.18.1"
  }
}
```

### pyproject.toml

```txt
[project]
name = "ollama-structured"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "instructor>=1.7.0",
    "ollama>=0.4.3",
]
```

### README.md

````markdown
# Ollama Structured Outputs

A demonstration project showing different approaches to getting structured outputs from Ollama using both JavaScript and Python implementations. The project focuses on type safety, proper error handling, and multiple implementation strategies.

[[toc]]

## Prerequisites

- Ollama installed and running
- Node.js 20 (managed via Volta)
- Python 3.12
- UV package manager for Python dependencies

## Installation

1. Clone the repository
2. Pull the required Ollama model:

```bash
ollama pull llama3.2:latest
```

### Python Setup

Install dependencies using UV:

```bash
uv pip install .
```

### JavaScript Setup

Install dependencies using npm:

```bash
npm install
```

## Implementations

### JavaScript Version

Uses Zod for runtime type validation and provides structured JSON outputs. Key features:

- Type safety with Zod
- Structured data output
- Schema validation
- ESM support

Run the JavaScript implementation:

```bash
node ollama_only.js
```

### Python Versions

Three different Python implementations are provided:

1. **Ollama Package (Async)**
   - Uses official Ollama Python package
   - Async/await for stream handling
   - Pydantic for type validation

   ```bash
   python ollama_only.py
   ```

2. **Instructor Implementation**
   - OpenAI-compatible interface
   - Built-in Pydantic integration

   ```bash
   python instructor_ollama.py
   ```

3. **Direct API Calls**
   - Raw HTTP requests to Ollama API
   - Comprehensive error handling

   ```bash
   python ollama_json.py
   ```

## Project Structure

- `ollama_only.js` - JavaScript implementation
- `ollama_only.py` - Python implementation using Ollama package
- `instructor_ollama.py` - Python implementation using Instructor
- `ollama_json.py` - Python implementation using direct API calls
- `pyproject.toml` - Python project configuration
- `package.json` - Node.js project configuration
- `uv.lock` - Python dependency lock file

## Features

- Multiple implementation approaches in both Python and JavaScript
- Type safety and validation
- Proper error handling
- Request timeouts
- Comprehensive documentation
- Linter compliance
- Async support (Python)

## Dependencies

### Python

- ollama: 0.4.4
- instructor: 1.7.0
- pydantic: 2.10.3
- openai: 1.57.0
- requests

### JavaScript

- ollama: ^0.5.11
- zod: ^3.23.8
- zod-to-json-schema: ^3.23.5

## Example Output

```javascript
{
  cities: [
    { name: 'Paris', country: 'France' },
    { name: 'Tokyo', country: 'Japan' },
    { name: 'Rio de Janeiro', country: 'Brazil' },
    { name: 'Beijing', country: 'China' },
    { name: 'Cape Town', country: 'South Africa' }
  ]
}
```

## Version Requirements

- Python: >=3.12
- Node.js: 20.x
````

### SETUP.md

````markdown
# Ollama Structured Outputs Setup

## Project Configuration

### Dependency Management

- Using `uv` package manager for Python dependencies
- `uv.lock` file ensures reproducible builds by:
  - Pinning exact package versions
  - Storing dependency hashes
  - Tracking Python version requirements (>=3.12)
- While not strictly necessary for this demo, keeping the lock file is good practice for reproducibility

### Initial Setup Commands

1. **Node.js Setup**

    ```bash
    # Install Node.js using Volta
    volta pin node@20
    volta install npm

    # Install JavaScript dependencies
    npm install
    ```

2. **Python Setup**

    ```bash
    # Install Python dependencies using uv
    uv pip install .
    ```

3. **Ollama Setup**

    ```bash
    # Pull required model
    ollama pull llama3.2:latest
    ```

## JavaScript Implementation

### Environment Setup JavaScript

1. **Node.js Environment**
   - Used Volta for Node.js version management
   - Pinned Node.js version 20 using Volta
   - Installed npm via Volta

2. **Dependencies**
   - ollama: ^0.5.11 (Ollama JavaScript client)
   - zod: ^3.23.8 (Runtime type checking)
   - zod-to-json-schema: ^3.23.5 (Converts Zod schemas to JSON Schema)

### Implementation Details

#### Schema Definition

```javascript
const City = z.object({
    name: z.string(),
    country: z.string(),
});

const Cities = z.object({
    cities: z.array(City)
})
```

### Ollama Integration

- Model: llama3.2:latest
- Using structured format output with JSON Schema
- Query: List of 5 cities from around the world and their countries

### Example Output

```javascript
{
  cities: [
    { name: 'Paris', country: 'France' },
    { name: 'Tokyo', country: 'Japan' },
    { name: 'Rio de Janeiro', country: 'Brazil' },
    { name: 'Beijing', country: 'China' },
    { name: 'Cape Town', country: 'South Africa' }
  ]
}
```

### Key Features

1. **Type Safety**: Using Zod for runtime type validation
2. **Structured Data**: Consistent JSON output format
3. **Schema Validation**: Automatic validation of LLM responses
4. **ESM Support**: Using ES modules for modern JavaScript

### Running the JavaScript Version

```bash
node ollama_only.js
```

## Python Implementations

### Environment Setup Python

1. **Python Environment**
   - Python 3.12 (configured via .python-version)
   - Using uv package manager for dependency management

2. **Dependencies** (installed via `uv pip install .`)
   - ollama: 0.4.4
   - instructor: 1.7.0
   - pydantic: 2.10.3
   - openai: 1.57.0
   - requests (for direct API calls)

### Implementation 1: Using Ollama Package (Async)

This implementation uses the official Ollama Python package with Pydantic for type validation and async/await for proper stream handling.

```python
async def get_city_list() -> Cities:
    """Retrieve and parse city list from Ollama."""
    async for response in chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": "List 5 cities..."}],
        format=Cities.model_json_schema(),
    ):
        if 'message' in response:
            return Cities.model_validate_json(response['message']['content'])

    raise RuntimeError("No valid response received from Ollama")

if __name__ == "__main__":
    city_list = asyncio.run(get_city_list())
```

### Implementation 2: Using Instructor

This implementation uses the Instructor package which provides an OpenAI-compatible interface with built-in Pydantic integration.

```python
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
    messages=[{"role": "user", "content": "List 5 cities..."}],
    response_model=Cities,
)
```

### Implementation 3: Direct API Calls

This implementation makes direct HTTP calls to Ollama's API endpoint with proper error handling and timeouts.

```python
try:
    response = requests.post(
        'http://localhost:11434/api/chat',
        json={
            "model": "llama3.2:latest",
            "messages": [{"role": "user", "content": "List 5 cities..."}],
            "format": "json",
            "stream": False
        },
        timeout=30  # 30 second timeout
    )

    if response.status_code == 200:
        result = json.loads(response.content)
        content_json = json.loads(result['message']['content'])
        cities_list = {
            "cities": [
                {"name": name.strip(), "country": country.strip()}
                for name, country in content_json.items()
            ]
        }

except (RequestException, json.JSONDecodeError) as e:
    print(f"Error occurred: {str(e)}")
```

### Key Features Across Python Implementations

1. **Multiple Approaches**:
   - Official Ollama package with async support
   - Instructor with OpenAI-compatible interface
   - Direct API calls with proper error handling

2. **Type Safety & Validation**:
   - Pydantic models for data validation
   - Runtime type checking
   - Proper type hints throughout

3. **Error Handling**:
   - Specific exception handling
   - Request timeouts
   - Proper async/await patterns

4. **Code Quality**:
   - Comprehensive docstrings
   - Proper import ordering
   - Type hints and annotations
   - Pylint compliance

### Running the Python Versions

```bash
# Run Ollama package implementation
python ollama_only.py

# Run Instructor implementation
python instructor_ollama.py

# Run direct API implementation
python ollama_json.py
```

Each implementation follows Python best practices and includes:

- Proper error handling
- Type hints and validation
- Comprehensive documentation
- Linter compliance
````

### uv.lock

```txt
version = 1
requires-python = ">=3.12"

[[package]]
name = "aiohappyeyeballs"
version = "2.4.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7f/55/e4373e888fdacb15563ef6fa9fa8c8252476ea071e96fb46defac9f18bf2/aiohappyeyeballs-2.4.4.tar.gz", hash = "sha256:5fdd7d87889c63183afc18ce9271f9b0a7d32c2303e394468dd45d514a757745", size = 21977 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b9/74/fbb6559de3607b3300b9be3cc64e97548d55678e44623db17820dbd20002/aiohappyeyeballs-2.4.4-py3-none-any.whl", hash = "sha256:a980909d50efcd44795c4afeca523296716d50cd756ddca6af8c65b996e27de8", size = 14756 },
]

[[package]]
name = "aiohttp"
version = "3.11.10"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "aiohappyeyeballs" },
    { name = "aiosignal" },
    { name = "attrs" },
    { name = "frozenlist" },
    { name = "multidict" },
    { name = "propcache" },
    { name = "yarl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/94/c4/3b5a937b16f6c2a0ada842a9066aad0b7a5708427d4a202a07bf09c67cbb/aiohttp-3.11.10.tar.gz", hash = "sha256:b1fc6b45010a8d0ff9e88f9f2418c6fd408c99c211257334aff41597ebece42e", size = 7668832 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/25/17/1dbe2f619f77795409c1a13ab395b98ed1b215d3e938cacde9b8ffdac53d/aiohttp-3.11.10-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:b78f053a7ecfc35f0451d961dacdc671f4bcbc2f58241a7c820e9d82559844cf", size = 704448 },
    { url = "https://files.pythonhosted.org/packages/e3/9b/112247ad47e9d7f6640889c6e42cc0ded8c8345dd0033c66bcede799b051/aiohttp-3.11.10-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:ab7485222db0959a87fbe8125e233b5a6f01f4400785b36e8a7878170d8c3138", size = 463829 },
    { url = "https://files.pythonhosted.org/packages/8a/36/a64b583771fc673062a7a1374728a6241d49e2eda5a9041fbf248e18c804/aiohttp-3.11.10-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:cf14627232dfa8730453752e9cdc210966490992234d77ff90bc8dc0dce361d5", size = 455774 },
    { url = "https://files.pythonhosted.org/packages/e5/75/ee1b8f510978b3de5f185c62535b135e4fc3f5a247ca0c2245137a02d800/aiohttp-3.11.10-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:076bc454a7e6fd646bc82ea7f98296be0b1219b5e3ef8a488afbdd8e81fbac50", size = 1682134 },
    { url = "https://files.pythonhosted.org/packages/87/46/65e8259432d5f73ca9ebf5edb645ef90e5303724e4e52477516cb4042240/aiohttp-3.11.10-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:482cafb7dc886bebeb6c9ba7925e03591a62ab34298ee70d3dd47ba966370d2c", size = 1736757 },
    { url = "https://files.pythonhosted.org/packages/03/f6/a6d1e791b7153fb2d101278f7146c0771b0e1569c547f8a8bc3035651984/aiohttp-3.11.10-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bf3d1a519a324af764a46da4115bdbd566b3c73fb793ffb97f9111dbc684fc4d", size = 1793033 },
    { url = "https://files.pythonhosted.org/packages/a8/e9/1ac90733e36e7848693aece522936a13bf17eeb617da662f94adfafc1c25/aiohttp-3.11.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:24213ba85a419103e641e55c27dc7ff03536c4873470c2478cce3311ba1eee7b", size = 1691609 },
    { url = "https://files.pythonhosted.org/packages/6d/a6/77b33da5a0bc04566c7ddcca94500f2c2a2334eecab4885387fffd1fc600/aiohttp-3.11.10-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b99acd4730ad1b196bfb03ee0803e4adac371ae8efa7e1cbc820200fc5ded109", size = 1619082 },
    { url = "https://files.pythonhosted.org/packages/48/94/5bf5f927d9a2fedd2c978adfb70a3680e16f46d178361685b56244eb52ed/aiohttp-3.11.10-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:14cdb5a9570be5a04eec2ace174a48ae85833c2aadc86de68f55541f66ce42ab", size = 1641186 },
    { url = "https://files.pythonhosted.org/packages/99/2d/e85103aa01d1064e51bc50cb51e7b40150a8ff5d34e5a3173a46b241860b/aiohttp-3.11.10-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:7e97d622cb083e86f18317282084bc9fbf261801b0192c34fe4b1febd9f7ae69", size = 1646280 },
    { url = "https://files.pythonhosted.org/packages/7b/e0/44651fda8c1d865a51b3a81f1956ea55ce16fc568fe7a3e05db7fc22f139/aiohttp-3.11.10-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:012f176945af138abc10c4a48743327a92b4ca9adc7a0e078077cdb5dbab7be0", size = 1701862 },
    { url = "https://files.pythonhosted.org/packages/4e/1e/0804459ae325a5b95f6f349778fb465f29d2b863e522b6a349db0aaad54c/aiohttp-3.11.10-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:44224d815853962f48fe124748227773acd9686eba6dc102578defd6fc99e8d9", size = 1734373 },
    { url = "https://files.pythonhosted.org/packages/07/87/b8f6721668cad74bcc9c7cfe6d0230b304d1250196b221e54294a0d78dbe/aiohttp-3.11.10-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:c87bf31b7fdab94ae3adbe4a48e711bfc5f89d21cf4c197e75561def39e223bc", size = 1694343 },
    { url = "https://files.pythonhosted.org/packages/4b/20/42813fc60d9178ba9b1b86c58a5441ddb6cf8ffdfe66387345bff173bcff/aiohttp-3.11.10-cp312-cp312-win32.whl", hash = "sha256:06a8e2ee1cbac16fe61e51e0b0c269400e781b13bcfc33f5425912391a542985", size = 411118 },
    { url = "https://files.pythonhosted.org/packages/3a/51/df9c263c861ce93998b5ad2ba3212caab2112d5b66dbe91ddbe90c41ded4/aiohttp-3.11.10-cp312-cp312-win_amd64.whl", hash = "sha256:be2b516f56ea883a3e14dda17059716593526e10fb6303189aaf5503937db408", size = 437424 },
    { url = "https://files.pythonhosted.org/packages/8c/1d/88bfdbe28a3d1ba5b94a235f188f27726caf8ade9a0e13574848f44fe0fe/aiohttp-3.11.10-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:8cc5203b817b748adccb07f36390feb730b1bc5f56683445bfe924fc270b8816", size = 697755 },
    { url = "https://files.pythonhosted.org/packages/86/00/4c4619d6fe5c5be32f74d1422fc719b3e6cd7097af0c9e03877ca9bd4ebc/aiohttp-3.11.10-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5ef359ebc6949e3a34c65ce20230fae70920714367c63afd80ea0c2702902ccf", size = 460440 },
    { url = "https://files.pythonhosted.org/packages/aa/1c/2f927408f50593a29465d198ec3c57c835c8602330233163e8d89c1093db/aiohttp-3.11.10-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9bca390cb247dbfaec3c664326e034ef23882c3f3bfa5fbf0b56cad0320aaca5", size = 452726 },
    { url = "https://files.pythonhosted.org/packages/06/6a/ff00ed0a2ba45c34b3c366aa5b0004b1a4adcec5a9b5f67dd0648ee1c88a/aiohttp-3.11.10-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:811f23b3351ca532af598405db1093f018edf81368e689d1b508c57dcc6b6a32", size = 1664944 },
    { url = "https://files.pythonhosted.org/packages/02/c2/61923f2a7c2e14d7424b3a526e054f0358f57ccdf5573d4d3d033b01921a/aiohttp-3.11.10-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:ddf5f7d877615f6a1e75971bfa5ac88609af3b74796ff3e06879e8422729fd01", size = 1717707 },
    { url = "https://files.pythonhosted.org/packages/8a/08/0d3d074b24d377569ec89d476a95ca918443099c0401bb31b331104e35d1/aiohttp-3.11.10-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6ab29b8a0beb6f8eaf1e5049252cfe74adbaafd39ba91e10f18caeb0e99ffb34", size = 1774890 },
    { url = "https://files.pythonhosted.org/packages/e8/49/052ada2b6e90ed65f0e6a7e548614621b5f8dcd193cb9415d2e6bcecc94a/aiohttp-3.11.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c49a76c1038c2dd116fa443eba26bbb8e6c37e924e2513574856de3b6516be99", size = 1676945 },
    { url = "https://files.pythonhosted.org/packages/7c/9e/0c48e1a48e072a869b8b5e3920c9f6a8092861524a4a6f159cd7e6fda939/aiohttp-3.11.10-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7f3dc0e330575f5b134918976a645e79adf333c0a1439dcf6899a80776c9ab39", size = 1602959 },
    { url = "https://files.pythonhosted.org/packages/ab/98/791f979093ff7f67f80344c182cb0ca4c2c60daed397ecaf454cc8d7a5cd/aiohttp-3.11.10-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:efb15a17a12497685304b2d976cb4939e55137df7b09fa53f1b6a023f01fcb4e", size = 1618058 },
    { url = "https://files.pythonhosted.org/packages/7b/5d/2d4b05feb3fd68eb7c8335f73c81079b56e582633b91002da695ccb439ef/aiohttp-3.11.10-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:db1d0b28fcb7f1d35600150c3e4b490775251dea70f894bf15c678fdd84eda6a", size = 1616289 },
    { url = "https://files.pythonhosted.org/packages/50/83/68cc28c00fe681dce6150614f105efe98282da19252cd6e32dfa893bb328/aiohttp-3.11.10-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:15fccaf62a4889527539ecb86834084ecf6e9ea70588efde86e8bc775e0e7542", size = 1685239 },
    { url = "https://files.pythonhosted.org/packages/16/f9/68fc5c8928f63238ce9314f04f3f59d9190a4db924998bb9be99c7aacce8/aiohttp-3.11.10-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:593c114a2221444f30749cc5e5f4012488f56bd14de2af44fe23e1e9894a9c60", size = 1715078 },
    { url = "https://files.pythonhosted.org/packages/3f/e0/3dd3f0451c532c77e35780bafb2b6469a046bc15a6ec2e039475a1d2f161/aiohttp-3.11.10-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:7852bbcb4d0d2f0c4d583f40c3bc750ee033265d80598d0f9cb6f372baa6b836", size = 1672544 },
    { url = "https://files.pythonhosted.org/packages/a5/b1/3530ab040dd5d7fb016b47115016f9b3a07ea29593b0e07e53dbe06a380c/aiohttp-3.11.10-cp313-cp313-win32.whl", hash = "sha256:65e55ca7debae8faaffee0ebb4b47a51b4075f01e9b641c31e554fd376595c6c", size = 409984 },
    { url = "https://files.pythonhosted.org/packages/49/1f/deed34e9fca639a7f873d01150d46925d3e1312051eaa591c1aa1f2e6ddc/aiohttp-3.11.10-cp313-cp313-win_amd64.whl", hash = "sha256:beb39a6d60a709ae3fb3516a1581777e7e8b76933bb88c8f4420d875bb0267c6", size = 435837 },
]

[[package]]
name = "aiosignal"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "frozenlist" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ae/67/0952ed97a9793b4958e5736f6d2b346b414a2cd63e82d05940032f45b32f/aiosignal-1.3.1.tar.gz", hash = "sha256:54cd96e15e1649b75d6c87526a6ff0b6c1b0dd3459f43d9ca11d48c339b68cfc", size = 19422 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/ac/a7305707cb852b7e16ff80eaf5692309bde30e2b1100a1fcacdc8f731d97/aiosignal-1.3.1-py3-none-any.whl", hash = "sha256:f8376fb07dd1e86a584e4fcdec80b36b7f81aac666ebc724e2c090300dd83b17", size = 7617 },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643 },
]

[[package]]
name = "anyio"
version = "4.7.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
    { name = "sniffio" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f6/40/318e58f669b1a9e00f5c4453910682e2d9dd594334539c7b7817dabb765f/anyio-4.7.0.tar.gz", hash = "sha256:2f834749c602966b7d456a7567cafcb309f96482b5081d14ac93ccd457f9dd48", size = 177076 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/7a/4daaf3b6c08ad7ceffea4634ec206faeff697526421c20f07628c7372156/anyio-4.7.0-py3-none-any.whl", hash = "sha256:ea60c3723ab42ba6fff7e8ccb0488c898ec538ff4df1f1d5e642c3601d07e352", size = 93052 },
]

[[package]]
name = "attrs"
version = "24.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/0f/aafca9af9315aee06a89ffde799a10a582fe8de76c563ee80bbcdc08b3fb/attrs-24.2.0.tar.gz", hash = "sha256:5cfb1b9148b5b086569baec03f20d7b6bf3bcacc9a42bebf87ffaaca362f6346", size = 792678 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6a/21/5b6702a7f963e95456c0de2d495f67bf5fd62840ac655dc451586d23d39a/attrs-24.2.0-py3-none-any.whl", hash = "sha256:81921eb96de3191c8258c199618104dd27ac608d9366f5e35d011eae1867ede2", size = 63001 },
]

[[package]]
name = "certifi"
version = "2024.8.30"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/ee/9b19140fe824b367c04c5e1b369942dd754c4c5462d5674002f75c4dedc1/certifi-2024.8.30.tar.gz", hash = "sha256:bec941d2aa8195e248a60b31ff9f0558284cf01a52591ceda73ea9afffd69fd9", size = 168507 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/90/3c9ff0512038035f59d279fddeb79f5f1eccd8859f06d6163c58798b9487/certifi-2024.8.30-py3-none-any.whl", hash = "sha256:922820b53db7a7257ffbda3f597266d435245903d80737e34f8a45ff3e3230d8", size = 167321 },
]

[[package]]
name = "charset-normalizer"
version = "3.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f2/4f/e1808dc01273379acc506d18f1504eb2d299bd4131743b9fc54d7be4df1e/charset_normalizer-3.4.0.tar.gz", hash = "sha256:223217c3d4f82c3ac5e29032b3f1c2eb0fb591b72161f86d93f5719079dae93e", size = 106620 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d3/0b/4b7a70987abf9b8196845806198975b6aab4ce016632f817ad758a5aa056/charset_normalizer-3.4.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:0713f3adb9d03d49d365b70b84775d0a0d18e4ab08d12bc46baa6132ba78aaf6", size = 194445 },
    { url = "https://files.pythonhosted.org/packages/50/89/354cc56cf4dd2449715bc9a0f54f3aef3dc700d2d62d1fa5bbea53b13426/charset_normalizer-3.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:de7376c29d95d6719048c194a9cf1a1b0393fbe8488a22008610b0361d834ecf", size = 125275 },
    { url = "https://files.pythonhosted.org/packages/fa/44/b730e2a2580110ced837ac083d8ad222343c96bb6b66e9e4e706e4d0b6df/charset_normalizer-3.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4a51b48f42d9358460b78725283f04bddaf44a9358197b889657deba38f329db", size = 119020 },
    { url = "https://files.pythonhosted.org/packages/9d/e4/9263b8240ed9472a2ae7ddc3e516e71ef46617fe40eaa51221ccd4ad9a27/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b295729485b06c1a0683af02a9e42d2caa9db04a373dc38a6a58cdd1e8abddf1", size = 139128 },
    { url = "https://files.pythonhosted.org/packages/6b/e3/9f73e779315a54334240353eaea75854a9a690f3f580e4bd85d977cb2204/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:ee803480535c44e7f5ad00788526da7d85525cfefaf8acf8ab9a310000be4b03", size = 149277 },
    { url = "https://files.pythonhosted.org/packages/1a/cf/f1f50c2f295312edb8a548d3fa56a5c923b146cd3f24114d5adb7e7be558/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3d59d125ffbd6d552765510e3f31ed75ebac2c7470c7274195b9161a32350284", size = 142174 },
    { url = "https://files.pythonhosted.org/packages/16/92/92a76dc2ff3a12e69ba94e7e05168d37d0345fa08c87e1fe24d0c2a42223/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8cda06946eac330cbe6598f77bb54e690b4ca93f593dee1568ad22b04f347c15", size = 143838 },
    { url = "https://files.pythonhosted.org/packages/a4/01/2117ff2b1dfc61695daf2babe4a874bca328489afa85952440b59819e9d7/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:07afec21bbbbf8a5cc3651aa96b980afe2526e7f048fdfb7f1014d84acc8b6d8", size = 146149 },
    { url = "https://files.pythonhosted.org/packages/f6/9b/93a332b8d25b347f6839ca0a61b7f0287b0930216994e8bf67a75d050255/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6b40e8d38afe634559e398cc32b1472f376a4099c75fe6299ae607e404c033b2", size = 140043 },
    { url = "https://files.pythonhosted.org/packages/ab/f6/7ac4a01adcdecbc7a7587767c776d53d369b8b971382b91211489535acf0/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:b8dcd239c743aa2f9c22ce674a145e0a25cb1566c495928440a181ca1ccf6719", size = 148229 },
    { url = "https://files.pythonhosted.org/packages/9d/be/5708ad18161dee7dc6a0f7e6cf3a88ea6279c3e8484844c0590e50e803ef/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:84450ba661fb96e9fd67629b93d2941c871ca86fc38d835d19d4225ff946a631", size = 151556 },
    { url = "https://files.pythonhosted.org/packages/5a/bb/3d8bc22bacb9eb89785e83e6723f9888265f3a0de3b9ce724d66bd49884e/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:44aeb140295a2f0659e113b31cfe92c9061622cadbc9e2a2f7b8ef6b1e29ef4b", size = 149772 },
    { url = "https://files.pythonhosted.org/packages/f7/fa/d3fc622de05a86f30beea5fc4e9ac46aead4731e73fd9055496732bcc0a4/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:1db4e7fefefd0f548d73e2e2e041f9df5c59e178b4c72fbac4cc6f535cfb1565", size = 144800 },
    { url = "https://files.pythonhosted.org/packages/9a/65/bdb9bc496d7d190d725e96816e20e2ae3a6fa42a5cac99c3c3d6ff884118/charset_normalizer-3.4.0-cp312-cp312-win32.whl", hash = "sha256:5726cf76c982532c1863fb64d8c6dd0e4c90b6ece9feb06c9f202417a31f7dd7", size = 94836 },
    { url = "https://files.pythonhosted.org/packages/3e/67/7b72b69d25b89c0b3cea583ee372c43aa24df15f0e0f8d3982c57804984b/charset_normalizer-3.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:b197e7094f232959f8f20541ead1d9862ac5ebea1d58e9849c1bf979255dfac9", size = 102187 },
    { url = "https://files.pythonhosted.org/packages/f3/89/68a4c86f1a0002810a27f12e9a7b22feb198c59b2f05231349fbce5c06f4/charset_normalizer-3.4.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:dd4eda173a9fcccb5f2e2bd2a9f423d180194b1bf17cf59e3269899235b2a114", size = 194617 },
    { url = "https://files.pythonhosted.org/packages/4f/cd/8947fe425e2ab0aa57aceb7807af13a0e4162cd21eee42ef5b053447edf5/charset_normalizer-3.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e9e3c4c9e1ed40ea53acf11e2a386383c3304212c965773704e4603d589343ed", size = 125310 },
    { url = "https://files.pythonhosted.org/packages/5b/f0/b5263e8668a4ee9becc2b451ed909e9c27058337fda5b8c49588183c267a/charset_normalizer-3.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:92a7e36b000bf022ef3dbb9c46bfe2d52c047d5e3f3343f43204263c5addc250", size = 119126 },
    { url = "https://files.pythonhosted.org/packages/ff/6e/e445afe4f7fda27a533f3234b627b3e515a1b9429bc981c9a5e2aa5d97b6/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:54b6a92d009cbe2fb11054ba694bc9e284dad30a26757b1e372a1fdddaf21920", size = 139342 },
    { url = "https://files.pythonhosted.org/packages/a1/b2/4af9993b532d93270538ad4926c8e37dc29f2111c36f9c629840c57cd9b3/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1ffd9493de4c922f2a38c2bf62b831dcec90ac673ed1ca182fe11b4d8e9f2a64", size = 149383 },
    { url = "https://files.pythonhosted.org/packages/fb/6f/4e78c3b97686b871db9be6f31d64e9264e889f8c9d7ab33c771f847f79b7/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:35c404d74c2926d0287fbd63ed5d27eb911eb9e4a3bb2c6d294f3cfd4a9e0c23", size = 142214 },
    { url = "https://files.pythonhosted.org/packages/2b/c9/1c8fe3ce05d30c87eff498592c89015b19fade13df42850aafae09e94f35/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4796efc4faf6b53a18e3d46343535caed491776a22af773f366534056c4e1fbc", size = 144104 },
    { url = "https://files.pythonhosted.org/packages/ee/68/efad5dcb306bf37db7db338338e7bb8ebd8cf38ee5bbd5ceaaaa46f257e6/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e7fdd52961feb4c96507aa649550ec2a0d527c086d284749b2f582f2d40a2e0d", size = 146255 },
    { url = "https://files.pythonhosted.org/packages/0c/75/1ed813c3ffd200b1f3e71121c95da3f79e6d2a96120163443b3ad1057505/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:92db3c28b5b2a273346bebb24857fda45601aef6ae1c011c0a997106581e8a88", size = 140251 },
    { url = "https://files.pythonhosted.org/packages/7d/0d/6f32255c1979653b448d3c709583557a4d24ff97ac4f3a5be156b2e6a210/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ab973df98fc99ab39080bfb0eb3a925181454d7c3ac8a1e695fddfae696d9e90", size = 148474 },
    { url = "https://files.pythonhosted.org/packages/ac/a0/c1b5298de4670d997101fef95b97ac440e8c8d8b4efa5a4d1ef44af82f0d/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:4b67fdab07fdd3c10bb21edab3cbfe8cf5696f453afce75d815d9d7223fbe88b", size = 151849 },
    { url = "https://files.pythonhosted.org/packages/04/4f/b3961ba0c664989ba63e30595a3ed0875d6790ff26671e2aae2fdc28a399/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:aa41e526a5d4a9dfcfbab0716c7e8a1b215abd3f3df5a45cf18a12721d31cb5d", size = 149781 },
    { url = "https://files.pythonhosted.org/packages/d8/90/6af4cd042066a4adad58ae25648a12c09c879efa4849c705719ba1b23d8c/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ffc519621dce0c767e96b9c53f09c5d215578e10b02c285809f76509a3931482", size = 144970 },
    { url = "https://files.pythonhosted.org/packages/cc/67/e5e7e0cbfefc4ca79025238b43cdf8a2037854195b37d6417f3d0895c4c2/charset_normalizer-3.4.0-cp313-cp313-win32.whl", hash = "sha256:f19c1585933c82098c2a520f8ec1227f20e339e33aca8fa6f956f6691b784e67", size = 94973 },
    { url = "https://files.pythonhosted.org/packages/65/97/fc9bbc54ee13d33dc54a7fcf17b26368b18505500fc01e228c27b5222d80/charset_normalizer-3.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:707b82d19e65c9bd28b81dde95249b07bf9f5b90ebe1ef17d9b57473f8a64b7b", size = 102308 },
    { url = "https://files.pythonhosted.org/packages/bf/9b/08c0432272d77b04803958a4598a51e2a4b51c06640af8b8f0f908c18bf2/charset_normalizer-3.4.0-py3-none-any.whl", hash = "sha256:fe9f97feb71aa9896b81973a7bbada8c49501dc73e58a10fcef6663af95e5079", size = 49446 },
]

[[package]]
name = "click"
version = "8.1.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "platform_system == 'Windows'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz", hash = "sha256:ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de", size = 336121 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl", hash = "sha256:ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28", size = 97941 },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335 },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277 },
]

[[package]]
name = "docstring-parser"
version = "0.16"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/08/12/9c22a58c0b1e29271051222d8906257616da84135af9ed167c9e28f85cb3/docstring_parser-0.16.tar.gz", hash = "sha256:538beabd0af1e2db0146b6bd3caa526c35a34d61af9fd2887f3a8a27a739aa6e", size = 26565 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d5/7c/e9fcff7623954d86bdc17782036cbf715ecab1bec4847c008557affe1ca8/docstring_parser-0.16-py3-none-any.whl", hash = "sha256:bf0a1387354d3691d102edef7ec124f219ef639982d096e26e3b60aeffa90637", size = 36533 },
]

[[package]]
name = "frozenlist"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8f/ed/0f4cec13a93c02c47ec32d81d11c0c1efbadf4a471e3f3ce7cad366cbbd3/frozenlist-1.5.0.tar.gz", hash = "sha256:81d5af29e61b9c8348e876d442253723928dce6433e0e76cd925cd83f1b4b817", size = 39930 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/79/73/fa6d1a96ab7fd6e6d1c3500700963eab46813847f01ef0ccbaa726181dd5/frozenlist-1.5.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:31115ba75889723431aa9a4e77d5f398f5cf976eea3bdf61749731f62d4a4a21", size = 94026 },
    { url = "https://files.pythonhosted.org/packages/ab/04/ea8bf62c8868b8eada363f20ff1b647cf2e93377a7b284d36062d21d81d1/frozenlist-1.5.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7437601c4d89d070eac8323f121fcf25f88674627505334654fd027b091db09d", size = 54150 },
    { url = "https://files.pythonhosted.org/packages/d0/9a/8e479b482a6f2070b26bda572c5e6889bb3ba48977e81beea35b5ae13ece/frozenlist-1.5.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7948140d9f8ece1745be806f2bfdf390127cf1a763b925c4a805c603df5e697e", size = 51927 },
    { url = "https://files.pythonhosted.org/packages/e3/12/2aad87deb08a4e7ccfb33600871bbe8f0e08cb6d8224371387f3303654d7/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:feeb64bc9bcc6b45c6311c9e9b99406660a9c05ca8a5b30d14a78555088b0b3a", size = 282647 },
    { url = "https://files.pythonhosted.org/packages/77/f2/07f06b05d8a427ea0060a9cef6e63405ea9e0d761846b95ef3fb3be57111/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:683173d371daad49cffb8309779e886e59c2f369430ad28fe715f66d08d4ab1a", size = 289052 },
    { url = "https://files.pythonhosted.org/packages/bd/9f/8bf45a2f1cd4aa401acd271b077989c9267ae8463e7c8b1eb0d3f561b65e/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7d57d8f702221405a9d9b40f9da8ac2e4a1a8b5285aac6100f3393675f0a85ee", size = 291719 },
    { url = "https://files.pythonhosted.org/packages/41/d1/1f20fd05a6c42d3868709b7604c9f15538a29e4f734c694c6bcfc3d3b935/frozenlist-1.5.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:30c72000fbcc35b129cb09956836c7d7abf78ab5416595e4857d1cae8d6251a6", size = 267433 },
    { url = "https://files.pythonhosted.org/packages/af/f2/64b73a9bb86f5a89fb55450e97cd5c1f84a862d4ff90d9fd1a73ab0f64a5/frozenlist-1.5.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:000a77d6034fbad9b6bb880f7ec073027908f1b40254b5d6f26210d2dab1240e", size = 283591 },
    { url = "https://files.pythonhosted.org/packages/29/e2/ffbb1fae55a791fd6c2938dd9ea779509c977435ba3940b9f2e8dc9d5316/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5d7f5a50342475962eb18b740f3beecc685a15b52c91f7d975257e13e029eca9", size = 273249 },
    { url = "https://files.pythonhosted.org/packages/2e/6e/008136a30798bb63618a114b9321b5971172a5abddff44a100c7edc5ad4f/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:87f724d055eb4785d9be84e9ebf0f24e392ddfad00b3fe036e43f489fafc9039", size = 271075 },
    { url = "https://files.pythonhosted.org/packages/ae/f0/4e71e54a026b06724cec9b6c54f0b13a4e9e298cc8db0f82ec70e151f5ce/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:6e9080bb2fb195a046e5177f10d9d82b8a204c0736a97a153c2466127de87784", size = 285398 },
    { url = "https://files.pythonhosted.org/packages/4d/36/70ec246851478b1c0b59f11ef8ade9c482ff447c1363c2bd5fad45098b12/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:9b93d7aaa36c966fa42efcaf716e6b3900438632a626fb09c049f6a2f09fc631", size = 294445 },
    { url = "https://files.pythonhosted.org/packages/37/e0/47f87544055b3349b633a03c4d94b405956cf2437f4ab46d0928b74b7526/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:52ef692a4bc60a6dd57f507429636c2af8b6046db8b31b18dac02cbc8f507f7f", size = 280569 },
    { url = "https://files.pythonhosted.org/packages/f9/7c/490133c160fb6b84ed374c266f42800e33b50c3bbab1652764e6e1fc498a/frozenlist-1.5.0-cp312-cp312-win32.whl", hash = "sha256:29d94c256679247b33a3dc96cce0f93cbc69c23bf75ff715919332fdbb6a32b8", size = 44721 },
    { url = "https://files.pythonhosted.org/packages/b1/56/4e45136ffc6bdbfa68c29ca56ef53783ef4c2fd395f7cbf99a2624aa9aaa/frozenlist-1.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:8969190d709e7c48ea386db202d708eb94bdb29207a1f269bab1196ce0dcca1f", size = 51329 },
    { url = "https://files.pythonhosted.org/packages/da/3b/915f0bca8a7ea04483622e84a9bd90033bab54bdf485479556c74fd5eaf5/frozenlist-1.5.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:7a1a048f9215c90973402e26c01d1cff8a209e1f1b53f72b95c13db61b00f953", size = 91538 },
    { url = "https://files.pythonhosted.org/packages/c7/d1/a7c98aad7e44afe5306a2b068434a5830f1470675f0e715abb86eb15f15b/frozenlist-1.5.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:dd47a5181ce5fcb463b5d9e17ecfdb02b678cca31280639255ce9d0e5aa67af0", size = 52849 },
    { url = "https://files.pythonhosted.org/packages/3a/c8/76f23bf9ab15d5f760eb48701909645f686f9c64fbb8982674c241fbef14/frozenlist-1.5.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:1431d60b36d15cda188ea222033eec8e0eab488f39a272461f2e6d9e1a8e63c2", size = 50583 },
    { url = "https://files.pythonhosted.org/packages/1f/22/462a3dd093d11df623179d7754a3b3269de3b42de2808cddef50ee0f4f48/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6482a5851f5d72767fbd0e507e80737f9c8646ae7fd303def99bfe813f76cf7f", size = 265636 },
    { url = "https://files.pythonhosted.org/packages/80/cf/e075e407fc2ae7328155a1cd7e22f932773c8073c1fc78016607d19cc3e5/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:44c49271a937625619e862baacbd037a7ef86dd1ee215afc298a417ff3270608", size = 270214 },
    { url = "https://files.pythonhosted.org/packages/a1/58/0642d061d5de779f39c50cbb00df49682832923f3d2ebfb0fedf02d05f7f/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:12f78f98c2f1c2429d42e6a485f433722b0061d5c0b0139efa64f396efb5886b", size = 273905 },
    { url = "https://files.pythonhosted.org/packages/ab/66/3fe0f5f8f2add5b4ab7aa4e199f767fd3b55da26e3ca4ce2cc36698e50c4/frozenlist-1.5.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ce3aa154c452d2467487765e3adc730a8c153af77ad84096bc19ce19a2400840", size = 250542 },
    { url = "https://files.pythonhosted.org/packages/f6/b8/260791bde9198c87a465224e0e2bb62c4e716f5d198fc3a1dacc4895dbd1/frozenlist-1.5.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9b7dc0c4338e6b8b091e8faf0db3168a37101943e687f373dce00959583f7439", size = 267026 },
    { url = "https://files.pythonhosted.org/packages/2e/a4/3d24f88c527f08f8d44ade24eaee83b2627793fa62fa07cbb7ff7a2f7d42/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:45e0896250900b5aa25180f9aec243e84e92ac84bd4a74d9ad4138ef3f5c97de", size = 257690 },
    { url = "https://files.pythonhosted.org/packages/de/9a/d311d660420b2beeff3459b6626f2ab4fb236d07afbdac034a4371fe696e/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:561eb1c9579d495fddb6da8959fd2a1fca2c6d060d4113f5844b433fc02f2641", size = 253893 },
    { url = "https://files.pythonhosted.org/packages/c6/23/e491aadc25b56eabd0f18c53bb19f3cdc6de30b2129ee0bc39cd387cd560/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:df6e2f325bfee1f49f81aaac97d2aa757c7646534a06f8f577ce184afe2f0a9e", size = 267006 },
    { url = "https://files.pythonhosted.org/packages/08/c4/ab918ce636a35fb974d13d666dcbe03969592aeca6c3ab3835acff01f79c/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:140228863501b44b809fb39ec56b5d4071f4d0aa6d216c19cbb08b8c5a7eadb9", size = 276157 },
    { url = "https://files.pythonhosted.org/packages/c0/29/3b7a0bbbbe5a34833ba26f686aabfe982924adbdcafdc294a7a129c31688/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:7707a25d6a77f5d27ea7dc7d1fc608aa0a478193823f88511ef5e6b8a48f9d03", size = 264642 },
    { url = "https://files.pythonhosted.org/packages/ab/42/0595b3dbffc2e82d7fe658c12d5a5bafcd7516c6bf2d1d1feb5387caa9c1/frozenlist-1.5.0-cp313-cp313-win32.whl", hash = "sha256:31a9ac2b38ab9b5a8933b693db4939764ad3f299fcaa931a3e605bc3460e693c", size = 44914 },
    { url = "https://files.pythonhosted.org/packages/17/c4/b7db1206a3fea44bf3b838ca61deb6f74424a8a5db1dd53ecb21da669be6/frozenlist-1.5.0-cp313-cp313-win_amd64.whl", hash = "sha256:11aabdd62b8b9c4b84081a3c246506d1cddd2dd93ff0ad53ede5defec7886b28", size = 51167 },
    { url = "https://files.pythonhosted.org/packages/c6/c8/a5be5b7550c10858fcf9b0ea054baccab474da77d37f1e828ce043a3a5d4/frozenlist-1.5.0-py3-none-any.whl", hash = "sha256:d994863bba198a4a518b467bb971c56e1db3f180a25c6cf7bb1949c267f748c3", size = 11901 },
]

[[package]]
name = "h11"
version = "0.14.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f5/38/3af3d3633a34a3316095b39c8e8fb4853a28a536e55d347bd8d8e9a14b03/h11-0.14.0.tar.gz", hash = "sha256:8f19fbbe99e72420ff35c00b27a34cb9937e902a8b810e2c88300c6f0a3b699d", size = 100418 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/95/04/ff642e65ad6b90db43e668d70ffb6736436c7ce41fcc549f4e9472234127/h11-0.14.0-py3-none-any.whl", hash = "sha256:e3fe4ac4b851c468cc8363d500db52c2ead036020723024a109d37346efaa761", size = 58259 },
]

[[package]]
name = "httpcore"
version = "1.0.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/6a/41/d7d0a89eb493922c37d343b607bc1b5da7f5be7e383740b4753ad8943e90/httpcore-1.0.7.tar.gz", hash = "sha256:8551cb62a169ec7162ac7be8d4817d561f60e08eaa485234898414bb5a8a0b4c", size = 85196 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/f5/72347bc88306acb359581ac4d52f23c0ef445b57157adedb9aee0cd689d2/httpcore-1.0.7-py3-none-any.whl", hash = "sha256:a3fff8f43dc260d5bd363d9f9cf1830fa3a458b332856f34282de498ed420edd", size = 78551 },
]

[[package]]
name = "httpx"
version = "0.27.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
    { name = "sniffio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/78/82/08f8c936781f67d9e6b9eeb8a0c8b4e406136ea4c3d1f89a5db71d42e0e6/httpx-0.27.2.tar.gz", hash = "sha256:f7c2be1d2f3c3c3160d441802406b206c2b76f5947b11115e6df10c6c65e66c2", size = 144189 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/56/95/9377bcb415797e44274b51d46e3249eba641711cf3348050f76ee7b15ffc/httpx-0.27.2-py3-none-any.whl", hash = "sha256:7bb2708e112d8fdd7829cd4243970f0c223274051cb35ee80c03301ee29a3df0", size = 76395 },
]

[[package]]
name = "idna"
version = "3.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442 },
]

[[package]]
name = "instructor"
version = "1.7.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "aiohttp" },
    { name = "docstring-parser" },
    { name = "jinja2" },
    { name = "jiter" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "pydantic-core" },
    { name = "requests" },
    { name = "rich" },
    { name = "tenacity" },
    { name = "typer" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b5/5f/5326d811f8cd59fc4fffbd629c91eeb82a345a2375ad34500c2755aab4d8/instructor-1.7.0.tar.gz", hash = "sha256:51b308ae9c5e4d56096514be785ac4f28f710c91bed80af74412fc21593431b3", size = 57079 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/07/84/2351df1678678f4a0a2c251f986d05e0ba090199f7a9f39e6d152b314946/instructor-1.7.0-py3-none-any.whl", hash = "sha256:0bff965d71a5398aed9d3f728e07ffb7b5050569c81f306c0e5a8d022071fe29", size = 70145 },
]

[[package]]
name = "jinja2"
version = "3.1.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ed/55/39036716d19cab0747a5020fc7e907f362fbf48c984b14e62127f7e68e5d/jinja2-3.1.4.tar.gz", hash = "sha256:4a3aee7acbbe7303aede8e9648d13b8bf88a429282aa6122a993f0ac800cb369", size = 240245 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/31/80/3a54838c3fb461f6fec263ebf3a3a41771bd05190238de3486aae8540c36/jinja2-3.1.4-py3-none-any.whl", hash = "sha256:bc5dd2abb727a5319567b7a813e6a2e7318c39f4f487cfe6c89c6f9c7d25197d", size = 133271 },
]

[[package]]
name = "jiter"
version = "0.6.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/26/ef/64458dfad180debd70d9dd1ca4f607e52bb6de748e5284d748556a0d5173/jiter-0.6.1.tar.gz", hash = "sha256:e19cd21221fc139fb032e4112986656cb2739e9fe6d84c13956ab30ccc7d4449", size = 161306 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2e/d5/fcdfbcea637f8b9b833597797d6b77fd7e22649b4794fc571674477c8520/jiter-0.6.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:1fad93654d5a7dcce0809aff66e883c98e2618b86656aeb2129db2cd6f26f867", size = 289279 },
    { url = "https://files.pythonhosted.org/packages/9a/47/8e4a7704a267b8d1d3287b4353fc07f1f4a3541b27988ea3e49ccbf3164a/jiter-0.6.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4e6e340e8cd92edab7f6a3a904dbbc8137e7f4b347c49a27da9814015cc0420c", size = 300931 },
    { url = "https://files.pythonhosted.org/packages/ea/4f/fbb1e11fcc3881d108359d3db8456715c9d30ddfce84dc5f9e0856e08e11/jiter-0.6.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:691352e5653af84ed71763c3c427cff05e4d658c508172e01e9c956dfe004aba", size = 336534 },
    { url = "https://files.pythonhosted.org/packages/29/8a/4c1e1229f89127187df166de760438b2a20e5a311391ba10d2b69db0da6f/jiter-0.6.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:defee3949313c1f5b55e18be45089970cdb936eb2a0063f5020c4185db1b63c9", size = 354266 },
    { url = "https://files.pythonhosted.org/packages/19/15/3f27f4b9d40bc7709a30fda99876cbe9e9f75a0ea2ef7d55f3dd4d04f927/jiter-0.6.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:26d2bdd5da097e624081c6b5d416d3ee73e5b13f1703bcdadbb1881f0caa1933", size = 370492 },
    { url = "https://files.pythonhosted.org/packages/1f/9d/9ec03c07325bc3a3c5b5082840b8ecb7e7ad38f3071c149b7c6fb9e78706/jiter-0.6.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:18aa9d1626b61c0734b973ed7088f8a3d690d0b7f5384a5270cd04f4d9f26c86", size = 390330 },
    { url = "https://files.pythonhosted.org/packages/bd/3b/612ea6daa52d64bc0cc46f2bd2e138952c58f1edbe86b17fd89e07c33d86/jiter-0.6.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7a3567c8228afa5ddcce950631c6b17397ed178003dc9ee7e567c4c4dcae9fa0", size = 324245 },
    { url = "https://files.pythonhosted.org/packages/21/0f/f3a1ffd9f203d4014b4e5045c0ea2c67ee71a7eee8bf3408dbf11007cf07/jiter-0.6.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e5c0507131c922defe3f04c527d6838932fcdfd69facebafd7d3574fa3395314", size = 368232 },
    { url = "https://files.pythonhosted.org/packages/62/12/5d75729e0a57804852de0affc6f03b3df8518259e47ed4cd89aeeb671a71/jiter-0.6.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:540fcb224d7dc1bcf82f90f2ffb652df96f2851c031adca3c8741cb91877143b", size = 513820 },
    { url = "https://files.pythonhosted.org/packages/5f/e8/e47734280e19cd465832e610e1c69367ee72947de738785c4b6fc4031e25/jiter-0.6.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:e7b75436d4fa2032b2530ad989e4cb0ca74c655975e3ff49f91a1a3d7f4e1df2", size = 496023 },
    { url = "https://files.pythonhosted.org/packages/52/01/5f65dd1387d39aa3fd4a98a5be1d8470e929a0cb0dd6cbfebaccd9a20ac5/jiter-0.6.1-cp312-none-win32.whl", hash = "sha256:883d2ced7c21bf06874fdeecab15014c1c6d82216765ca6deef08e335fa719e0", size = 197425 },
    { url = "https://files.pythonhosted.org/packages/43/b2/bd6665030f7d7cd5d9182c62a869c3d5ceadd7bff9f1b305de9192e7dbf8/jiter-0.6.1-cp312-none-win_amd64.whl", hash = "sha256:91e63273563401aadc6c52cca64a7921c50b29372441adc104127b910e98a5b6", size = 198966 },
    { url = "https://files.pythonhosted.org/packages/23/38/7b48e0149778ff4b893567c9fd997ecfcc013e290375aa7823e1f681b3d3/jiter-0.6.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:852508a54fe3228432e56019da8b69208ea622a3069458252f725d634e955b31", size = 288674 },
    { url = "https://files.pythonhosted.org/packages/85/3b/96d15b483d82a637279da53a1d299dd5da6e029b9905bcd1a4e1f89b8e4f/jiter-0.6.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f491cc69ff44e5a1e8bc6bf2b94c1f98d179e1aaf4a554493c171a5b2316b701", size = 301531 },
    { url = "https://files.pythonhosted.org/packages/cf/54/9681f112cbec4e197259e9db679bd4bc314f4bd24f74b9aa5e93073990b5/jiter-0.6.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cc56c8f0b2a28ad4d8047f3ae62d25d0e9ae01b99940ec0283263a04724de1f3", size = 335954 },
    { url = "https://files.pythonhosted.org/packages/4a/4d/f9c0ba82b154c66278e28348086086264ccf50622ae468ec215e4bbc2873/jiter-0.6.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:51b58f7a0d9e084a43b28b23da2b09fc5e8df6aa2b6a27de43f991293cab85fd", size = 353996 },
    { url = "https://files.pythonhosted.org/packages/ee/be/7f26b258ef190f6d582e21c76c7dd1097753a2203bad3e1643f45392720a/jiter-0.6.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5f79ce15099154c90ef900d69c6b4c686b64dfe23b0114e0971f2fecd306ec6c", size = 369733 },
    { url = "https://files.pythonhosted.org/packages/5f/85/037ed5261fa622312471ef5520b2135c26b29256c83adc16c8cc55dc4108/jiter-0.6.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:03a025b52009f47e53ea619175d17e4ded7c035c6fbd44935cb3ada11e1fd592", size = 389920 },
    { url = "https://files.pythonhosted.org/packages/a8/f3/2e01294712faa476be9e6ceb49e424c3919e03415ded76d103378a06bb80/jiter-0.6.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c74a8d93718137c021d9295248a87c2f9fdc0dcafead12d2930bc459ad40f885", size = 324138 },
    { url = "https://files.pythonhosted.org/packages/00/45/50377814f21b6412c7785be27f2dace225af52e0af20be7af899a7e3f264/jiter-0.6.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:40b03b75f903975f68199fc4ec73d546150919cb7e534f3b51e727c4d6ccca5a", size = 367610 },
    { url = "https://files.pythonhosted.org/packages/af/fc/51ba30875125381bfe21a1572c176de1a7dd64a386a7498355fc100decc4/jiter-0.6.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:825651a3f04cf92a661d22cad61fc913400e33aa89b3e3ad9a6aa9dc8a1f5a71", size = 512945 },
    { url = "https://files.pythonhosted.org/packages/69/60/af26168bd4916f9199ed433161e9f8a4eeda581a4e5982560d0f22dd146c/jiter-0.6.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:928bf25eb69ddb292ab8177fe69d3fbf76c7feab5fce1c09265a7dccf25d3991", size = 494963 },
    { url = "https://files.pythonhosted.org/packages/f3/2f/4f3cc5c9067a6fd1020d3c4365546535a69ed77da7fba2bec24368f3662c/jiter-0.6.1-cp313-none-win32.whl", hash = "sha256:352cd24121e80d3d053fab1cc9806258cad27c53cad99b7a3cac57cf934b12e4", size = 196869 },
    { url = "https://files.pythonhosted.org/packages/7a/fc/8709ee90837e94790d8b50db51c7b8a70e86e41b2c81e824c20b0ecfeba7/jiter-0.6.1-cp313-none-win_amd64.whl", hash = "sha256:be7503dd6f4bf02c2a9bacb5cc9335bc59132e7eee9d3e931b13d76fd80d7fda", size = 198919 },
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb", size = 74596 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", size = 87528 },
]

[[package]]
name = "markupsafe"
version = "3.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/97/5d42485e71dfc078108a86d6de8fa46db44a1a9295e89c5d6d4a06e23a62/markupsafe-3.0.2.tar.gz", hash = "sha256:ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0", size = 20537 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/22/09/d1f21434c97fc42f09d290cbb6350d44eb12f09cc62c9476effdb33a18aa/MarkupSafe-3.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:9778bd8ab0a994ebf6f84c2b949e65736d5575320a17ae8984a77fab08db94cf", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/6b/b0/18f76bba336fa5aecf79d45dcd6c806c280ec44538b3c13671d49099fdd0/MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:846ade7b71e3536c4e56b386c2a47adf5741d2d8b94ec9dc3e92e5e1ee1e2225", size = 12348 },
    { url = "https://files.pythonhosted.org/packages/e0/25/dd5c0f6ac1311e9b40f4af06c78efde0f3b5cbf02502f8ef9501294c425b/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1c99d261bd2d5f6b59325c92c73df481e05e57f19837bdca8413b9eac4bd8028", size = 24149 },
    { url = "https://files.pythonhosted.org/packages/f3/f0/89e7aadfb3749d0f52234a0c8c7867877876e0a20b60e2188e9850794c17/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e17c96c14e19278594aa4841ec148115f9c7615a47382ecb6b82bd8fea3ab0c8", size = 23118 },
    { url = "https://files.pythonhosted.org/packages/d5/da/f2eeb64c723f5e3777bc081da884b414671982008c47dcc1873d81f625b6/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:88416bd1e65dcea10bc7569faacb2c20ce071dd1f87539ca2ab364bf6231393c", size = 22993 },
    { url = "https://files.pythonhosted.org/packages/da/0e/1f32af846df486dce7c227fe0f2398dc7e2e51d4a370508281f3c1c5cddc/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:2181e67807fc2fa785d0592dc2d6206c019b9502410671cc905d132a92866557", size = 24178 },
    { url = "https://files.pythonhosted.org/packages/c4/f6/bb3ca0532de8086cbff5f06d137064c8410d10779c4c127e0e47d17c0b71/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:52305740fe773d09cffb16f8ed0427942901f00adedac82ec8b67752f58a1b22", size = 23319 },
    { url = "https://files.pythonhosted.org/packages/a2/82/8be4c96ffee03c5b4a034e60a31294daf481e12c7c43ab8e34a1453ee48b/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ad10d3ded218f1039f11a75f8091880239651b52e9bb592ca27de44eed242a48", size = 23352 },
    { url = "https://files.pythonhosted.org/packages/51/ae/97827349d3fcffee7e184bdf7f41cd6b88d9919c80f0263ba7acd1bbcb18/MarkupSafe-3.0.2-cp312-cp312-win32.whl", hash = "sha256:0f4ca02bea9a23221c0182836703cbf8930c5e9454bacce27e767509fa286a30", size = 15097 },
    { url = "https://files.pythonhosted.org/packages/c1/80/a61f99dc3a936413c3ee4e1eecac96c0da5ed07ad56fd975f1a9da5bc630/MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:8e06879fc22a25ca47312fbe7c8264eb0b662f6db27cb2d3bbbc74b1df4b9b87", size = 15601 },
    { url = "https://files.pythonhosted.org/packages/83/0e/67eb10a7ecc77a0c2bbe2b0235765b98d164d81600746914bebada795e97/MarkupSafe-3.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ba9527cdd4c926ed0760bc301f6728ef34d841f405abf9d4f959c478421e4efd", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/2b/6d/9409f3684d3335375d04e5f05744dfe7e9f120062c9857df4ab490a1031a/MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f8b3d067f2e40fe93e1ccdd6b2e1d16c43140e76f02fb1319a05cf2b79d99430", size = 12352 },
    { url = "https://files.pythonhosted.org/packages/d2/f5/6eadfcd3885ea85fe2a7c128315cc1bb7241e1987443d78c8fe712d03091/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:569511d3b58c8791ab4c2e1285575265991e6d8f8700c7be0e88f86cb0672094", size = 24122 },
    { url = "https://files.pythonhosted.org/packages/0c/91/96cf928db8236f1bfab6ce15ad070dfdd02ed88261c2afafd4b43575e9e9/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:15ab75ef81add55874e7ab7055e9c397312385bd9ced94920f2802310c930396", size = 23085 },
    { url = "https://files.pythonhosted.org/packages/c2/cf/c9d56af24d56ea04daae7ac0940232d31d5a8354f2b457c6d856b2057d69/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f3818cb119498c0678015754eba762e0d61e5b52d34c8b13d770f0719f7b1d79", size = 22978 },
    { url = "https://files.pythonhosted.org/packages/2a/9f/8619835cd6a711d6272d62abb78c033bda638fdc54c4e7f4272cf1c0962b/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:cdb82a876c47801bb54a690c5ae105a46b392ac6099881cdfb9f6e95e4014c6a", size = 24208 },
    { url = "https://files.pythonhosted.org/packages/f9/bf/176950a1792b2cd2102b8ffeb5133e1ed984547b75db47c25a67d3359f77/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cabc348d87e913db6ab4aa100f01b08f481097838bdddf7c7a84b7575b7309ca", size = 23357 },
    { url = "https://files.pythonhosted.org/packages/ce/4f/9a02c1d335caabe5c4efb90e1b6e8ee944aa245c1aaaab8e8a618987d816/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:444dcda765c8a838eaae23112db52f1efaf750daddb2d9ca300bcae1039adc5c", size = 23344 },
    { url = "https://files.pythonhosted.org/packages/ee/55/c271b57db36f748f0e04a759ace9f8f759ccf22b4960c270c78a394f58be/MarkupSafe-3.0.2-cp313-cp313-win32.whl", hash = "sha256:bcf3e58998965654fdaff38e58584d8937aa3096ab5354d493c77d1fdd66d7a1", size = 15101 },
    { url = "https://files.pythonhosted.org/packages/29/88/07df22d2dd4df40aba9f3e402e6dc1b8ee86297dddbad4872bd5e7b0094f/MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:e6a2a455bd412959b57a172ce6328d2dd1f01cb2135efda2e4576e8a23fa3b0f", size = 15603 },
    { url = "https://files.pythonhosted.org/packages/62/6a/8b89d24db2d32d433dffcd6a8779159da109842434f1dd2f6e71f32f738c/MarkupSafe-3.0.2-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:b5a6b3ada725cea8a5e634536b1b01c30bcdcd7f9c6fff4151548d5bf6b3a36c", size = 14510 },
    { url = "https://files.pythonhosted.org/packages/7a/06/a10f955f70a2e5a9bf78d11a161029d278eeacbd35ef806c3fd17b13060d/MarkupSafe-3.0.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:a904af0a6162c73e3edcb969eeeb53a63ceeb5d8cf642fade7d39e7963a22ddb", size = 12486 },
    { url = "https://files.pythonhosted.org/packages/34/cf/65d4a571869a1a9078198ca28f39fba5fbb910f952f9dbc5220afff9f5e6/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4aa4e5faecf353ed117801a068ebab7b7e09ffb6e1d5e412dc852e0da018126c", size = 25480 },
    { url = "https://files.pythonhosted.org/packages/0c/e3/90e9651924c430b885468b56b3d597cabf6d72be4b24a0acd1fa0e12af67/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0ef13eaeee5b615fb07c9a7dadb38eac06a0608b41570d8ade51c56539e509d", size = 23914 },
    { url = "https://files.pythonhosted.org/packages/66/8c/6c7cf61f95d63bb866db39085150df1f2a5bd3335298f14a66b48e92659c/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d16a81a06776313e817c951135cf7340a3e91e8c1ff2fac444cfd75fffa04afe", size = 23796 },
    { url = "https://files.pythonhosted.org/packages/bb/35/cbe9238ec3f47ac9a7c8b3df7a808e7cb50fe149dc7039f5f454b3fba218/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:6381026f158fdb7c72a168278597a5e3a5222e83ea18f543112b2662a9b699c5", size = 25473 },
    { url = "https://files.pythonhosted.org/packages/e6/32/7621a4382488aa283cc05e8984a9c219abad3bca087be9ec77e89939ded9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:3d79d162e7be8f996986c064d1c7c817f6df3a77fe3d6859f6f9e7be4b8c213a", size = 24114 },
    { url = "https://files.pythonhosted.org/packages/0d/80/0985960e4b89922cb5a0bac0ed39c5b96cbc1a536a99f30e8c220a996ed9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:131a3c7689c85f5ad20f9f6fb1b866f402c445b220c19fe4308c0b147ccd2ad9", size = 24098 },
    { url = "https://files.pythonhosted.org/packages/82/78/fedb03c7d5380df2427038ec8d973587e90561b2d90cd472ce9254cf348b/MarkupSafe-3.0.2-cp313-cp313t-win32.whl", hash = "sha256:ba8062ed2cf21c07a9e295d5b8a2a5ce678b913b45fdf68c32d95d6c1291e0b6", size = 15208 },
    { url = "https://files.pythonhosted.org/packages/4f/65/6079a46068dfceaeabb5dcad6d674f5f5c61a6fa5673746f42a9f4c233b3/MarkupSafe-3.0.2-cp313-cp313t-win_amd64.whl", hash = "sha256:e444a31f8db13eb18ada366ab3cf45fd4b31e4db1236a4448f68778c1d1a5a2f", size = 15739 },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979 },
]

[[package]]
name = "multidict"
version = "6.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/be/504b89a5e9ca731cd47487e91c469064f8ae5af93b7259758dcfc2b9c848/multidict-6.1.0.tar.gz", hash = "sha256:22ae2ebf9b0c69d206c003e2f6a914ea33f0a932d4aa16f236afc049d9958f4a", size = 64002 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fd/16/92057c74ba3b96d5e211b553895cd6dc7cc4d1e43d9ab8fafc727681ef71/multidict-6.1.0-cp312-cp312-macosx_10_9_universal2.whl", hash = "sha256:b04772ed465fa3cc947db808fa306d79b43e896beb677a56fb2347ca1a49c1fa", size = 48713 },
    { url = "https://files.pythonhosted.org/packages/94/3d/37d1b8893ae79716179540b89fc6a0ee56b4a65fcc0d63535c6f5d96f217/multidict-6.1.0-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:6180c0ae073bddeb5a97a38c03f30c233e0a4d39cd86166251617d1bbd0af436", size = 29516 },
    { url = "https://files.pythonhosted.org/packages/a2/12/adb6b3200c363062f805275b4c1e656be2b3681aada66c80129932ff0bae/multidict-6.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:071120490b47aa997cca00666923a83f02c7fbb44f71cf7f136df753f7fa8761", size = 29557 },
    { url = "https://files.pythonhosted.org/packages/47/e9/604bb05e6e5bce1e6a5cf80a474e0f072e80d8ac105f1b994a53e0b28c42/multidict-6.1.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:50b3a2710631848991d0bf7de077502e8994c804bb805aeb2925a981de58ec2e", size = 130170 },
    { url = "https://files.pythonhosted.org/packages/7e/13/9efa50801785eccbf7086b3c83b71a4fb501a4d43549c2f2f80b8787d69f/multidict-6.1.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:b58c621844d55e71c1b7f7c498ce5aa6985d743a1a59034c57a905b3f153c1ef", size = 134836 },
    { url = "https://files.pythonhosted.org/packages/bf/0f/93808b765192780d117814a6dfcc2e75de6dcc610009ad408b8814dca3ba/multidict-6.1.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:55b6d90641869892caa9ca42ff913f7ff1c5ece06474fbd32fb2cf6834726c95", size = 133475 },
    { url = "https://files.pythonhosted.org/packages/d3/c8/529101d7176fe7dfe1d99604e48d69c5dfdcadb4f06561f465c8ef12b4df/multidict-6.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4b820514bfc0b98a30e3d85462084779900347e4d49267f747ff54060cc33925", size = 131049 },
    { url = "https://files.pythonhosted.org/packages/ca/0c/fc85b439014d5a58063e19c3a158a889deec399d47b5269a0f3b6a2e28bc/multidict-6.1.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:10a9b09aba0c5b48c53761b7c720aaaf7cf236d5fe394cd399c7ba662d5f9966", size = 120370 },
    { url = "https://files.pythonhosted.org/packages/db/46/d4416eb20176492d2258fbd47b4abe729ff3b6e9c829ea4236f93c865089/multidict-6.1.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:1e16bf3e5fc9f44632affb159d30a437bfe286ce9e02754759be5536b169b305", size = 125178 },
    { url = "https://files.pythonhosted.org/packages/5b/46/73697ad7ec521df7de5531a32780bbfd908ded0643cbe457f981a701457c/multidict-6.1.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:76f364861c3bfc98cbbcbd402d83454ed9e01a5224bb3a28bf70002a230f73e2", size = 119567 },
    { url = "https://files.pythonhosted.org/packages/cd/ed/51f060e2cb0e7635329fa6ff930aa5cffa17f4c7f5c6c3ddc3500708e2f2/multidict-6.1.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:820c661588bd01a0aa62a1283f20d2be4281b086f80dad9e955e690c75fb54a2", size = 129822 },
    { url = "https://files.pythonhosted.org/packages/df/9e/ee7d1954b1331da3eddea0c4e08d9142da5f14b1321c7301f5014f49d492/multidict-6.1.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:0e5f362e895bc5b9e67fe6e4ded2492d8124bdf817827f33c5b46c2fe3ffaca6", size = 128656 },
    { url = "https://files.pythonhosted.org/packages/77/00/8538f11e3356b5d95fa4b024aa566cde7a38aa7a5f08f4912b32a037c5dc/multidict-6.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:3ec660d19bbc671e3a6443325f07263be452c453ac9e512f5eb935e7d4ac28b3", size = 125360 },
    { url = "https://files.pythonhosted.org/packages/be/05/5d334c1f2462d43fec2363cd00b1c44c93a78c3925d952e9a71caf662e96/multidict-6.1.0-cp312-cp312-win32.whl", hash = "sha256:58130ecf8f7b8112cdb841486404f1282b9c86ccb30d3519faf301b2e5659133", size = 26382 },
    { url = "https://files.pythonhosted.org/packages/a3/bf/f332a13486b1ed0496d624bcc7e8357bb8053823e8cd4b9a18edc1d97e73/multidict-6.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:188215fc0aafb8e03341995e7c4797860181562380f81ed0a87ff455b70bf1f1", size = 28529 },
    { url = "https://files.pythonhosted.org/packages/22/67/1c7c0f39fe069aa4e5d794f323be24bf4d33d62d2a348acdb7991f8f30db/multidict-6.1.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:d569388c381b24671589335a3be6e1d45546c2988c2ebe30fdcada8457a31008", size = 48771 },
    { url = "https://files.pythonhosted.org/packages/3c/25/c186ee7b212bdf0df2519eacfb1981a017bda34392c67542c274651daf23/multidict-6.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:052e10d2d37810b99cc170b785945421141bf7bb7d2f8799d431e7db229c385f", size = 29533 },
    { url = "https://files.pythonhosted.org/packages/67/5e/04575fd837e0958e324ca035b339cea174554f6f641d3fb2b4f2e7ff44a2/multidict-6.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f90c822a402cb865e396a504f9fc8173ef34212a342d92e362ca498cad308e28", size = 29595 },
    { url = "https://files.pythonhosted.org/packages/d3/b2/e56388f86663810c07cfe4a3c3d87227f3811eeb2d08450b9e5d19d78876/multidict-6.1.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b225d95519a5bf73860323e633a664b0d85ad3d5bede6d30d95b35d4dfe8805b", size = 130094 },
    { url = "https://files.pythonhosted.org/packages/6c/ee/30ae9b4186a644d284543d55d491fbd4239b015d36b23fea43b4c94f7052/multidict-6.1.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:23bfd518810af7de1116313ebd9092cb9aa629beb12f6ed631ad53356ed6b86c", size = 134876 },
    { url = "https://files.pythonhosted.org/packages/84/c7/70461c13ba8ce3c779503c70ec9d0345ae84de04521c1f45a04d5f48943d/multidict-6.1.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5c09fcfdccdd0b57867577b719c69e347a436b86cd83747f179dbf0cc0d4c1f3", size = 133500 },
    { url = "https://files.pythonhosted.org/packages/4a/9f/002af221253f10f99959561123fae676148dd730e2daa2cd053846a58507/multidict-6.1.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bf6bea52ec97e95560af5ae576bdac3aa3aae0b6758c6efa115236d9e07dae44", size = 131099 },
    { url = "https://files.pythonhosted.org/packages/82/42/d1c7a7301d52af79d88548a97e297f9d99c961ad76bbe6f67442bb77f097/multidict-6.1.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:57feec87371dbb3520da6192213c7d6fc892d5589a93db548331954de8248fd2", size = 120403 },
    { url = "https://files.pythonhosted.org/packages/68/f3/471985c2c7ac707547553e8f37cff5158030d36bdec4414cb825fbaa5327/multidict-6.1.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:0c3f390dc53279cbc8ba976e5f8035eab997829066756d811616b652b00a23a3", size = 125348 },
    { url = "https://files.pythonhosted.org/packages/67/2c/e6df05c77e0e433c214ec1d21ddd203d9a4770a1f2866a8ca40a545869a0/multidict-6.1.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:59bfeae4b25ec05b34f1956eaa1cb38032282cd4dfabc5056d0a1ec4d696d3aa", size = 119673 },
    { url = "https://files.pythonhosted.org/packages/c5/cd/bc8608fff06239c9fb333f9db7743a1b2eafe98c2666c9a196e867a3a0a4/multidict-6.1.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:b2f59caeaf7632cc633b5cf6fc449372b83bbdf0da4ae04d5be36118e46cc0aa", size = 129927 },
    { url = "https://files.pythonhosted.org/packages/44/8e/281b69b7bc84fc963a44dc6e0bbcc7150e517b91df368a27834299a526ac/multidict-6.1.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:37bb93b2178e02b7b618893990941900fd25b6b9ac0fa49931a40aecdf083fe4", size = 128711 },
    { url = "https://files.pythonhosted.org/packages/12/a4/63e7cd38ed29dd9f1881d5119f272c898ca92536cdb53ffe0843197f6c85/multidict-6.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4e9f48f58c2c523d5a06faea47866cd35b32655c46b443f163d08c6d0ddb17d6", size = 125519 },
    { url = "https://files.pythonhosted.org/packages/38/e0/4f5855037a72cd8a7a2f60a3952d9aa45feedb37ae7831642102604e8a37/multidict-6.1.0-cp313-cp313-win32.whl", hash = "sha256:3a37ffb35399029b45c6cc33640a92bef403c9fd388acce75cdc88f58bd19a81", size = 26426 },
    { url = "https://files.pythonhosted.org/packages/7e/a5/17ee3a4db1e310b7405f5d25834460073a8ccd86198ce044dfaf69eac073/multidict-6.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:e9aa71e15d9d9beaad2c6b9319edcdc0a49a43ef5c0a4c8265ca9ee7d6c67774", size = 28531 },
    { url = "https://files.pythonhosted.org/packages/99/b7/b9e70fde2c0f0c9af4cc5277782a89b66d35948ea3369ec9f598358c3ac5/multidict-6.1.0-py3-none-any.whl", hash = "sha256:48e171e52d1c4d33888e529b999e5900356b9ae588c2f09a52dcefb158b27506", size = 10051 },
]

[[package]]
name = "ollama"
version = "0.4.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "httpx" },
    { name = "pydantic" },
]
sdist = { url = "https://files.pythonhosted.org/packages/87/0f/c8141c044a618543a0a5928c9404866502d92ce41b9154d7c635b8dc4500/ollama-0.4.3.tar.gz", hash = "sha256:7b294051b2144be5d6ad4f0d033880f66b95a9377f4b40d8512e2974ca4001ef", size = 13078 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/a9/3af6f408b0851aca56c6badd86af5364aa5635dd2e397a72999d522297a8/ollama-0.4.3-py3-none-any.whl", hash = "sha256:4c06c6b4cd7df346a382e157f696ba53eb9ee2cc94db85a4f7d530b9acb9dba2", size = 13172 },
]

[[package]]
name = "ollama-structured"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "instructor" },
    { name = "ollama" },
]

[package.metadata]
requires-dist = [
    { name = "instructor", specifier = ">=1.7.0" },
    { name = "ollama", specifier = ">=0.4.3" },
]

[[package]]
name = "openai"
version = "1.57.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fa/64/4acd9331b3c0e1069f36692d4c29d2c8deea6649a1e150f45a096f91b339/openai-1.57.0.tar.gz", hash = "sha256:76f91971c4bdbd78380c9970581075e0337b5d497c2fbf7b5255078f4b31abf9", size = 315514 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ab/2d/eb8539a2d5809eb78508633a8faa8df7745960e99af0388310c43b2c0be1/openai-1.57.0-py3-none-any.whl", hash = "sha256:972e36960b821797952da3dc4532f486c28e28a2a332d7d0c5407f242e9d9c39", size = 389854 },
]

[[package]]
name = "propcache"
version = "0.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/20/c8/2a13f78d82211490855b2fb303b6721348d0787fdd9a12ac46d99d3acde1/propcache-0.2.1.tar.gz", hash = "sha256:3f77ce728b19cb537714499928fe800c3dda29e8d9428778fc7c186da4c09a64", size = 41735 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4c/28/1d205fe49be8b1b4df4c50024e62480a442b1a7b818e734308bb0d17e7fb/propcache-0.2.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:081a430aa8d5e8876c6909b67bd2d937bfd531b0382d3fdedb82612c618bc41a", size = 79588 },
    { url = "https://files.pythonhosted.org/packages/21/ee/fc4d893f8d81cd4971affef2a6cb542b36617cd1d8ce56b406112cb80bf7/propcache-0.2.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d2ccec9ac47cf4e04897619c0e0c1a48c54a71bdf045117d3a26f80d38ab1fb0", size = 45825 },
    { url = "https://files.pythonhosted.org/packages/4a/de/bbe712f94d088da1d237c35d735f675e494a816fd6f54e9db2f61ef4d03f/propcache-0.2.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:14d86fe14b7e04fa306e0c43cdbeebe6b2c2156a0c9ce56b815faacc193e320d", size = 45357 },
    { url = "https://files.pythonhosted.org/packages/7f/14/7ae06a6cf2a2f1cb382586d5a99efe66b0b3d0c6f9ac2f759e6f7af9d7cf/propcache-0.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:049324ee97bb67285b49632132db351b41e77833678432be52bdd0289c0e05e4", size = 241869 },
    { url = "https://files.pythonhosted.org/packages/cc/59/227a78be960b54a41124e639e2c39e8807ac0c751c735a900e21315f8c2b/propcache-0.2.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1cd9a1d071158de1cc1c71a26014dcdfa7dd3d5f4f88c298c7f90ad6f27bb46d", size = 247884 },
    { url = "https://files.pythonhosted.org/packages/84/58/f62b4ffaedf88dc1b17f04d57d8536601e4e030feb26617228ef930c3279/propcache-0.2.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:98110aa363f1bb4c073e8dcfaefd3a5cea0f0834c2aab23dda657e4dab2f53b5", size = 248486 },
    { url = "https://files.pythonhosted.org/packages/1c/07/ebe102777a830bca91bbb93e3479cd34c2ca5d0361b83be9dbd93104865e/propcache-0.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:647894f5ae99c4cf6bb82a1bb3a796f6e06af3caa3d32e26d2350d0e3e3faf24", size = 243649 },
    { url = "https://files.pythonhosted.org/packages/ed/bc/4f7aba7f08f520376c4bb6a20b9a981a581b7f2e385fa0ec9f789bb2d362/propcache-0.2.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bfd3223c15bebe26518d58ccf9a39b93948d3dcb3e57a20480dfdd315356baff", size = 229103 },
    { url = "https://files.pythonhosted.org/packages/fe/d5/04ac9cd4e51a57a96f78795e03c5a0ddb8f23ec098b86f92de028d7f2a6b/propcache-0.2.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:d71264a80f3fcf512eb4f18f59423fe82d6e346ee97b90625f283df56aee103f", size = 226607 },
    { url = "https://files.pythonhosted.org/packages/e3/f0/24060d959ea41d7a7cc7fdbf68b31852331aabda914a0c63bdb0e22e96d6/propcache-0.2.1-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:e73091191e4280403bde6c9a52a6999d69cdfde498f1fdf629105247599b57ec", size = 221153 },
    { url = "https://files.pythonhosted.org/packages/77/a7/3ac76045a077b3e4de4859a0753010765e45749bdf53bd02bc4d372da1a0/propcache-0.2.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:3935bfa5fede35fb202c4b569bb9c042f337ca4ff7bd540a0aa5e37131659348", size = 222151 },
    { url = "https://files.pythonhosted.org/packages/e7/af/5e29da6f80cebab3f5a4dcd2a3240e7f56f2c4abf51cbfcc99be34e17f0b/propcache-0.2.1-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:f508b0491767bb1f2b87fdfacaba5f7eddc2f867740ec69ece6d1946d29029a6", size = 233812 },
    { url = "https://files.pythonhosted.org/packages/8c/89/ebe3ad52642cc5509eaa453e9f4b94b374d81bae3265c59d5c2d98efa1b4/propcache-0.2.1-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:1672137af7c46662a1c2be1e8dc78cb6d224319aaa40271c9257d886be4363a6", size = 238829 },
    { url = "https://files.pythonhosted.org/packages/e9/2f/6b32f273fa02e978b7577159eae7471b3cfb88b48563b1c2578b2d7ca0bb/propcache-0.2.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b74c261802d3d2b85c9df2dfb2fa81b6f90deeef63c2db9f0e029a3cac50b518", size = 230704 },
    { url = "https://files.pythonhosted.org/packages/5c/2e/f40ae6ff5624a5f77edd7b8359b208b5455ea113f68309e2b00a2e1426b6/propcache-0.2.1-cp312-cp312-win32.whl", hash = "sha256:d09c333d36c1409d56a9d29b3a1b800a42c76a57a5a8907eacdbce3f18768246", size = 40050 },
    { url = "https://files.pythonhosted.org/packages/3b/77/a92c3ef994e47180862b9d7d11e37624fb1c00a16d61faf55115d970628b/propcache-0.2.1-cp312-cp312-win_amd64.whl", hash = "sha256:c214999039d4f2a5b2073ac506bba279945233da8c786e490d411dfc30f855c1", size = 44117 },
    { url = "https://files.pythonhosted.org/packages/0f/2a/329e0547cf2def8857157f9477669043e75524cc3e6251cef332b3ff256f/propcache-0.2.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:aca405706e0b0a44cc6bfd41fbe89919a6a56999157f6de7e182a990c36e37bc", size = 77002 },
    { url = "https://files.pythonhosted.org/packages/12/2d/c4df5415e2382f840dc2ecbca0eeb2293024bc28e57a80392f2012b4708c/propcache-0.2.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:12d1083f001ace206fe34b6bdc2cb94be66d57a850866f0b908972f90996b3e9", size = 44639 },
    { url = "https://files.pythonhosted.org/packages/d0/5a/21aaa4ea2f326edaa4e240959ac8b8386ea31dedfdaa636a3544d9e7a408/propcache-0.2.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:d93f3307ad32a27bda2e88ec81134b823c240aa3abb55821a8da553eed8d9439", size = 44049 },
    { url = "https://files.pythonhosted.org/packages/4e/3e/021b6cd86c0acc90d74784ccbb66808b0bd36067a1bf3e2deb0f3845f618/propcache-0.2.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ba278acf14471d36316159c94a802933d10b6a1e117b8554fe0d0d9b75c9d536", size = 224819 },
    { url = "https://files.pythonhosted.org/packages/3c/57/c2fdeed1b3b8918b1770a133ba5c43ad3d78e18285b0c06364861ef5cc38/propcache-0.2.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4e6281aedfca15301c41f74d7005e6e3f4ca143584ba696ac69df4f02f40d629", size = 229625 },
    { url = "https://files.pythonhosted.org/packages/9d/81/70d4ff57bf2877b5780b466471bebf5892f851a7e2ca0ae7ffd728220281/propcache-0.2.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5b750a8e5a1262434fb1517ddf64b5de58327f1adc3524a5e44c2ca43305eb0b", size = 232934 },
    { url = "https://files.pythonhosted.org/packages/3c/b9/bb51ea95d73b3fb4100cb95adbd4e1acaf2cbb1fd1083f5468eeb4a099a8/propcache-0.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bf72af5e0fb40e9babf594308911436c8efde3cb5e75b6f206c34ad18be5c052", size = 227361 },
    { url = "https://files.pythonhosted.org/packages/f1/20/3c6d696cd6fd70b29445960cc803b1851a1131e7a2e4ee261ee48e002bcd/propcache-0.2.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b2d0a12018b04f4cb820781ec0dffb5f7c7c1d2a5cd22bff7fb055a2cb19ebce", size = 213904 },
    { url = "https://files.pythonhosted.org/packages/a1/cb/1593bfc5ac6d40c010fa823f128056d6bc25b667f5393781e37d62f12005/propcache-0.2.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e800776a79a5aabdb17dcc2346a7d66d0777e942e4cd251defeb084762ecd17d", size = 212632 },
    { url = "https://files.pythonhosted.org/packages/6d/5c/e95617e222be14a34c709442a0ec179f3207f8a2b900273720501a70ec5e/propcache-0.2.1-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:4160d9283bd382fa6c0c2b5e017acc95bc183570cd70968b9202ad6d8fc48dce", size = 207897 },
    { url = "https://files.pythonhosted.org/packages/8e/3b/56c5ab3dc00f6375fbcdeefdede5adf9bee94f1fab04adc8db118f0f9e25/propcache-0.2.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:30b43e74f1359353341a7adb783c8f1b1c676367b011709f466f42fda2045e95", size = 208118 },
    { url = "https://files.pythonhosted.org/packages/86/25/d7ef738323fbc6ebcbce33eb2a19c5e07a89a3df2fded206065bd5e868a9/propcache-0.2.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:58791550b27d5488b1bb52bc96328456095d96206a250d28d874fafe11b3dfaf", size = 217851 },
    { url = "https://files.pythonhosted.org/packages/b3/77/763e6cef1852cf1ba740590364ec50309b89d1c818e3256d3929eb92fabf/propcache-0.2.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:0f022d381747f0dfe27e99d928e31bc51a18b65bb9e481ae0af1380a6725dd1f", size = 222630 },
    { url = "https://files.pythonhosted.org/packages/4f/e9/0f86be33602089c701696fbed8d8c4c07b6ee9605c5b7536fd27ed540c5b/propcache-0.2.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:297878dc9d0a334358f9b608b56d02e72899f3b8499fc6044133f0d319e2ec30", size = 216269 },
    { url = "https://files.pythonhosted.org/packages/cc/02/5ac83217d522394b6a2e81a2e888167e7ca629ef6569a3f09852d6dcb01a/propcache-0.2.1-cp313-cp313-win32.whl", hash = "sha256:ddfab44e4489bd79bda09d84c430677fc7f0a4939a73d2bba3073036f487a0a6", size = 39472 },
    { url = "https://files.pythonhosted.org/packages/f4/33/d6f5420252a36034bc8a3a01171bc55b4bff5df50d1c63d9caa50693662f/propcache-0.2.1-cp313-cp313-win_amd64.whl", hash = "sha256:556fc6c10989f19a179e4321e5d678db8eb2924131e64652a51fe83e4c3db0e1", size = 43363 },
    { url = "https://files.pythonhosted.org/packages/41/b6/c5319caea262f4821995dca2107483b94a3345d4607ad797c76cb9c36bcc/propcache-0.2.1-py3-none-any.whl", hash = "sha256:52277518d6aae65536e9cea52d4e7fd2f7a66f4aa2d30ed3f2fcea620ace3c54", size = 11818 },
]

[[package]]
name = "pydantic"
version = "2.10.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/45/0f/27908242621b14e649a84e62b133de45f84c255eecb350ab02979844a788/pydantic-2.10.3.tar.gz", hash = "sha256:cb5ac360ce894ceacd69c403187900a02c4b20b693a9dd1d643e1effab9eadf9", size = 786486 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/62/51/72c18c55cf2f46ff4f91ebcc8f75aa30f7305f3d726be3f4ebffb4ae972b/pydantic-2.10.3-py3-none-any.whl", hash = "sha256:be04d85bbc7b65651c5f8e6b9976ed9c6f41782a55524cef079a34a0bb82144d", size = 456997 },
]

[[package]]
name = "pydantic-core"
version = "2.27.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a6/9f/7de1f19b6aea45aeb441838782d68352e71bfa98ee6fa048d5041991b33e/pydantic_core-2.27.1.tar.gz", hash = "sha256:62a763352879b84aa31058fc931884055fd75089cccbd9d58bb6afd01141b235", size = 412785 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/be/51/2e9b3788feb2aebff2aa9dfbf060ec739b38c05c46847601134cc1fed2ea/pydantic_core-2.27.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:9cbd94fc661d2bab2bc702cddd2d3370bbdcc4cd0f8f57488a81bcce90c7a54f", size = 1895239 },
    { url = "https://files.pythonhosted.org/packages/7b/9e/f8063952e4a7d0127f5d1181addef9377505dcce3be224263b25c4f0bfd9/pydantic_core-2.27.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:5f8c4718cd44ec1580e180cb739713ecda2bdee1341084c1467802a417fe0f02", size = 1805070 },
    { url = "https://files.pythonhosted.org/packages/2c/9d/e1d6c4561d262b52e41b17a7ef8301e2ba80b61e32e94520271029feb5d8/pydantic_core-2.27.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:15aae984e46de8d376df515f00450d1522077254ef6b7ce189b38ecee7c9677c", size = 1828096 },
    { url = "https://files.pythonhosted.org/packages/be/65/80ff46de4266560baa4332ae3181fffc4488ea7d37282da1a62d10ab89a4/pydantic_core-2.27.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:1ba5e3963344ff25fc8c40da90f44b0afca8cfd89d12964feb79ac1411a260ac", size = 1857708 },
    { url = "https://files.pythonhosted.org/packages/d5/ca/3370074ad758b04d9562b12ecdb088597f4d9d13893a48a583fb47682cdf/pydantic_core-2.27.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:992cea5f4f3b29d6b4f7f1726ed8ee46c8331c6b4eed6db5b40134c6fe1768bb", size = 2037751 },
    { url = "https://files.pythonhosted.org/packages/b1/e2/4ab72d93367194317b99d051947c071aef6e3eb95f7553eaa4208ecf9ba4/pydantic_core-2.27.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:0325336f348dbee6550d129b1627cb8f5351a9dc91aad141ffb96d4937bd9529", size = 2733863 },
    { url = "https://files.pythonhosted.org/packages/8a/c6/8ae0831bf77f356bb73127ce5a95fe115b10f820ea480abbd72d3cc7ccf3/pydantic_core-2.27.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7597c07fbd11515f654d6ece3d0e4e5093edc30a436c63142d9a4b8e22f19c35", size = 2161161 },
    { url = "https://files.pythonhosted.org/packages/f1/f4/b2fe73241da2429400fc27ddeaa43e35562f96cf5b67499b2de52b528cad/pydantic_core-2.27.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:3bbd5d8cc692616d5ef6fbbbd50dbec142c7e6ad9beb66b78a96e9c16729b089", size = 1993294 },
    { url = "https://files.pythonhosted.org/packages/77/29/4bb008823a7f4cc05828198153f9753b3bd4c104d93b8e0b1bfe4e187540/pydantic_core-2.27.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:dc61505e73298a84a2f317255fcc72b710b72980f3a1f670447a21efc88f8381", size = 2001468 },
    { url = "https://files.pythonhosted.org/packages/f2/a9/0eaceeba41b9fad851a4107e0cf999a34ae8f0d0d1f829e2574f3d8897b0/pydantic_core-2.27.1-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:e1f735dc43da318cad19b4173dd1ffce1d84aafd6c9b782b3abc04a0d5a6f5bb", size = 2091413 },
    { url = "https://files.pythonhosted.org/packages/d8/36/eb8697729725bc610fd73940f0d860d791dc2ad557faaefcbb3edbd2b349/pydantic_core-2.27.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:f4e5658dbffe8843a0f12366a4c2d1c316dbe09bb4dfbdc9d2d9cd6031de8aae", size = 2154735 },
    { url = "https://files.pythonhosted.org/packages/52/e5/4f0fbd5c5995cc70d3afed1b5c754055bb67908f55b5cb8000f7112749bf/pydantic_core-2.27.1-cp312-none-win32.whl", hash = "sha256:672ebbe820bb37988c4d136eca2652ee114992d5d41c7e4858cdd90ea94ffe5c", size = 1833633 },
    { url = "https://files.pythonhosted.org/packages/ee/f2/c61486eee27cae5ac781305658779b4a6b45f9cc9d02c90cb21b940e82cc/pydantic_core-2.27.1-cp312-none-win_amd64.whl", hash = "sha256:66ff044fd0bb1768688aecbe28b6190f6e799349221fb0de0e6f4048eca14c16", size = 1986973 },
    { url = "https://files.pythonhosted.org/packages/df/a6/e3f12ff25f250b02f7c51be89a294689d175ac76e1096c32bf278f29ca1e/pydantic_core-2.27.1-cp312-none-win_arm64.whl", hash = "sha256:9a3b0793b1bbfd4146304e23d90045f2a9b5fd5823aa682665fbdaf2a6c28f3e", size = 1883215 },
    { url = "https://files.pythonhosted.org/packages/0f/d6/91cb99a3c59d7b072bded9959fbeab0a9613d5a4935773c0801f1764c156/pydantic_core-2.27.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:f216dbce0e60e4d03e0c4353c7023b202d95cbaeff12e5fd2e82ea0a66905073", size = 1895033 },
    { url = "https://files.pythonhosted.org/packages/07/42/d35033f81a28b27dedcade9e967e8a40981a765795c9ebae2045bcef05d3/pydantic_core-2.27.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:a2e02889071850bbfd36b56fd6bc98945e23670773bc7a76657e90e6b6603c08", size = 1807542 },
    { url = "https://files.pythonhosted.org/packages/41/c2/491b59e222ec7e72236e512108ecad532c7f4391a14e971c963f624f7569/pydantic_core-2.27.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:42b0e23f119b2b456d07ca91b307ae167cc3f6c846a7b169fca5326e32fdc6cf", size = 1827854 },
    { url = "https://files.pythonhosted.org/packages/e3/f3/363652651779113189cefdbbb619b7b07b7a67ebb6840325117cc8cc3460/pydantic_core-2.27.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:764be71193f87d460a03f1f7385a82e226639732214b402f9aa61f0d025f0737", size = 1857389 },
    { url = "https://files.pythonhosted.org/packages/5f/97/be804aed6b479af5a945daec7538d8bf358d668bdadde4c7888a2506bdfb/pydantic_core-2.27.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1c00666a3bd2f84920a4e94434f5974d7bbc57e461318d6bb34ce9cdbbc1f6b2", size = 2037934 },
    { url = "https://files.pythonhosted.org/packages/42/01/295f0bd4abf58902917e342ddfe5f76cf66ffabfc57c2e23c7681a1a1197/pydantic_core-2.27.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3ccaa88b24eebc0f849ce0a4d09e8a408ec5a94afff395eb69baf868f5183107", size = 2735176 },
    { url = "https://files.pythonhosted.org/packages/9d/a0/cd8e9c940ead89cc37812a1a9f310fef59ba2f0b22b4e417d84ab09fa970/pydantic_core-2.27.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c65af9088ac534313e1963443d0ec360bb2b9cba6c2909478d22c2e363d98a51", size = 2160720 },
    { url = "https://files.pythonhosted.org/packages/73/ae/9d0980e286627e0aeca4c352a60bd760331622c12d576e5ea4441ac7e15e/pydantic_core-2.27.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:206b5cf6f0c513baffaeae7bd817717140770c74528f3e4c3e1cec7871ddd61a", size = 1992972 },
    { url = "https://files.pythonhosted.org/packages/bf/ba/ae4480bc0292d54b85cfb954e9d6bd226982949f8316338677d56541b85f/pydantic_core-2.27.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:062f60e512fc7fff8b8a9d680ff0ddaaef0193dba9fa83e679c0c5f5fbd018bc", size = 2001477 },
    { url = "https://files.pythonhosted.org/packages/55/b7/e26adf48c2f943092ce54ae14c3c08d0d221ad34ce80b18a50de8ed2cba8/pydantic_core-2.27.1-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:a0697803ed7d4af5e4c1adf1670af078f8fcab7a86350e969f454daf598c4960", size = 2091186 },
    { url = "https://files.pythonhosted.org/packages/ba/cc/8491fff5b608b3862eb36e7d29d36a1af1c945463ca4c5040bf46cc73f40/pydantic_core-2.27.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:58ca98a950171f3151c603aeea9303ef6c235f692fe555e883591103da709b23", size = 2154429 },
    { url = "https://files.pythonhosted.org/packages/78/d8/c080592d80edd3441ab7f88f865f51dae94a157fc64283c680e9f32cf6da/pydantic_core-2.27.1-cp313-none-win32.whl", hash = "sha256:8065914ff79f7eab1599bd80406681f0ad08f8e47c880f17b416c9f8f7a26d05", size = 1833713 },
    { url = "https://files.pythonhosted.org/packages/83/84/5ab82a9ee2538ac95a66e51f6838d6aba6e0a03a42aa185ad2fe404a4e8f/pydantic_core-2.27.1-cp313-none-win_amd64.whl", hash = "sha256:ba630d5e3db74c79300d9a5bdaaf6200172b107f263c98a0539eeecb857b2337", size = 1987897 },
    { url = "https://files.pythonhosted.org/packages/df/c3/b15fb833926d91d982fde29c0624c9f225da743c7af801dace0d4e187e71/pydantic_core-2.27.1-cp313-none-win_arm64.whl", hash = "sha256:45cf8588c066860b623cd11c4ba687f8d7175d5f7ef65f7129df8a394c502de5", size = 1882983 },
]

[[package]]
name = "pygments"
version = "2.18.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8e/62/8336eff65bcbc8e4cb5d05b55faf041285951b6e80f33e2bff2024788f31/pygments-2.18.0.tar.gz", hash = "sha256:786ff802f32e91311bff3889f6e9a86e81505fe99f2735bb6d60ae0c5004f199", size = 4891905 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/3f/01c8b82017c199075f8f788d0d906b9ffbbc5a47dc9918a945e13d5a2bda/pygments-2.18.0-py3-none-any.whl", hash = "sha256:b8e6aca0523f3ab76fee51799c488e38782ac06eafcf95e7ba832985c8e7b13a", size = 1205513 },
]

[[package]]
name = "requests"
version = "2.32.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/63/70/2bf7780ad2d390a8d301ad0b550f1581eadbd9a20f896afe06353c2a2913/requests-2.32.3.tar.gz", hash = "sha256:55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760", size = 131218 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl", hash = "sha256:70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6", size = 64928 },
]

[[package]]
name = "rich"
version = "13.9.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ab/3a/0316b28d0761c6734d6bc14e770d85506c986c85ffb239e688eeaab2c2bc/rich-13.9.4.tar.gz", hash = "sha256:439594978a49a09530cff7ebc4b5c7103ef57baf48d5ea3184f21d9a2befa098", size = 223149 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/19/71/39c7c0d87f8d4e6c020a393182060eaefeeae6c01dab6a84ec346f2567df/rich-13.9.4-py3-none-any.whl", hash = "sha256:6049d5e6ec054bf2779ab3358186963bac2ea89175919d699e378b99738c2a90", size = 242424 },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755 },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235 },
]

[[package]]
name = "tenacity"
version = "9.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cd/94/91fccdb4b8110642462e653d5dcb27e7b674742ad68efd146367da7bdb10/tenacity-9.0.0.tar.gz", hash = "sha256:807f37ca97d62aa361264d497b0e31e92b8027044942bfa756160d908320d73b", size = 47421 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b6/cb/b86984bed139586d01532a587464b5805f12e397594f19f931c4c2fbfa61/tenacity-9.0.0-py3-none-any.whl", hash = "sha256:93de0c98785b27fcf659856aa9f54bfbd399e29969b0621bc7f762bd441b4539", size = 28169 },
]

[[package]]
name = "tqdm"
version = "4.67.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "platform_system == 'Windows'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a8/4b/29b4ef32e036bb34e4ab51796dd745cdba7ed47ad142a9f4a1eb8e0c744d/tqdm-4.67.1.tar.gz", hash = "sha256:f8aef9c52c08c13a65f30ea34f4e5aac3fd1a34959879d7e59e63027286627f2", size = 169737 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl", hash = "sha256:26445eca388f82e72884e0d580d5464cd801a3ea01e63e5601bdff9ba6a48de2", size = 78540 },
]

[[package]]
name = "typer"
version = "0.15.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/cb/ce/dca7b219718afd37a0068f4f2530a727c2b74a8b6e8e0c0080a4c0de4fcd/typer-0.15.1.tar.gz", hash = "sha256:a0588c0a7fa68a1978a069818657778f86abe6ff5ea6abf472f940a08bfe4f0a", size = 99789 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/cc/0a838ba5ca64dc832aa43f727bd586309846b0ffb2ce52422543e6075e8a/typer-0.15.1-py3-none-any.whl", hash = "sha256:7994fb7b8155b64d3402518560648446072864beefd44aa2dc36972a5972e847", size = 44908 },
]

[[package]]
name = "typing-extensions"
version = "4.12.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/df/db/f35a00659bc03fec321ba8bce9420de607a1d37f8342eee1863174c69557/typing_extensions-4.12.2.tar.gz", hash = "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8", size = 85321 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/26/9f/ad63fc0248c5379346306f8668cda6e2e2e9c95e01216d2b8ffd9ff037d0/typing_extensions-4.12.2-py3-none-any.whl", hash = "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d", size = 37438 },
]

[[package]]
name = "urllib3"
version = "2.2.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ed/63/22ba4ebfe7430b76388e7cd448d5478814d3032121827c12a2cc287e2260/urllib3-2.2.3.tar.gz", hash = "sha256:e7d814a81dad81e6caf2ec9fdedb284ecc9c73076b62654547cc64ccdcae26e9", size = 300677 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ce/d9/5f4c13cecde62396b0d3fe530a50ccea91e7dfc1ccf0e09c228841bb5ba8/urllib3-2.2.3-py3-none-any.whl", hash = "sha256:ca899ca043dcb1bafa3e262d73aa25c465bfb49e0bd9dd5d59f1d0acba2f8fac", size = 126338 },
]

[[package]]
name = "yarl"
version = "1.18.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
    { name = "multidict" },
    { name = "propcache" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b7/9d/4b94a8e6d2b51b599516a5cb88e5bc99b4d8d4583e468057eaa29d5f0918/yarl-1.18.3.tar.gz", hash = "sha256:ac1801c45cbf77b6c99242eeff4fffb5e4e73a800b5c4ad4fc0be5def634d2e1", size = 181062 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/33/85/bd2e2729752ff4c77338e0102914897512e92496375e079ce0150a6dc306/yarl-1.18.3-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:1dd4bdd05407ced96fed3d7f25dbbf88d2ffb045a0db60dbc247f5b3c5c25d50", size = 142644 },
    { url = "https://files.pythonhosted.org/packages/ff/74/1178322cc0f10288d7eefa6e4a85d8d2e28187ccab13d5b844e8b5d7c88d/yarl-1.18.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7c33dd1931a95e5d9a772d0ac5e44cac8957eaf58e3c8da8c1414de7dd27c576", size = 94962 },
    { url = "https://files.pythonhosted.org/packages/be/75/79c6acc0261e2c2ae8a1c41cf12265e91628c8c58ae91f5ff59e29c0787f/yarl-1.18.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:25b411eddcfd56a2f0cd6a384e9f4f7aa3efee14b188de13048c25b5e91f1640", size = 92795 },
    { url = "https://files.pythonhosted.org/packages/6b/32/927b2d67a412c31199e83fefdce6e645247b4fb164aa1ecb35a0f9eb2058/yarl-1.18.3-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:436c4fc0a4d66b2badc6c5fc5ef4e47bb10e4fd9bf0c79524ac719a01f3607c2", size = 332368 },
    { url = "https://files.pythonhosted.org/packages/19/e5/859fca07169d6eceeaa4fde1997c91d8abde4e9a7c018e371640c2da2b71/yarl-1.18.3-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e35ef8683211db69ffe129a25d5634319a677570ab6b2eba4afa860f54eeaf75", size = 342314 },
    { url = "https://files.pythonhosted.org/packages/08/75/76b63ccd91c9e03ab213ef27ae6add2e3400e77e5cdddf8ed2dbc36e3f21/yarl-1.18.3-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:84b2deecba4a3f1a398df819151eb72d29bfeb3b69abb145a00ddc8d30094512", size = 341987 },
    { url = "https://files.pythonhosted.org/packages/1a/e1/a097d5755d3ea8479a42856f51d97eeff7a3a7160593332d98f2709b3580/yarl-1.18.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:00e5a1fea0fd4f5bfa7440a47eff01d9822a65b4488f7cff83155a0f31a2ecba", size = 336914 },
    { url = "https://files.pythonhosted.org/packages/0b/42/e1b4d0e396b7987feceebe565286c27bc085bf07d61a59508cdaf2d45e63/yarl-1.18.3-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d0e883008013c0e4aef84dcfe2a0b172c4d23c2669412cf5b3371003941f72bb", size = 325765 },
    { url = "https://files.pythonhosted.org/packages/7e/18/03a5834ccc9177f97ca1bbb245b93c13e58e8225276f01eedc4cc98ab820/yarl-1.18.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5a3f356548e34a70b0172d8890006c37be92995f62d95a07b4a42e90fba54272", size = 344444 },
    { url = "https://files.pythonhosted.org/packages/c8/03/a713633bdde0640b0472aa197b5b86e90fbc4c5bc05b727b714cd8a40e6d/yarl-1.18.3-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:ccd17349166b1bee6e529b4add61727d3f55edb7babbe4069b5764c9587a8cc6", size = 340760 },
    { url = "https://files.pythonhosted.org/packages/eb/99/f6567e3f3bbad8fd101886ea0276c68ecb86a2b58be0f64077396cd4b95e/yarl-1.18.3-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:b958ddd075ddba5b09bb0be8a6d9906d2ce933aee81100db289badbeb966f54e", size = 346484 },
    { url = "https://files.pythonhosted.org/packages/8e/a9/84717c896b2fc6cb15bd4eecd64e34a2f0a9fd6669e69170c73a8b46795a/yarl-1.18.3-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:c7d79f7d9aabd6011004e33b22bc13056a3e3fb54794d138af57f5ee9d9032cb", size = 359864 },
    { url = "https://files.pythonhosted.org/packages/1e/2e/d0f5f1bef7ee93ed17e739ec8dbcb47794af891f7d165fa6014517b48169/yarl-1.18.3-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:4891ed92157e5430874dad17b15eb1fda57627710756c27422200c52d8a4e393", size = 364537 },
    { url = "https://files.pythonhosted.org/packages/97/8a/568d07c5d4964da5b02621a517532adb8ec5ba181ad1687191fffeda0ab6/yarl-1.18.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ce1af883b94304f493698b00d0f006d56aea98aeb49d75ec7d98cd4a777e9285", size = 357861 },
    { url = "https://files.pythonhosted.org/packages/7d/e3/924c3f64b6b3077889df9a1ece1ed8947e7b61b0a933f2ec93041990a677/yarl-1.18.3-cp312-cp312-win32.whl", hash = "sha256:f91c4803173928a25e1a55b943c81f55b8872f0018be83e3ad4938adffb77dd2", size = 84097 },
    { url = "https://files.pythonhosted.org/packages/34/45/0e055320daaabfc169b21ff6174567b2c910c45617b0d79c68d7ab349b02/yarl-1.18.3-cp312-cp312-win_amd64.whl", hash = "sha256:7e2ee16578af3b52ac2f334c3b1f92262f47e02cc6193c598502bd46f5cd1477", size = 90399 },
    { url = "https://files.pythonhosted.org/packages/30/c7/c790513d5328a8390be8f47be5d52e141f78b66c6c48f48d241ca6bd5265/yarl-1.18.3-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:90adb47ad432332d4f0bc28f83a5963f426ce9a1a8809f5e584e704b82685dcb", size = 140789 },
    { url = "https://files.pythonhosted.org/packages/30/aa/a2f84e93554a578463e2edaaf2300faa61c8701f0898725842c704ba5444/yarl-1.18.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:913829534200eb0f789d45349e55203a091f45c37a2674678744ae52fae23efa", size = 94144 },
    { url = "https://files.pythonhosted.org/packages/c6/fc/d68d8f83714b221a85ce7866832cba36d7c04a68fa6a960b908c2c84f325/yarl-1.18.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:ef9f7768395923c3039055c14334ba4d926f3baf7b776c923c93d80195624782", size = 91974 },
    { url = "https://files.pythonhosted.org/packages/56/4e/d2563d8323a7e9a414b5b25341b3942af5902a2263d36d20fb17c40411e2/yarl-1.18.3-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:88a19f62ff30117e706ebc9090b8ecc79aeb77d0b1f5ec10d2d27a12bc9f66d0", size = 333587 },
    { url = "https://files.pythonhosted.org/packages/25/c9/cfec0bc0cac8d054be223e9f2c7909d3e8442a856af9dbce7e3442a8ec8d/yarl-1.18.3-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e17c9361d46a4d5addf777c6dd5eab0715a7684c2f11b88c67ac37edfba6c482", size = 344386 },
    { url = "https://files.pythonhosted.org/packages/ab/5d/4c532190113b25f1364d25f4c319322e86232d69175b91f27e3ebc2caf9a/yarl-1.18.3-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1a74a13a4c857a84a845505fd2d68e54826a2cd01935a96efb1e9d86c728e186", size = 345421 },
    { url = "https://files.pythonhosted.org/packages/23/d1/6cdd1632da013aa6ba18cee4d750d953104a5e7aac44e249d9410a972bf5/yarl-1.18.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:41f7ce59d6ee7741af71d82020346af364949314ed3d87553763a2df1829cc58", size = 339384 },
    { url = "https://files.pythonhosted.org/packages/9a/c4/6b3c39bec352e441bd30f432cda6ba51681ab19bb8abe023f0d19777aad1/yarl-1.18.3-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f52a265001d830bc425f82ca9eabda94a64a4d753b07d623a9f2863fde532b53", size = 326689 },
    { url = "https://files.pythonhosted.org/packages/23/30/07fb088f2eefdc0aa4fc1af4e3ca4eb1a3aadd1ce7d866d74c0f124e6a85/yarl-1.18.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:82123d0c954dc58db301f5021a01854a85bf1f3bb7d12ae0c01afc414a882ca2", size = 345453 },
    { url = "https://files.pythonhosted.org/packages/63/09/d54befb48f9cd8eec43797f624ec37783a0266855f4930a91e3d5c7717f8/yarl-1.18.3-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:2ec9bbba33b2d00999af4631a3397d1fd78290c48e2a3e52d8dd72db3a067ac8", size = 341872 },
    { url = "https://files.pythonhosted.org/packages/91/26/fd0ef9bf29dd906a84b59f0cd1281e65b0c3e08c6aa94b57f7d11f593518/yarl-1.18.3-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:fbd6748e8ab9b41171bb95c6142faf068f5ef1511935a0aa07025438dd9a9bc1", size = 347497 },
    { url = "https://files.pythonhosted.org/packages/d9/b5/14ac7a256d0511b2ac168d50d4b7d744aea1c1aa20c79f620d1059aab8b2/yarl-1.18.3-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:877d209b6aebeb5b16c42cbb377f5f94d9e556626b1bfff66d7b0d115be88d0a", size = 359981 },
    { url = "https://files.pythonhosted.org/packages/ca/b3/d493221ad5cbd18bc07e642894030437e405e1413c4236dd5db6e46bcec9/yarl-1.18.3-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:b464c4ab4bfcb41e3bfd3f1c26600d038376c2de3297760dfe064d2cb7ea8e10", size = 366229 },
    { url = "https://files.pythonhosted.org/packages/04/56/6a3e2a5d9152c56c346df9b8fb8edd2c8888b1e03f96324d457e5cf06d34/yarl-1.18.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8d39d351e7faf01483cc7ff7c0213c412e38e5a340238826be7e0e4da450fdc8", size = 360383 },
    { url = "https://files.pythonhosted.org/packages/fd/b7/4b3c7c7913a278d445cc6284e59b2e62fa25e72758f888b7a7a39eb8423f/yarl-1.18.3-cp313-cp313-win32.whl", hash = "sha256:61ee62ead9b68b9123ec24bc866cbef297dd266175d53296e2db5e7f797f902d", size = 310152 },
    { url = "https://files.pythonhosted.org/packages/f5/d5/688db678e987c3e0fb17867970700b92603cadf36c56e5fb08f23e822a0c/yarl-1.18.3-cp313-cp313-win_amd64.whl", hash = "sha256:578e281c393af575879990861823ef19d66e2b1d0098414855dd367e234f5b3c", size = 315723 },
    { url = "https://files.pythonhosted.org/packages/f5/4b/a06e0ec3d155924f77835ed2d167ebd3b211a7b0853da1cf8d8414d784ef/yarl-1.18.3-py3-none-any.whl", hash = "sha256:b57f4f58099328dfb26c6a771d09fb20dbbae81d20cfb66141251ea063bd101b", size = 45109 },
]
```

### docs/notes.md

````markdown
# Project Dependencies Documentation

This document provides a detailed overview of all dependencies used in the Ollama Structured Outputs project, explaining their purpose and role in both the JavaScript and Python implementations.

## JavaScript Dependencies

### Core Dependencies JavaScript

- **ollama** (^0.5.11)
  - Client library for interacting with Ollama, an open-source local LLM server
  - Ollama allows running large language models locally with a simple API
  - Provides efficient inference and model management capabilities
  - Used in this project to make requests to locally running LLM instances

### Type Safety & Validation

- **zod** (^3.23.8)
  - Runtime type validation library
  - Used for ensuring type safety in the JavaScript implementation
  - Provides schema validation for structured data outputs
  - Helps catch type-related errors at runtime

- **zod-to-json-schema** (^3.23.5)
  - Converts Zod schemas to JSON Schema format
  - Enables interoperability between Zod's type system and JSON Schema
  - Useful for documentation and API validation

### Development Environment

- **Node.js** (20.18.1)
  - Managed via Volta for consistent versioning
  - Project uses ES Modules (type: "module" in package.json)

## Python Dependencies

### Core Dependencies Python

- **ollama** (>=0.4.3)
  - Python client library for Ollama LLM server
  - Enables Python applications to interact with locally running language models
  - Provides async/await support for stream handling
  - Used in the basic Python implementation for LLM inference

### AI/LLM Integration

- **instructor** (>=1.7.0)
  - Provides OpenAI-compatible interface
  - Built-in Pydantic integration for type validation
  - Used in the instructor-based implementation
  - Helps structure and validate LLM outputs

### Additional Dependencies (from README)

These dependencies are mentioned in the README but not explicitly listed in pyproject.toml:

- **pydantic** (2.10.3)
  - Data validation using Python type annotations
  - Used for type validation and data modeling
  - Core dependency for the instructor implementation

- **openai** (1.57.0)
  - Required by instructor for OpenAI-compatible interfaces
  - Provides base functionality that instructor builds upon

- **requests**
  - Used in the direct API implementation
  - Handles HTTP requests to the Ollama API
  - Provides comprehensive error handling capabilities

### Python Environment

- Requires Python >=3.12
- Uses UV package manager for dependency management
- Dependencies are locked via uv.lock for reproducible builds

## Implementation-Specific Usage

The project provides multiple implementations, each using different combinations of these dependencies:

1. **JavaScript Implementation** (`ollama_only.js`)
   - Uses ollama for local LLM inference
   - Leverages zod for type safety
   - Uses zod-to-json-schema for schema validation

2. **Python Implementations**:
   - **Ollama Package** (`ollama_only.py`): Uses ollama package with async support
   - **Instructor** (`instructor_ollama.py`): Uses instructor with Pydantic integration
   - **Direct API** (`ollama_json.py`): Uses requests for raw HTTP calls

Each implementation demonstrates different approaches to achieving structured outputs from Ollama, with varying levels of type safety and validation.
````

### docs/structured-json-outputs.md

````markdown
# Structured JSON outputs

Ollama now supports structured outputs making it possible to constrain a model’s output to a specific format defined by a JSON schema. The Ollama Python and JavaScript libraries have been updated to support structured outputs.

[[toc]]

Use cases for structured outputs include:

* Parsing data from documents
* Extracting data from images
* Structuring all language model responses
* More reliability and consistency than JSON mode

## Get started

Download the latest version of [Ollama](https://ollama.com/download)

Upgrade to the latest version of the Ollama Python or JavaScript library:

Python

```bash
pip install -U ollama
```

JavaScript

```bash
npm i ollama
```

To pass structured outputs to the model, the `format` parameter can be used in the cURL request or the `format` parameter in the Python or JavaScript libraries.

### cURL

```shell
curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "llama3.1",
  "messages": [{"role": "user", "content": "Tell me about Canada."}],
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "capital": {
        "type": "string"
      },
      "languages": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "name",
      "capital",
      "languages"
    ]
  }
}'
```

> Output

The response is returned in the format defined by the JSON schema in the request.

```json
{
  "capital": "Ottawa",
  "languages": [
    "English",
    "French"
  ],
  "name": "Canada"
}
```

### Python

Using the [Ollama Python library](https://github.com/ollama/ollama-python), pass in the schema as a JSON object to the `format` parameter as either `dict` or use Pydantic (recommended) to serialize the schema using `model_json_schema()`.

```py
from ollama import chat
from pydantic import BaseModel

class Country(BaseModel):
  name: str
  capital: str
  languages: list[str]

response = chat(
  messages=[
    {
      'role': 'user',
      'content': 'Tell me about Canada.',
    }
  ],
  model='llama3.1',
  format=Country.model_json_schema(),
)

country = Country.model_validate_json(response.message.content)
print(country)
```

> Output

```py
name='Canada' capital='Ottawa' languages=['English', 'French']
```

### JavaScript

Using the [Ollama JavaScript library](https://github.com/ollama/ollama-js), pass in the schema as a JSON object to the `format` parameter as either `object` or use Zod (recommended) to serialize the schema using `zodToJsonSchema()`.

```js
import ollama from 'ollama';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const Country = z.object({
    name: z.string(),
    capital: z.string(),
    languages: z.array(z.string()),
});

const response = await ollama.chat({
    model: 'llama3.1',
    messages: [{ role: 'user', content: 'Tell me about Canada.' }],
    format: zodToJsonSchema(Country),
});

const country = Country.parse(JSON.parse(response.message.content));
console.log(country);
```

> Output

```js
{
  name: "Canada",
  capital: "Ottawa",
  languages: [ "English", "French" ],
}
```

## Examples

### Data extraction

To extract structured data from text, define a schema to represent information. The model then extracts the information and returns the data in the defined schema as JSON:

```py
from ollama import chat
from pydantic import BaseModel

class Pet(BaseModel):
  name: str
  animal: str
  age: int
  color: str | None
  favorite_toy: str | None

class PetList(BaseModel):
  pets: list[Pet]

response = chat(
  messages=[
    {
      'role': 'user',
      'content': '''
        I have two pets.
        A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
        I also have a 2 year old black cat named Loki who loves tennis balls.
      ''',
    }
  ],
  model='llama3.1',
  format=PetList.model_json_schema(),
)

pets = PetList.model_validate_json(response.message.content)
print(pets)

```

> Example output

```py
pets=[
  Pet(name='Luna', animal='cat', age=5, color='grey', favorite_toy='yarn'),
  Pet(name='Loki', animal='cat', age=2, color='black', favorite_toy='tennis balls')
]
```

### Image description

Structured outputs can also be used with vision models. For example, the following code uses `llama3.2-vision` to describe the following image and returns a structured output:

![image](/public/blog/beach.jpg)

```py
from ollama import chat
from pydantic import BaseModel

class Object(BaseModel):
  name: str
  confidence: float
  attributes: str

class ImageDescription(BaseModel):
  summary: str
  objects: List[Object]
  scene: str
  colors: List[str]
  time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
  setting: Literal['Indoor', 'Outdoor', 'Unknown']
  text_content: Optional[str] = None

path = 'path/to/image.jpg'

response = chat(
  model='llama3.2-vision',
  format=ImageDescription.model_json_schema(),  # Pass in the schema for the response
  messages=[
    {
      'role': 'user',
      'content': 'Analyze this image and describe what you see, including any objects, the scene, colors and any text you can detect.',
      'images': [path],
    },
  ],
  options={'temperature': 0},  # Set temperature to 0 for more deterministic output
)

image_description = ImageDescription.model_validate_json(response.message.content)
print(image_description)
```

> Example output

```py
summary='A palm tree on a sandy beach with blue water and sky.'
objects=[
  Object(name='tree', confidence=0.9, attributes='palm tree'),
  Object(name='beach', confidence=1.0, attributes='sand')
],
scene='beach',
colors=['blue', 'green', 'white'],
time_of_day='Afternoon'
setting='Outdoor'
text_content=None
```

#### OpenAI compatibility

```py
from openai import OpenAI
import openai
from pydantic import BaseModel

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

class Pet(BaseModel):
    name: str
    animal: str
    age: int
    color: str | None
    favorite_toy: str | None

class PetList(BaseModel):
    pets: list[Pet]

try:
    completion = client.beta.chat.completions.parse(
        temperature=0,
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": '''
                I have two pets.
                A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                I also have a 2 year old black cat named Loki who loves tennis balls.
            '''}
        ],
        response_format=PetList,
    )

    pet_response = completion.choices[0].message
    if pet_response.parsed:
        print(pet_response.parsed)
    elif pet_response.refusal:
        print(pet_response.refusal)
except Exception as e:
    if type(e) == openai.LengthFinishReasonError:
        print("Too many tokens: ", e)
        pass
    else:
        print(e)
        pass
```

## Tips

For reliable use of structured outputs, consider to:

* Use Pydantic (Python) or Zod (JavaScript) to define the schema for the response
* Add “return as JSON” to the prompt to help the model understand the request
* Set the temperature to 0 for more deterministic output

## What’s next?

* Exposing logits for controlled generation
* Performance and accuracy improvements for structured outputs
* GPU acceleration for sampling
* Additional format support beyond JSON schema
````

> This concludes the repository's file contents. Please review thoroughly for a comprehensive understanding of the codebase.
