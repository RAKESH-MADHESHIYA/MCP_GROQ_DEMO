# MCP Multi-Server Agent with Groq

## Overview

This project demonstrates how to build an AI Agent using:

* LangChain
* Groq LLM (Llama 3.3 70B)
* Model Context Protocol (MCP)
* Multiple MCP Servers
* LangChain MCP Adapters

The agent connects to multiple MCP servers and dynamically discovers tools that can be invoked by the LLM.

Current MCP Servers:

1. Math Server (STDIO Transport)
2. Weather Server (Streamable HTTP Transport)

---

## Architecture

```text
+-------------------+
|   User Query      |
+---------+---------+
          |
          v
+-------------------+
| LangChain Agent   |
| (Groq LLM)        |
+---------+---------+
          |
          v
+-------------------+
| MCP Client        |
+---------+---------+
          |
  -------------------
  |                 |
  v                 v
Math MCP       Weather MCP
(STDIO)        (HTTP)
```

---

## Prerequisites

* Python 3.10+
* Groq API Key

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Project Structure

```text
.
├── client.py
├── mathserver.py
├── weather.py
├── .env
├── requirements.txt
└── README.md
```

---

## MCP Configuration

### Math Server

Uses STDIO transport.

```python
"math": {
    "command": "python",
    "args": ["mathserver.py"],
    "transport": "stdio"
}
```

### Weather Server

Uses Streamable HTTP transport.

```python
"weather": {
    "url": "http://localhost:8000/mcp",
    "transport": "streamable_http"
}
```

---

## Running the Application

Start the Weather MCP server:

```bash
python weather.py
```

Run the client:

```bash
python client.py
```

---

## Example Queries

### Math Tool

```text
Use available tools to calculate 18 multiplied by 12
```

Example Response:

```text
216
```

### Weather Tool

```text
What is the weather in California?
```

Example Response:

```text
Current weather information for California...
```

---

## Key Features

* Multi-server MCP integration
* Automatic tool discovery
* Groq-powered reasoning
* STDIO transport support
* Streamable HTTP transport support
* LangChain agent orchestration

---

## Technologies Used

* Python
* LangChain
* MCP
* LangChain MCP Adapters
* Groq
* AsyncIO

---

## Future Enhancements

* Azure OpenAI integration
* Authentication and authorization
* Docker deployment
* FastAPI integration
* Additional MCP tools
* CI/CD using GitHub Actions
## CI/CD Workflow

This project uses GitHub Actions for Continuous Integration (CI) to automatically validate code quality on every push and pull request.

### Workflow Pipeline

```text
Push/Pull Request
       ↓
Checkout Code
       ↓
Setup Python
       ↓
Install Dependencies
       ↓
Syntax Validation
       ↓
Run Unit Tests
       ↓
Build Application
```

### GitHub Actions Workflow

The workflow performs the following tasks:

* Checks out the latest source code
* Sets up Python 3.12
* Installs project dependencies
* Validates Python syntax using `compileall`
* Runs automated tests using `pytest`
* Builds and validates the application

### Benefits

* Early detection of syntax errors
* Automated test execution
* Consistent build process
* Improved code quality
* Faster feedback for developers

### Workflow File Location

```text
.github/
└── workflows/
    └── ci.yml
```


---

## License

This project is for educational and demonstration purposes.
