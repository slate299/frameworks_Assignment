# ================================
# Part 4: Streamlit App
# ================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# -----------------------------
# Load prepared dataset
# -----------------------------
df = pd.read_csv("metadata_prepared.csv", low_memory=False)

# -----------------------------
# Streamlit Layout
# -----------------------------
st.title("CORD-19 Data Explorer")
st.write("""
Explore COVID-19 research papers: publications over time, top journals, 
frequent title words, and source distribution.
""")

# -----------------------------
# Interactive Year Filter
# -----------------------------
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (2020, 2021))

# Filter dataframe based on slider
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -----------------------------
# 1. Publications per Year
# -----------------------------
st.subheader("Publications per Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# -----------------------------
# 2. Top 10 Journals
# -----------------------------
st.subheader("Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# -----------------------------
# 3. Word Cloud of Titles
# -----------------------------
st.subheader("Word Cloud of Paper Titles")
all_titles = " ".join(filtered_df['title'].dropna()).lower()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
fig_wc, ax_wc = plt.subplots(figsize=(15,7))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis('off')
st.pyplot(fig_wc)

# -----------------------------
# 4. Paper Counts by Source
# -----------------------------
st.subheader("Paper Counts by Source")
source_counts = filtered_df['source_x'].value_counts()
st.bar_chart(source_counts)

# -----------------------------
# 5. Sample Papers Table
# -----------------------------
st.subheader("Sample Papers")
st.write(filtered_df[['title', 'abstract', 'year']].head(10))
