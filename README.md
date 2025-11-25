# Retail Data Engineering Platform (Supermarket Sales Dataset)

## 🚀 Project Overview
This project implements an end-to-end **Data Engineering Pipeline** using:

- **PySpark** for ETL  
- **Databricks Lakehouse** (Bronze → Silver → Gold)  
- **Delta Lake** for storage  
- **GenAI SQL Query Engine** for natural language analytics  

Users can ask questions like:

> "Top 3 product lines by revenue in March?"

The GenAI module converts the question → SQL → executes → generates insights.

---

## 📂 Project Architecture
RAW (Bronze) → Cleaned (Silver) → Star Schema (Gold)
↓
GenAI SQL Query Engine


---

## 🏗 Tech Stack
- PySpark  
- Delta Lake  
- Databricks  
- Azure Fabric (optional)  
- LangChain + SQLDatabaseChain  
- SQLite / Delta Tables  

---

## 📊 Features
✔ Automated ingestion  
✔ Cleaning + transformation  
✔ Star schema (FactSales + DimProduct)  
✔ Delta Lake storage  
✔ Natural language to SQL  
✔ Insight generation  

---

## 📁 Folder Structure
(As shown above)

---

## ▶️ How to Run


pip install -r requirements.txt
python 1_ingestion/ingest_raw.py
python 2_transformation/clean_transform.py
python 2_transformation/create_gold_tables.py
python 3_genai_query/genai_sql_query.py

