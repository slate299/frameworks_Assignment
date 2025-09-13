# Python Frameworks Assignment – CORD-19 Data Exploration

## 1. Overview
This project explores the CORD-19 research dataset of COVID-19 research papers. The goal is to **load, clean, analyze, and visualize the dataset**, and then present the findings using a **Streamlit web application**.  

Tools used: **Python, pandas, matplotlib, seaborn, WordCloud, Streamlit**.

---

## 2. Dataset
- File: `metadata.csv` (subset of CORD-19 metadata)
- Columns include: Paper title, abstract, authors, journal, source, publication date, etc.
- Cleaned and prepared version: `metadata_prepared.csv` (used for analysis and visualization)

---

## 3. Project Steps

### Part 1: Data Loading & Exploration
- Loaded dataset using pandas.
- Explored shape, data types, and missing values.
- Saved a cleaned CSV for further analysis.

### Part 2: Data Cleaning & Preparation
- Dropped empty columns (`mag_id`, `who_covidence_id`, `arxiv_id`, `s2_id`).
- Filled missing values in `abstract`, `authors`, and `journal`.
- Converted `publish_time` to datetime and extracted the `year`.
- Added `abstract_word_count` for text analysis.
- Saved as `metadata_prepared.csv`.

### Part 3: Data Analysis & Visualization
- Counted publications per year.
- Identified top 10 journals publishing COVID-19 research.
- Created a word cloud of paper titles.
- Plotted distribution of papers by source.

### Part 4: Streamlit Application
- Built an interactive web app (`app.py`) to display findings.
- Features:
  - Year range slider to filter publications
  - Publications per year bar chart
  - Top 10 journals chart
  - Word cloud of paper titles
  - Paper source distribution
  - Sample table of research papers

#### Streamlit App Screenshots

**Homepage**  
![Streamlit Home](images/streamlit_home.png)

**Publications per Year**  
![Publications per Year](images/publications_per_year.png)

**Top 10 Journals**  
![Top Journals](images/top_journals.png)

**Word Cloud of Titles**  
![Word Cloud](images/wordcloud_titles.png)

**Source Distribution**  
![Source Distribution](images/source_distribution.png)

**Sample Papers Table**  
![Sample Papers](images/sample_papers.png)

---

## 4. Key Findings
- Research activity peaked in **[insert peak year from your plot]**.
- Top journals publishing COVID-19 research include **[insert top 3 journals]**.
- Frequent words in titles highlight a focus on **[insert key topics from word cloud]**.
- Most papers came from sources like **PMC, MedRxiv**, etc.

---

## 5. Challenges
- Large dataset required filtering to a manageable subset.
- Handling missing values across multiple columns.
- Generating readable visualizations and word clouds with many titles.

---

## 6. Reflection & Learning
- Learned how to clean and prepare real-world datasets.
- Practiced creating visualizations with matplotlib and WordCloud.
- Built a functional Streamlit app to present findings interactively.
- Documented the entire workflow and prepared files for submission.

---

## 7. Files & Submission
- `exploration.ipynb` → Notebook with analysis and visualizations
- `app.py` → Streamlit interactive app
- `metadata_clean.csv` → Cleaned CSV (optional)
- `metadata_prepared.csv` → Prepared dataset for analysis
- `images/` → Folder containing all screenshots
- `README.md` → Project documentation
- **GitHub Repository:** [https://github.com/slate299/frameworks_Assignment.git]
