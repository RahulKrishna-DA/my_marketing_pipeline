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

# Load the raw data from the database
raw_df = load_data_from_duckdb()

# ==========================================
# NEW: INTERACTIVE SIDEBAR FILTERS 🎛️
# ==========================================
st.sidebar.header("Filter Analytics View")

# 1. Channel Filter Dropdown
# Gets unique channels from your utm_source column and adds an "All" option
channels = ["All"] + list(raw_df['utm_source'].unique())
selected_channel = st.sidebar.selectbox("Select Marketing Channel", channels)

# 2. Spend Threshold Slider
# Filters out rows where the ad spend was lower than a certain amount
max_spend = float(raw_df['spend'].max())
min_spend = float(raw_df['spend'].min())
selected_spend_limit = st.sidebar.slider("Minimum Spend Threshold ($)", min_spend, max_spend, min_spend)

# ==========================================
# NEW: FILTER LOGIC BASED ON USER CLICKS ⚡
# ==========================================
# Apply the slider filter first
filtered_df = raw_df[raw_df['spend'] >= selected_spend_limit]

# Apply the channel dropdown filter next
if selected_channel != "All":
    filtered_df = filtered_df[filtered_df['utm_source'] == selected_channel]


# ==========================================
# METRICS & CHARTS (Now using filtered_df!)
# ==========================================
# Show key metrics based on user selections
total_spend = filtered_df['spend'].sum()
total_revenue = filtered_df['revenue'].sum()
avg_roas = filtered_df['roas'].mean() if not filtered_df.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Spend", f"${total_spend:,.2f}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
# Fixed a small edge case: round to 2 decimals to match your string conversion
col3.metric("Average ROAS", f"{avg_roas:.2f}x")

st.divider()

# Display the filtered Mart Data Table
st.subheader("📊 Final Mart Data Preview")
st.dataframe(filtered_df, use_container_width=True)

# Add an interactive chart that changes dynamically
st.subheader("⚡ Spend by Channel")
st.bar_chart(filtered_df, x="utm_source", y="spend")
