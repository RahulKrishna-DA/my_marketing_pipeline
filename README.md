# Analytics Engineering Transformation & Streamlit App

A robust end-to-end data pipeline project demonstrating modern analytics engineering practices using **dbt**, **GitHub Actions**, and **Streamlit**.

---

## 🚀 Project Overview

This project simulates a complete data stack:
* **Data Generation:** Built with Python and `Faker` to generate synthetic, complex business datasets.
* **Transformation Pipeline:** A 3-layer modular dbt (data build tool) architecture that cleans, models, and transforms raw data into analytics-ready data marts.
* **CI/CD Automation:** Automated execution of the dbt pipeline using **GitHub Actions**.
* **Interactive Dashboard:** A deployed **Streamlit** application connected directly to the output data marts to deliver real-time business insights and automated reporting.

---

## 🛠️ Tech Stack

* **Transformation:** dbt Core
* **CI/CD & Automation:** GitHub Actions
* **Data Modeling & Scripting:** Python, Faker
* **Visualization:** Streamlit
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
├── .github/workflows/    # CI/CD pipelines (GitHub Actions)
├── models/               # dbt models (Staging, Intermediate, Marts)
├── data_generation/      # Python scripts utilizing Faker for synthetic data
├── app.py                # Streamlit application for dashboards
├── dbt_project.yml       # dbt configuration
└── README.md             # Project documentation