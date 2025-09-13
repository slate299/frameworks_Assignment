# Python Frameworks Assignment – CORD-19 Data Exploration

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#)

---

## Table of Contents

1. [Overview](#1-overview)  
2. [Dataset](#2-dataset)  
3. [Project Steps](#3-project-steps)  
   - [Part 1: Data Loading & Exploration](#part-1-data-loading--exploration)  
   - [Part 2: Data Cleaning & Preparation](#part-2-data-cleaning--preparation)  
   - [Part 3: Data Analysis & Visualization](#part-3-data-analysis--visualization)  
   - [Part 4: Streamlit Application](#part-4-streamlit-application)  
4. [Key Findings](#4-key-findings)  
5. [Challenges](#5-challenges)  
6. [Reflection & Learning](#6-reflection--learning)  
7. [How to Run](#7-how-to-run)  
8. [Project Structure](#8-project-structure)  
9. [Requirements](#9-requirements)  
10. [Submission](#10-submission) 

---

## 1. Overview

This project explores the **CORD-19 research dataset** of COVID-19 research papers. The goal is to **load, clean, analyze, and visualize the dataset**, and then present the findings using a **Streamlit web application**.

**Tools Used:** Python, pandas, matplotlib, seaborn, WordCloud, Streamlit

---

## 2. Dataset

* File: `metadata.csv` (subset of CORD-19 metadata)  
* Columns include: Paper title, abstract, authors, journal, source, publication date, etc.  
* Cleaned and prepared version: `metadata_prepared.csv` (used for analysis and visualizations)  
* ⚠️ **Note:** The `metadata.csv` file is very large (\~1.6 GB) and is **not included in the repo** due to GitHub size limits. Download it separately from [Kaggle CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and place it in the project folder.  
* 💡 **Tip:** Ensure your machine has sufficient RAM to handle the dataset.

---

## 3. Project Steps

### Part 1: Data Loading & Exploration

* Loaded dataset using pandas.
* Explored shape, data types, and missing values.
* Saved a cleaned CSV for further analysis.

### Part 2: Data Cleaning & Preparation

* Dropped empty columns (`mag_id`, `who_covidence_id`, `arxiv_id`, `s2_id`).
* Filled missing values in `abstract`, `authors`, and `journal`.
* Converted `publish_time` to datetime and extracted the `year`.
* Added `abstract_word_count` for text analysis.
* Saved as `metadata_prepared.csv`.

### Part 3: Data Analysis & Visualization

* Counted publications per year.
* Identified top 10 journals publishing COVID-19 research.
* Created a word cloud of paper titles.
* Plotted distribution of papers by source.

### Part 4: Streamlit Application

* Built an interactive web app (`app.py`) to display findings.
* Features:

  * Year range slider to filter publications
  * Publications per year bar chart
  * Top 10 journals chart
  * Word cloud of paper titles
  * Paper source distribution
  * Sample table of research papers

#### Streamlit App Screenshots

> Screenshots below show the Streamlit app interface and example visualizations.

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

* Research activity peaked in **\[insert peak year from your plot]**.
* Top journals publishing COVID-19 research include **\[insert top 3 journals]**.
* Frequent words in titles highlight a focus on **\[insert key topics from word cloud]**.
* Most papers came from sources like **PMC, MedRxiv**, etc.

---

## 5. Challenges

* Large dataset required filtering to a manageable subset.
* Handling missing values across multiple columns.
* Generating readable visualizations and word clouds with many titles.

---

## 6. Reflection & Learning

* Learned how to clean and prepare real-world datasets.
* Practiced creating visualizations with matplotlib and WordCloud.
* Built a functional Streamlit app to present findings interactively.
* Documented the entire workflow and prepared files for submission.

---

## 7. How to Run

### Jupyter Notebook

1. Download `metadata.csv` from Kaggle and place it in the project folder.
2. Open `exploration.ipynb` in Jupyter Notebook.
3. Run the cells sequentially to explore, clean, and visualize the data.

### Streamlit App

1. Make sure `metadata_prepared.csv` is in the project folder.
2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. The app will open in your browser. Use the sliders and dropdowns to interact with the visualizations.

---

## 8. Project Structure

```
Frameworks_Assignment/
│
├─ exploration.ipynb        # Jupyter notebook with analysis
├─ app.py                   # Streamlit interactive app
├─ metadata_clean.csv       # Cleaned CSV (optional)
├─ metadata_prepared.csv    # Prepared dataset for analysis
├─ README.md                # Project documentation
├─ requirements.txt         # Python packages required
└─ images/                  # Screenshots for README
    ├─ streamlit_home.png
    ├─ publications_per_year.png
    ├─ top_journals.png
    ├─ wordcloud_titles.png
    ├─ source_distribution.png
    └─ sample_papers.png
```

---

## 9. Requirements

Create `requirements.txt` with the following packages:

```
pandas
matplotlib
seaborn
streamlit
wordcloud
```

> Optional: To freeze exact versions for reproducibility:

```bash
pip freeze > requirements.txt
```

---

## 10. Submission

* **GitHub Repository:** [https://github.com/slate299/frameworks\_Assignment](https://github.com/slate299/frameworks_Assignment)
* Include all files **except the large CSVs**, which users download from Kaggle.

---

