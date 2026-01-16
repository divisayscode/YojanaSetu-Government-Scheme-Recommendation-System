# YojanaSetu: Semantic Search and RAG-based Assistant for Government Schemes

## Overview
YojanaSetu is an end-to-end **Conversational AI system** designed to help users discover relevant **Government of India welfare schemes** based on their needs.  
The project evolves from a **semantic search–based retrieval system** to a **Retrieval-Augmented Generation (RAG)** pipeline that combines deep learning with large language model reasoning.

The system addresses limitations of traditional keyword search by understanding **user intent, eligibility context, and scheme benefits**.

---

## Problem Statement
India has hundreds of government welfare schemes, but citizens often struggle to find schemes they are eligible for due to:
- Complex bureaucratic language
- Fragmented information sources
- Poor performance of keyword-based search systems

The goal of this project is to build an intelligent assistant that can **retrieve, reason, and respond** accurately to user queries about government schemes.

---

## Dataset Collection (Web Scraping)
A **custom dataset** was created specifically for this project.

- Scheme data was scraped using `requests` and `BeautifulSoup`
- Information was extracted from unordered lists and structured tables
- Irrelevant and duplicate entries were removed
- A fallback mechanism was implemented to ensure robustness in case scraping fails

The final dataset was saved as a structured CSV file containing:
- Scheme ID  
- Scheme Name  
- Scheme Description  

This scraping pipeline forms the foundation of the system.

---

## Data Preprocessing
The collected textual data was cleaned and standardized before modeling:
- Removal of noise and irrelevant characters
- Lowercasing and whitespace normalization
- Deduplication of scheme descriptions
- Formatting for embedding-based retrieval

---

## Phase 1: Semantic Search using Deep Learning
The initial version of the system relied purely on **semantic similarity**.

### Model
- **Sentence-BERT (SBERT)** was used to convert scheme descriptions into dense vector embeddings
- **Cosine similarity** was used to retrieve the most relevant schemes for a given query

### Limitation
While semantic search outperformed keyword-based methods, it failed in cases requiring **reasoning**.
For example, queries related to business loans sometimes retrieved student loan schemes due to lexical similarity.

---

## Phase 2: Retrieval-Augmented Generation (RAG)
To overcome the limitations of semantic search, the system was extended to a **RAG architecture**.

### Retriever
- SBERT retrieves the **top-k most relevant schemes**
- Retrieved scheme descriptions are combined into a context block

### Generator (Reasoning Engine)
- **Google Gemini API** is used as the large language model
- The LLM analyzes retrieved context and generates:
  - Clear explanations
  - Exact monetary benefits
  - Eligibility-based recommendations

### Safety and Robustness
- API rate-limit handling using retry logic
- Graceful fallback mechanisms to prevent system failure

---

## Evaluation and Results
The system was evaluated in two stages:

### Semantic Search Only
- Accuracy: ~48%
- Retrieval based purely on embedding similarity

### RAG-based System
- Introduced reasoning over retrieved content
- Evaluated using an **LLM-as-a-Judge** framework
- Test cases spanned multiple domains (Housing, Education, Health, Business, Pension)
- Final average evaluation score: **4.6 / 5**

This demonstrated a significant improvement in correctness and response quality.

---

## Key Features
- Automated dataset creation via web scraping
- Semantic search using transformer-based embeddings
- RAG pipeline combining retrieval and reasoning
- Conversational responses instead of raw search results
- Robust error handling and evaluation framework

---

## Technologies Used
- Python
- Requests, BeautifulSoup
- Pandas, NumPy
- Sentence-BERT (SBERT)
- Cosine Similarity
- Google Gemini API
- Retrieval-Augmented Generation (RAG)

---

## Conclusion
This project demonstrates how combining **semantic search with generative reasoning** significantly improves accuracy and usability for real-world information retrieval tasks.  
YojanaSetu highlights the importance of **context-aware AI systems** for public-facing applications.


