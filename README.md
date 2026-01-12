# 📊 Automated Log Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat&logo=pandas)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

## 📌 Project Overview
**"Automating ETL for unstructured server logs."**

In data-intensive engineering environments, manually inspecting raw logs is inefficient. I developed this pipeline to demonstrate **automated data ingestion and parsing** using Python.

The goal was to build a robust script that converts unstructured text data into structured CSV reports, enabling statistical analysis of system health without manual intervention.

## 🚀 Key Features
- **🧹 Regex-Based Parsing:** Utilizes custom **Regular Expressions** to extract critical fields (`Timestamp`, `Error Level`, `Message`) from noisy raw text.
- **🚨 Statistical Pattern Detection:** Aggregates error occurrences to identify high-frequency failure patterns.
- **📈 Automated Visualization:** Generates error distribution charts using **Matplotlib** to visualize system trends.

## 🛠 Tech Stack
- **Language:** Python 3.11
- **Data Processing:** Pandas, NumPy
- **Core Logic:** Regular Expressions (Re)
- **Visualization:** Matplotlib

## 🚧 Roadmap
This project is currently in the **Prototype** phase.

- [x] **Phase 1:** Build Regex Parser & Statistical Analysis
- [ ] **Phase 2:** Integrate with **RAG Agent** for AI-based Root Cause Analysis
- [ ] **Phase 3:** Real-time Dashboard Implementation with Streamlit

## 📂 Project Structure
```bash
├── logs/                   # Raw server logs (Simulated unstructured data)
├── output/                 # Processed CSV reports & Visualization images
├── analysis.py             # Main ETL & Analysis script
└── log_generator.py        # Script to simulate high-volume log data