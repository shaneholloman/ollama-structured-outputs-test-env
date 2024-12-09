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
