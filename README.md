# 🚀 Automated Marketing Analytics & Customer Velocity ELT Pipeline

A robust, end-to-end data engineering pipeline that automates the ingestion, transformation, and deployment of e-commerce marketing performance data. This project demonstrates modern analytics engineering practices to replace manual, slow spreadsheet lookups (`VLOOKUP`) with an automated data stack.

🌐 **[Click Here to View the Live Dashboard](https://mymarketingpipeline-nxsgxlonsgru8c5krxrtjl.streamlit.app/)
---

## ⚡ Key Business Metrics Automated
Unlike generic data pipelines, this architecture specifically tracks and models commercial marketing health:
*   📈 **Return on Ad Spend (ROAS):** Evaluates exact channel efficiency by merging granular ad spend data against transactional conversion revenue.
*   📊 **Customer Purchase Velocity:** Tracks repeat-purchase intervals to monitor consumer lifecycle value and retention trends.
*   💰 **Revenue Distribution:** Aggregates operational and channel-specific performance to optimize future ad budget allocations.

---

## 🏗️ Project Components & Features

* **Data Generation:** Python scripts utilizing `Faker` to mock realistic, complex e-commerce transaction logs, customer profiles, and ad campaign spend data.
* **Storage Engine:** **DuckDB** utilized as an embedded, high-performance columnar storage layer.
* **Transformation Pipeline:** A 3-layer modular **dbt Core** architecture (Staging ➔ Intermediate ➔ Marts) handling data cleaning, schema enforcement, and dimensional data modeling (Star Schema).
* **CI/CD Automation:** Automated execution, testing, and production builds of the dbt pipeline using **GitHub Actions**.
* **Interactive Dashboard:** A public-facing **Streamlit** cloud application featuring dynamic sidebar filters and reactive metrics calculation for stakeholder decision-making.

---

## 🛠️ Tech Stack

* **Database Engine:** DuckDB
* **Transformation & Modeling:** dbt Core (Data Build Tool)
* **CI/CD & Automation:** GitHub Actions
* **Scripting & Data Generation:** Python, Faker
* **Visualization Engine:** Streamlit / Streamlit Cloud
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
├── .github/workflows/    # CI/CD pipelines (GitHub Actions automatic dbt runs)
├── marketing_dbt/        # dbt models (Staging, Intermediate, Marts)
├── scripts/              # Python scripts utilizing Faker for data generation
├── app.py                # Streamlit application with interactive filters
├── requirements.txt      # Project dependencies for Streamlit Cloud
├── dev.duckdb            # Local embedded database engine
├── dbt_project.yml       # dbt project configurations
└── README.md             # Project documentation
```
