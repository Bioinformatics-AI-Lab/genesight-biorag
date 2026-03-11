# GeneSight + BioRAG

**A bioinformatics toolkit combining ML-based variant pathogenicity prediction with literature-grounded AI Q&A.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/genesight-biorag/blob/main/notebooks/01_GeneSight_Data_Pipeline.ipynb)

---

## 🔬 Projects

### GeneSight — Variant Pathogenicity Predictor
Predicts whether a genomic variant is pathogenic or benign by combining:
- **ClinVar** labeled variant annotations (ground truth)
- **gnomAD** population allele frequencies + gene-level constraint scores (pLI, LOEUF)
- **XGBoost** classifier with **SHAP** explainability

### BioRAG — Biomedical Literature Q&A
Upload your own research PDFs and ask natural language questions. Answers are grounded in your paper library with exact passage citations — powered by a BioBERT embedding model and Claude.

### Integration
When GeneSight returns a prediction, "Explain this variant" queries BioRAG against your literature library — connecting ML output to primary sources.

---

## 📓 Notebooks

| Notebook | Description | Open |
|---|---|---|
| `01_GeneSight_Data_Pipeline.ipynb` | ClinVar + gnomAD download & feature engineering | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/genesight-biorag/blob/main/notebooks/01_GeneSight_Data_Pipeline.ipynb) |
| `02_GeneSight_Model_SHAP.ipynb` | XGBoost training, evaluation, SHAP plots | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/genesight-biorag/blob/main/notebooks/02_GeneSight_Model_SHAP.ipynb) |
| `03_BioRAG_Ingestion.ipynb` | PDF ingestion, chunking & embeddings | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/genesight-biorag/blob/main/notebooks/03_BioRAG_Ingestion.ipynb) |
| `04_BioRAG_QA_Demo.ipynb` | Conversational Q&A with citation | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/genesight-biorag/blob/main/notebooks/04_BioRAG_QA_Demo.ipynb) |

---

## 🚀 Quickstart

All notebooks run in **Google Colab** — no local installation required. Click any badge above.

For local development:

```bash
git clone https://github.com/Bioinformatics-AI-Lab/genesight-biorag.git
cd genesight-biorag
pip install -r requirements.txt
jupyter notebook notebooks/
```

---

## 🏗️ Architecture

```
Input: VCF / gene list          Input: Research PDFs
        ↓                               ↓
  ClinVar + gnomAD              PDF text extraction
  feature engineering           BioBERT embeddings
        ↓                               ↓
  XGBoost classifier           ChromaDB vector store
        ↓                               ↓
  Pathogenicity score    →  "Explain this" → RAG Q&A
        ↓                               ↓
   SHAP waterfall            Cited passage retrieval
   explanation               + Claude synthesis
```

---

## 📦 Tech Stack

| Component | Technology |
|---|---|
| Data | ClinVar FTP, gnomAD GraphQL API |
| ML | XGBoost, scikit-learn, SHAP |
| Embeddings | BioBERT (sentence-transformers) |
| Vector DB | ChromaDB |
| LLM | Anthropic Claude API |
| Notebooks | Jupyter / Google Colab |

---

## ⚠️ Disclaimer

GeneSight predictions are for **research purposes only** and should not be used for clinical decision-making. BioRAG Q&A should always be verified against the original source documents.

---

## 📄 License

MIT License — see [LICENSE](LICENSE)
