import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Hospital Dashboard", layout="wide")

st.title("🏥 Hospital Resource Utilization & Patient Outcomes Dashboard")

# Load data
data = pd.read_csv("hospital_data.csv")

# Sidebar filters
st.sidebar.header("Filters")
department = st.sidebar.selectbox("Select Department", ["All"] + list(data["Department"].unique()))
date_range = st.sidebar.date_input("Select Date Range", [])

df = data.copy()

if department != "All":
    df = df[df["Department"] == department]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", len(df))
col2.metric("Bed Occupancy (%)", round(df["Bed_Occupancy"].mean(), 2))
col3.metric("Avg Length of Stay", round(df["Length_of_Stay"].mean(), 2))
col4.metric("Doctor Utilization (%)", round(df["Doctor_Utilization"].mean(), 2))

# Charts
st.subheader("📊 Department-wise Patient Count")
fig1 = px.bar(df, x="Department", title="Patients per Department")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🛏️ Bed Occupancy Trend")
fig2 = px.line(df, x="Date", y="Bed_Occupancy", title="Bed Occupancy Over Time")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("✅ Patient Outcomes Distribution")
fig3 = px.pie(df, names="Outcome", title="Patient Outcomes")
st.plotly_chart(fig3, use_container_width=True)
