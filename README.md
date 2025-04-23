# 🩺 Inquirmed – GenAI Clinical Assistant (Prototype)

Inquirmed is an open-source GenAI-powered clinical assistant designed to help healthcare practitioners explore medical information, answer symptom-related questions, and generate structured patient documentation — **entirely offline** and using only **publicly available datasets and free tools**.

This prototype simulates key features seen in AI-first clinical tools like **TrovoHealth**, **Ambience Healthcare**, and **Corti**, while being modular, transparent, and safe for demonstration purposes.

---

## 🚀 Features

### 🔍 1. Search FDA and PubMed
- Perform vector-based search over 10,000+ OpenFDA drug event reports and PubMed abstracts
- Returns top-k results with semantic ranking using `all-MiniLM-L6-v2` embeddings
- Built with ChromaDB for fast, local retrieval

### 💬 2. Agentic Assistant with Memory
- Ask clinical queries like "Is metformin safe during pregnancy?"
- Supports multi-turn interactions with LangChain's `ConversationalRetrievalChain`
- LLM used: `flan-t5-base` (HuggingFace, local)
- Includes transparent source references for every response

### 📄 3. SOAP Note Summarization
- Paste raw clinical notes to generate structured **Subjective, Objective, Assessment, Plan** sections
- Powered by an LLM prompt or fallback rules-based logic for consistent output
- Optimized for fast documentation workflows

---

## 📊 System Architecture

```
User Interface (Streamlit)
  ├── Tab 1: Search (FDA / PubMed)
  ├── Tab 2: Agentic Assistant (with memory + source docs)
  └── Tab 3: SOAP Summarizer (structured output)

Application Logic
  ├── search_collection(query, source)
  ├── get_agent(collection="fda")
  └── summarize_soap(note_text)

Backend Components
  ├── ChromaDB (Vector Store)
  ├── SentenceTransformers (Embedding)
  ├── LangChain Retriever + Memory
  └── HuggingFace Pipeline (flan-t5-base)
```

---

## ⚙️ Tech Stack
- **Frontend:** Streamlit
- **LLMs:** HuggingFace `flan-t5-base`
- **Retrieval:** LangChain + ChromaDB
- **Embeddings:** `all-MiniLM-L6-v2`
- **Data Sources:** OpenFDA + PubMed (JSON samples)
- **Languages:** Python

---

## 📁 Folder Structure
```
Inquirmed/
├── app/                 # Streamlit UI, agent, summarizer modules
├── retriever/           # Search and embedding logic
├── data/                # Raw + cleaned JSON files
├── db/chroma/           # Persistent ChromaDB vector index
├── embeddings/          # Optional precomputed embeddings
├── scripts/             # Preprocessing scripts for FDA/PubMed
└── requirements.txt     # Dependencies
```

---

## 📌 Why Use Model Context Protocol (MCP)?
Model Context Protocol (MCP) ensures LLMs generate **structured, schema-compliant outputs** — minimizing hallucinations and making results suitable for EHR systems. MCP will be applied to:
- Enforce SOAP formatting
- Structure assistant answers with tags (summary, references)
- Format PubMed summaries or patient timelines as YAML/JSON

---

## 🛠 Roadmap to Production
To move from prototype to production:

### Architecture
- Replace Streamlit with Next.js + FastAPI
- Add Docker + secure user auth

### LLM & Retrieval
- Upgrade to `Mistral-7B` or `BioGPT`
- Add keyword + hybrid search
- Use MCP for structured, safe outputs

### Dataset Upgrade
- Replace PubMed/FDA with **MIMIC-III** or **MIMIC-IV** for real patient discharge notes, vitals, meds
- Simulate EHR workflows using de-identified clinical data

### TrovoHealth-Inspired Features
- Voice transcript summarization
- FHIR integration with EHR
- Medication conflict detection
- Patient timeline generation

---

## 🧪 Demo Scenarios

### 🔹 Drug Lookup
```
Query: What are the side effects of metformin?
→ Returns 5 FDA-recorded adverse events with sources
```

### 🔹 Agentic Q&A
```
Q: Is metformin safe during pregnancy?
A: Yes, with caution... [📚 View Sources]
```

### 🔹 SOAP Summary
```
Input:
The patient complains of chest pain radiating to the left arm...
→ Output:
Subjective:
Objective:
Assessment:
Plan:
```

---

## 📄 License
This project is for **research and demonstration purposes only**. No clinical decisions should be made using this assistant.

---

## 🙌 Author
**Amrut Kulkarn**  
Recent MS CS Graduate @ University at Buffalo  
**Project: Inquirmed** (April 2025)

---

