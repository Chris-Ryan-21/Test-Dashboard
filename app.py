# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:24:46 2025

@author: CRyan
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# New section: Histogram
st.subheader(f"Exposure Histogram for {selected_cp}")

# Assuming your exposure is in a column called "Exposure" (or similar)
if 'Exposure' in filtered_df.columns:
    fig, ax = plt.subplots()
    ax.hist(filtered_df['Exposure'], bins=10, color='skyblue', edgecolor='black')
    ax.set_xlabel('Exposure Amount')
    ax.set_ylabel('Frequency')
    ax.set_title(f"Histogram of Exposure - {selected_cp}")
    st.pyplot(fig)
else:
    st.write("No 'Exposure' column found to plot.")