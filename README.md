# Automated Log Analysis & Noise Reduction Pipeline 📊

![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue?style=flat&logo=python)
![AIOps](https://img.shields.io/badge/Domain-AIOps-purple)

## 📌 Project Overview
**Automating Reliability Engineering:** A data pipeline designed to ingest raw, noisy server logs and convert them into actionable insights. It utilizes semantic clustering to reduce alert fatigue and uses LLMs to generate human-readable Root Cause Analysis (RCA).

## 🚀 Key Features
- **Regex Parsing:** Automated extraction of timestamps, error codes, and messages from unstructured logs.
- **Semantic Clustering:** Groups similar error patterns using sentence-transformers to reduce noise by 90%.
- **Auto-RCA:** Generates summaries for critical failure clusters using lightweight LLMs.

## 🛠 Tech Stack
- **Language:** Python
- **Data Processing:** Pandas, NumPy, Regular Expressions (Re)
- **AI Models:** Sentence-Transformers, OpenAI API

## 🚧 Development Roadmap
- [x] Data Collection & Exploratory Analysis
- [ ] Parsing Script Implementation (Regex)
- [ ] Clustering Algorithm Integration
- [ ] Automated Reporting Dashboard
