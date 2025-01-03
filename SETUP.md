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
