import streamlit as st
import duckdb
import os

st.title("🚀 Marketing Performance & Velocity Dashboard")
st.markdown("An end-to-end analytics engineering pipeline built with Python, dbt, and DuckDB.")

# Corrected path including my_marketing_pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, 'marketing_dbt', 'dev.duckdb'))

@st.cache_data
def load_data_from_duckdb():
    conn = duckdb.connect(DB_PATH, read_only=True)
    df = conn.execute("SELECT * FROM fct_marketing_performance").fetchdf()
    conn.close()
    return df

df = load_data_from_duckdb()

# Show key metrics at the top
total_spend = df['spend'].sum()
total_revenue = df['revenue'].sum()
avg_roas = df['roas'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Spend", f"${total_spend:,.2f}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Average ROAS", f"{avg_roas:.2f}x")

st.divider()

# Display the Clean Mart Data Table
st.subheader("📊 Final Mart Data Preview")
st.dataframe(df, use_container_width=True)

# Add a simple chart
st.subheader("⚡ Spend by Channel")
st.bar_chart(df, x="utm_source", y="spend")