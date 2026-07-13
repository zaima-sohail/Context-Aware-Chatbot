# Context-Aware Chatbot Using Retrieval-Augmented Generation (RAG) with Gemini API

## Project Overview

This project implements a **Context-Aware Chatbot** using **Retrieval-Augmented Generation (RAG)**. The chatbot retrieves relevant information from a custom knowledge base using **FAISS Vector Search** and generates intelligent responses using the **Google Gemini API**.

Unlike traditional chatbots, this system can answer questions based on external documents while maintaining conversation history for context-aware interactions.

---<img width="1899" height="998" alt="Screenshot 2026-07-13 210425" src="https://github.com/user-attachments/assets/9b8bc9f3-8e15-416f-ae8a-4c5ddcbf4617" />


## Objectives

- Build a conversational AI chatbot.
- Implement Retrieval-Augmented Generation (RAG).
- Store document embeddings in a FAISS vector database.
- Retrieve relevant documents using semantic similarity.
- Generate responses using Google's Gemini LLM.
- Maintain conversational context.
- Deploy the chatbot using Streamlit.

---

## Technologies Used

- Python
- Google Gemini API
- FAISS
- Sentence Transformers
- Streamlit
- NumPy

---

## Project Structure

```
RAG_Chatbot/
│
├── data/
│   └── documents.txt
│
├── vector_db/
│
├── chatbot.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install google-generativeai
pip install sentence-transformers
pip install faiss-cpu
pip install streamlit
pip install pypdf
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Replace the API key in the notebook or application:

```python
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
```

---

## Dataset

The chatbot uses a custom text document located in:

```
data/documents.txt
```

You can replace this file with:

- Company documents
- Research papers
- Notes
- Wikipedia content
- PDF text
- Knowledge base

---

## How It Works

1. Load documents.
2. Split the document into smaller chunks.
3. Generate embeddings using Sentence Transformers.
4. Store embeddings in a FAISS vector database.
5. Convert the user query into an embedding.
6. Retrieve the most relevant document chunks.
7. Send the retrieved context and conversation history to Gemini.
8. Generate a context-aware response.

---

## Running the Notebook

Open:

```
chatbot.ipynb
```

Run all cells sequentially.

---

## Running the Streamlit App

Execute:

```bash
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

## Example Conversation

**User**

```
What is Artificial Intelligence?
```

**Bot**

```
Artificial Intelligence is the simulation of human intelligence by machines.
```

**User**

```
What is Machine Learning?
```

**Bot**

```
Machine Learning is a subset of Artificial Intelligence.
```

**User**

```
Is it part of AI?
```

**Bot**

```
Yes. Machine Learning is a subset of Artificial Intelligence.
```

---

## Features

- Context-aware conversation
- Retrieval-Augmented Generation (RAG)
- Semantic document search
- FAISS vector database
- Gemini-powered response generation
- Easy integration with custom datasets
- Interactive Streamlit interface

---

## Future Enhancements

- Support PDF documents
- Multiple document formats
- Chat history stored in a database
- Voice-based interaction
- Multi-user support
- Advanced retrieval and ranking

---

## Skills Gained

- Conversational AI Development
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Document Embeddings
- Semantic Search
- Google Gemini API Integration
- Streamlit Deployment

graphical interface
<img width="1850" height="1042" alt="Screenshot 2026-07-13 192535" src="https://github.com/user-attachments/assets/ce25fc0a-9402-411a-92b7-60bd746d4b6d" />


## Author

**Name:** zaima Sohail

**internship :** Artificial Intelligence / Machine Learning

**Project:** Context-Aware Chatbot Using Retrieval-Augmented Generation (RAG)
