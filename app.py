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

# Create a bar chart of each counterparty's exposure
st.subheader("Exposure per Counterparty")

fig, ax = plt.subplots()
ax.bar(df['Counterparty'], df['Exposure'], color='skyblue', edgecolor='black')
ax.set_xlabel('Counterparty')
ax.set_ylabel('Exposure')
ax.set_title('Exposure by Counterparty')
plt.xticks(rotation=45, ha='right')  # rotate x-axis labels for better readability

st.pyplot(fig)
