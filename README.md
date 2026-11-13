# AI Chatbot & LLM Tooling Suite

A lightweight, practical Python toolkit showcasing core modern LLM application patterns:
1. **Streaming Terminal Chatbot:** Multi-turn conversational interface with streaming token output and conversation memory using OpenRouter / OpenAI API.
2. **Structured Information Extractor:** Strict Pydantic schema parsing from unstructured natural language inputs.
3. **Local Semantic Search:** Embedded vector search with ChromaDB for text similarity retrieval.

---

## Features

- **Real-Time Streaming:** Streams response deltas to the console without buffering.
- **Context Retention:** Maintains ongoing chat history in a structured message list.
- **Type-Safe Structured Output:** Uses OpenAI's `.beta.chat.completions.parse` with Pydantic models for reliable schema extraction.
- **Embedded Vector Search:** ChromaDB in-memory client for fast cosine-similarity search over documents.

---

## Installation & Setup

### 1. Clone & Install Dependencies
Using `uv` (recommended) or `pip`:

```bash
git clone https://github.com/eyyub679/ai_chatbot.git
cd ai_chatbot
uv sync
```

Or with `pip`:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Add your OpenRouter or OpenAI API key:
```ini
API_KEY="your-api-key-here"
```

---

## Usage

### 1. Interactive Streaming Chatbot
```bash
python chatbot.py
```
Type your message and receive live streaming answers. Type `q` to exit.

### 2. Structured Data Extraction
```bash
python extractor.py
```
Extracts typed Pydantic entities (e.g., player profile: name, position, foot, nationality, club history) from unstructured text.

### 3. Semantic Vector Search
```bash
python semantic_search.py
```
Indexes sample passages into a local ChromaDB collection and queries them using semantic similarity.
