# Adaptive RAG
Adaptive RAG is an advanced strategy for RAG that intelligently combines (1) dynamic query analysis with (2) active/self-corrective mechanisms.

Adaptive RAG represents the most sophisticated evolution, addressing a fundamental insight: not all queries are created equal. The research reveals that real-world queries exhibit vastly different complexity levels:



## Project Structure

```
building-adaptive-rag/
├── graph/
│   ├── chains/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_chains.py
│   │   ├── __init__.py
│   │   ├── answer_grader.py
│   │   ├── generation.py
│   │   ├── hallucination_grader.py
│   │   ├── retrieval_grader.py
│   │   └── router.py
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── generate.py
│   │   ├── grade_documents.py
│   │   ├── retrieve.py
│   │   └── web_search.py
│   ├── __init__.py
│   ├── consts.py
│   ├── graph.py
│   └── state.py
├── static/
│   ├── LangChain-logo.png
│   ├── Langgraph Adaptive Rag.png
│   └── graph.png
├── .env
├── .gitignore
├── ingestion.py
├── main.py
├── model.py
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

Install uv (if not already installed):

```PS
powershell -ExecutionPolicy Bypass -c "irm https://github.com/astral-sh/uv/releases/download/0.8.4/uv-installer.ps1 | iex"
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/debjeetism/adaptive-rag-cli
```

2. **Navigate to the project directory**

```bash
cd agentic-rag/agentic-rag-systems/building-adaptive-rag/
```

3. **Create and activate virtual environment**

```bash
uv venv --python 3.10
source .venv/bin/activate
```

4. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```env
GOOGLE_API_KEY=your_tavily_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # For web search capabilities
LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional, for tracing
LANGCHAIN_TRACING_V2=true                      # Optional
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com # Optional
LANGCHAIN_PROJECT=agentic-rag                  # Optional
```

**Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error.

## Usage

### Start the Agentic RAG flow

```bash
uv run main.py
```

### Running Tests

To run tests, execute the following command:

```bash
uv run pytest . -s -v
```

## Features

- **Adaptive RAG**: Dynamically routes queries to the most appropriate processing method
- **Self-RAG**: Implements self-reflection mechanisms for improved answer quality
- **Reflective RAG**: Incorporates reflection and grading for enhanced retrieval
- **Web Search Integration**: Fallback to web search when local knowledge is insufficient
- **LLM Fallback**: Fallback to direct LLM response, for general queries, greetings, etc.
- **Document Grading**: Evaluates relevance of retrieved documents
- **Hallucination Detection**: Identifies and handles potential hallucinations in generated responses

## Architecture

The system implements a sophisticated RAG pipeline with the following components:

- **Router**: Intelligently routes queries between vectorstore retrieval and web search
- **Retrieval Grader**: Evaluates the relevance of retrieved documents
- **Generation Chain**: Produces answers based on retrieved context
- **Hallucination Grader**: Detects potential hallucinations in generated responses
- **Answer Grader**: Evaluates the quality and relevance of final answers
