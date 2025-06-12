#  Fintech Customer Experience Analytics

##  Prerequisites

* **Python** 3.10 or higher
* **Git** (version control)
* **Oracle XE** (or PostgreSQL fallback for database storage)
* **VS Code** (with PowerShell or Terminal)

---

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lhiwi/fintech-customer-experience.git
   cd fintech-customer-experience
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv

   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
---

##  Project Structure

```
fintech-customer-experience/
├── src/               # Python modules (scraper, analysis, database loader)
├── scripts/           # Standalone executable scripts
├── notebooks/         # Jupyter notebooks for exploration and preprocessing
├── tests/             # pytest unit tests
├── .github/
│   └── workflows/     # CI/CD (GitHub Actions workflows)
├── .gitignore         # Git ignore file
├── requirements.txt   # Project dependencies
├── README.md          # Project overview (this file)
```

---

##  Branching Strategy

We follow a **task-based branching** workflow:

* `task-1`: Data Collection & Preprocessing
* `task-2`: Sentiment and Thematic Analysis
* `task-3`: Database Design and Loading
* `task-4`: Insights Visualization and Reporting

To create and switch to a task branch:

```bash
git checkout -b task-1
```

Merge completed work into `main` via **Pull Requests**.

---

##  Task 1: Data Collection & Preprocessing

* Scraped customer reviews from Google Play Store for:

  * Commercial Bank of Ethiopia (CBE)
  * Bank of Abyssinia (BOA)
  * Dashen Bank
* Preprocessing steps:

  * Removed duplicate and incomplete entries
  * Standardized date formats
* **Output**:

  * `data/bank_reviews_clean.csv` — Cleaned dataset

---

##  Task 2: Sentiment and Thematic Analysis

* Used `distilbert-base-uncased-finetuned-sst-2-english` for sentiment classification
* Assigned each review:

  * `sentiment_label` (POSITIVE/NEGATIVE)
  * `sentiment_score` (confidence level)
* Extracted key themes using **TF-IDF** and **NLTK**:

  * Identified recurring issues like “login errors” and “slow transactions”
  * Grouped into themes such as **Access Issues**, **Performance**, **UI/UX**, **Support**
* **Output**:

  * `data/reviews_with_sentiment.csv` — with sentiment scores
  * `data/keywords_nltk.csv` — extracted keywords
  * `data/reviews_labeled.csv` — reviews tagged with themes

---

##  Task 3: Database Design and Loading

* Designed a relational schema with:

  * `banks` table for metadata
  * `reviews` table for processed review entries
* Created tables in **Oracle XE**
* Loaded 1,200+ labeled reviews using a Python insert script via `oracledb`
* **Output**:

  * `scripts/load_to_oracle.py` — ETL script
  * Oracle schema with populated data
  * SQL dump for backup and reuse

---

##  Task 4: Insights Visualization and Reporting

* Generated key business insights per bank:

  * **Pain Points**: login failures, crashes, server delays
  * **Satisfaction Drivers**: ease of transfer, good UI
* Created stakeholder-friendly visualizations:

  * Sentiment distribution per bank
  * Word clouds for positive/negative reviews
  * Heatmap of rating vs sentiment
* Delivered recommendations for app improvement
* **Output**:

  * `notebooks/Insights&visualizations.ipynb`
  * `docs/final_report.pdf` — Medium-style report (7 pages, 7+ plots)

---

##  Project Objective

To analyze user feedback from fintech apps and provide **data-driven recommendations** to:

* Improve mobile app performance and usability
* Boost customer satisfaction
* Reduce churn through targeted enhancements

By leveraging NLP, data engineering, and visualization, this project helps Ethiopian banks **translate customer voices into actionable change**.
