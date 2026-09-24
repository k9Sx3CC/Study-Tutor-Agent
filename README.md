# Study-Tutor-Agent

# ✦ Study Tutor AI

A beginner-friendly AI Study Tutor built with Streamlit, CrewAI, and Groq.

The application helps students understand academic concepts through
step-by-step explanations, examples, study planning, and practice.

## Features

- AI study tutor
- Subject selection
- Learning-level selection
- Conversational interface
- Session-based conversation memory
- Calculator tool
- Study Planner tool
- CrewAI agent orchestration
- Groq GPT-OSS 120B
- Modern neon-blue AI interface
- Streamlit frontend

## Architecture

```text
Student
   |
   v
Streamlit UI
   |
   v
Study Tutor Agent
   |
   +------ Calculator Tool
   |
   +------ Study Planner Tool
   |
   v
Groq GPT-OSS 120B
   |
   v
Tutor Response
