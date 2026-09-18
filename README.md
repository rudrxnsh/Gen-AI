# 🤖 GenAI Learning Journey

A collection of my hands-on experiments and projects while learning **Generative AI, LLMs, Agents, Tools, Memory, and RAG**.

The goal is to learn by building small, practical applications and documenting the journey.

---

## 🚀 Current Project — AI Chatbot

A simple AI chatbot built with **LangChain + LangGraph + Groq + Google Search + Streamlit**.

### Architecture

```text
User
 ↓
Streamlit UI
 ↓
AI Agent
 ├── LLM (Groq)
 ├── Google Search Tool
 └── Memory (LangGraph)
 ↓
Streaming Response
