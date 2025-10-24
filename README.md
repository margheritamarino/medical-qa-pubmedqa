# 🧠 NLP Project: Medical Question Answering with PubMedQA

**Politecnico di Milano – Group Project**

---

## 📘 Overview
This project focuses on developing a **Medical Question Answering (QA)** system using the **PubMedQA** dataset. The goal was to explore how Natural Language Processing (NLP) techniques and Large Language Models (LLMs) can be applied to understand and answer biomedical questions with high accuracy.

---

## 🧩 Project Structure
The project is organized across four main notebooks:

1. **`main_notebook.ipynb`** — Main pipeline and evaluation workflow.  
2. **`compute_embeddings.ipynb`** — Embedding computation (TF-IDF, Word2Vec, BioBERT).  
3. **`rag_dataset_preparation.ipynb`** — Data preprocessing, cleaning, and retrieval-augmented generation setup.  
4. **`llm_inference.ipynb`** — Inference and comparison of fine-tuned models.

---

## ⚙️ Methodology
### 1. Data Preprocessing
- Balanced the dataset and normalized text using **NLTK**.  
- Tokenized and cleaned input data for model training.  
- Prepared embeddings for downstream models.

### 2. Exploratory Analysis
- Applied **clustering** and **PCA** to analyze dataset structure and embedding spaces.  
- Investigated relationships between question categories and answer distributions.

### 3. Model Training
- Implemented and compared multiple **classical ML models**:
  - Logistic Regression (LR)  
  - Support Vector Classifier (SVC)  
  - Gaussian Naive Bayes  
  - Random Forest  
  - Gradient Boosting  

- Fine-tuned **BioBERT** for improved domain-specific performance.
- Evaluated **DRAGON**, a modern transformer architecture pre-trained jointly on text and knowledge graphs, achieving enhanced reasoning and biomedical understanding.

### 4. Evaluation
- Compared baseline models, fine-tuned BioBERT, and DRAGON-based approaches on PubMedQA metrics.  
- Assessed factual correctness, reasoning quality, and answer interpretability.


### 5. Chatbot Integration
- Developed a **voice-enabled chatbot** integrating:
  - **Text-to-Speech (TTS)** for audio output  
  - **Speech-to-Text (STT)** for voice input  
- Enabled interactive medical Q&A experience.

---

## 🧠 Technologies Used
- **Python**
- **NLTK**
- **scikit-learn**
- **Word2Vec / Gensim**
- **BioBERT**
- **Hugging Face Transformers**
- **Plotly / Matplotlib**
- **SpeechRecognition**, **pyttsx3** (for TTS/STT)

---



