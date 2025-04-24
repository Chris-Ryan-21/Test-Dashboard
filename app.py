# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:24:46 2025

@author: CRyan
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Client Exposure Report")

# Load the Excel data
df = pd.read_excel("test_report.xlsx")

# Show the raw data
st.subheader("Raw Data")
st.dataframe(df)

# Optional: Filter by cp
cp_options = df['Counterparty'].unique()
selected_cp = st.selectbox("Select a counterparty to filter", cp_options)

filtered_df = df[df['Counterparty'] == selected_cp]

st.subheader(f"Data for {selected_cp}")
st.dataframe(filtered_df)
