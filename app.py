import streamlit as st
import duckdb
import os

st.title("🚀 Marketing Performance & Velocity Dashboard")
st.markdown("An end-to-end analytics engineering pipeline built with Python, dbt, and MotherDuck.")

# Safely check if the secret token exists
MOTHERDUCK_TOKEN = st.secrets.get("MOTHERDUCK_TOKEN", os.getenv("MOTHERDUCK_TOKEN"))

if not MOTHERDUCK_TOKEN:
    st.error("🚨 **Missing MotherDuck Token!** Please go to your Streamlit Cloud app settings -> **Secrets**, and add: `MOTHERDUCK_TOKEN = 'your_token_here'`")
    st.stop()

@st.cache_data
def load_data_from_motherduck():
    connection_string = f"md:my_db?motherduck_token={MOTHERDUCK_TOKEN}"
    conn = duckdb.connect(connection_string, read_only=True)
    df = conn.execute("SELECT * FROM main.fct_marketing_performance").fetchdf()
    conn.close()
    return df

try:
    df = load_data_from_motherduck()
except Exception as e:
    st.error(f"🚨 **Database Connection Error:** {e}")
    st.stop()

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

# Add a simple chart with fallback check for column names
st.subheader("⚡ Spend by Channel")
if "utm_source" in df.columns:
    st.bar_chart(df, x="utm_source", y="spend")
else:
    # Fallback to the first available column if utm_source differs
    st.bar_chart(df, x=df.columns[0], y="spend")
