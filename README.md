#  Fintech Customer Experience Analytics

## Prerequisites

* **Python** 3.8 or higher
* **Git** (version control)
* **Oracle XE** (or PostgreSQL fallback for database storage)
* **VS Code** (with PowerShell or Terminal)

##  Installation & Setup

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
├── docs/              # Challenge documentation and final reports
├── .github/
│   └── workflows/     # CI/CD (GitHub Actions workflows)
├── .gitignore         # Git ignore file
├── requirements.txt   # Project dependencies
├── README.md          # Project overview (this file)
└── LICENSE            # License (e.g., MIT)
```

---

##  Branching Strategy

We follow a **task-based branching** workflow:

* `task-1`: Data Collection & Preprocessing
* `task-2`: Sentiment and Thematic Analysis
* `task-3`: Database Design and Loading
* `task-4`: Insights Visualization and Reporting

**Create and switch to a task branch**:

```bash
git checkout -b task-1
```

Merge completed work into `main` via **Pull Requests**.
Pull Requests trigger the CI/CD pipelines configured for `task-*` branches and `main`.

---

##  Task 1: Data Collection & Preprocessing

* **Scraped** customer reviews from Google Play Store for:

  * Commercial Bank of Ethiopia
  * Bank of Abyssinia
  * Dashen Bank
* **Preprocessing** steps:

  * Removed duplicate reviews
  * Dropped reviews with missing data
* **Output**:

  * `data/bank_reviews_clean.csv` — cleaned dataset

---

## Customer Experience Analytics for Fintech Apps

In this project, customer reviews from the Google Play Store are analyzed to derive actionable insights for mobile banking apps. Key deliverables include:

* **Sentiment Analysis**: Categorize reviews into positive, neutral, and negative sentiments.
* **Thematic Analysis**: Extract key themes (e.g., UI/UX, performance, feature requests) using keyword extraction and topic modeling techniques.
* **Pain Points and Satisfaction Drivers**: Identify and prioritize issues users face and features they appreciate.
* **Visualization and Reporting**: Create clear, stakeholder-friendly charts and summaries to guide app improvement strategies.

The goal is to enable Ethiopian banks to **enhance customer satisfaction** and **retain users** by addressing real-world feedback.

---

 **Now ready for Task 2: Sentiment and Thematic Analysis!**
