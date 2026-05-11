# Iran Digital Blackout Sentiment 🕊️

<p align="center">
  
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow?style=for-the-badge&logo=gnu&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=ffd343)](https://python.org)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://kaggle.com/your-link)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model-FF9D00?style=for-the-badge&logo=huggingface)](https://huggingface.co/HooshvareLab/bert-base-parsbert-uncased)
<br>
[![CI Status](https://img.shields.io/github/actions/workflow/status/aydakikio/Iran_digital_blackout_sentiment/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/aydakikio/Iran_digital_blackout_sentiment/actions)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Botasaurus](https://img.shields.io/badge/Botasaurus-Scraper-6C3483?style=for-the-badge&logo=python&logoColor=white)](https://github.com/omkarcloud/botasaurus)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)](https://neo4j.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

</p>

<p align="center">
  <a href="#-overview">Overview🦤</a> •
  <a href="#-features">Features✨</a> •
   <a href="#-data-set">Dataset🪿</a> •
  <a href="#-scraper-installation">Installation🐧</a> •
  <a href="#-contributing">Contribute🤝</a> •
  <a href="#%E2%80%8D-developer-guidelines">Developer Guidelines 🐳</a>
</p>


For the shouts of innocent people that faded into darkness of Internet blackout 🕊️ 

An aspect based sentiment analysis of Persian comments on internet blackouts using machine learning and NLP techniques.

> [!WARNING]
> This research is in active development. Findings, methods, datasets,documentations, and conclusions may change at any time. Results may be incomplete or contain errors. Use at your own risk and do not consider them final, verified, or ready for citation.


## 📖 Overview
This project analyzes public sentiment regarding internet blackout and digital isolation in Iran through aspect-based sentiment analysis. By processing Persian comments from [Offline Iran](https://offlineiran.com/),[Citna](https://www.citna.ir/), [Zoomit](https://www.zoomit.ir/),[Digiato](https://digiato.com/), we extract key aspects (e.g., "government policy," "network quality," "economic impact") and determine sentiment polarity for each aspect.

Iran has experienced slow, heavily filtered internet connection and holds the record for the longest nationwide internet blackout (72 days).Many online businesses are destroyed and more people have fallen into poverty by losing thier job. There is no official announcement on when the internet connection will be restored. There is some news about the classification of the Internet that shows the injustice on a broader scale, and some leaked documents show that this process was created to increase censorship and expand suppression horizontally.

### 🗝️ Research Key Goals
- Extract meaningful aspects from Persian text about internet outages
- Classify sentiment (positive, negative, neutral) for each aspect
- Provide insights into public perception and concerns
- Create a reusable pipeline for Persian sentiment analysis

---

## ✨ Features
- **Persian Language Support**: Full UTF-8 support and dedicated preprocessing pipeline for Persian text (normalization, half-space handling, tokenization).
- **Public Datasets**: The gathered data will be published on GitHub and Kaggle to enable community access and reproducibility.
- **Scraper Architecture Documentation**: All scraper architecture documents are available [here](https://github.com).
- **Modular Architecture**: Provides great flexibility to extend or replace components like scrapers, aspect extractors, and sentiment classifiers.
- **Multi-Database Design**: Supports multiple storage backends (e.g., SQLite for prototyping, PostgreSQL for production) with separate tables for raw comments, extracted aspects, and sentiment results.
- **Automated Kaggle Update**: The Kaggle dataset is refreshed automatically with the latest scraped and analyzed data via scheduled workflows.
- **Aspect-Based Sentiment Analysis**: Detects fine-grained aspects (e.g., “government policy”, “network quality”, “economic impact”) in each comment and determines sentiment polarity (positive, negative, neutral) for every aspect.
- **Persian-Specific Preprocessing**: Includes informal expression mapping, emoji removal, and normalization of Persian-specific characters to improve model accuracy.
- **Model Evaluation & Benchmarking**: Provides standard metrics (F1-score, accuracy, confusion matrix) and benchmark results on the collected Persian dataset to ensure transparency.

---

## 📊 Data set
The dataset collected from Feb 27, 2026 to ??  
*(status: ongoing / to be updated)*

### Data Sources
- **[Offline Iran](https://offlineiran.com/)**
- **[Digiato](https://digiato.com/)**
- **[Citna](https://www.citna.ir/)**
- **[Zoomit](https://www.zoomit.ir/)**

### 🦤 Scrape Schedule

| Website Name  | Session |Data From | Data To | Scrape Start date | Scrape End date | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  [Offline Iran](https://offlineiran.com/) | **#1** | Feb 28 2026  | May 10 2026 | 10 May 2026 (10:19Z) | 10 May 2026 (19:01Z) | 🟢 Finished |
| [Citna](https://www.citna.ir/) | **#1** | - | - | - | - | 🟠 Not started | 
| [Zoomit](https://www.zoomit.ir/) | **#1** | - | - | - | - | 🟠 Not started | 
| [Digiato](https://digiato.com/) | **#1** | - | - | - | - | 🟠 Not started | 


### 🧭 Accessing the Dataset
Comming Soon!

---
## 🐧 Scraper Installation 

### Offline Iran Scraper

#### Prerequisites
- python 3.8+
- pip 26.1.1+ package manager
- chrome browser
- PostgreSQL
- Git


#### Step 1: Clone the Repository
```
git clone https://github.com/aydakikio/Iran_digital_blackout_sentiment.git

cd Iran_digital_blackout_sentiment
```

#### Step 2: Create Virtual Environment
```
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 3: Install Dependencies
```
cd Scrapers/Offline_Iran/
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables
Create `.env` file 
```
nano .env 
```

Set this variable,replace `YOUR_DATABASE_URL` with your actual database connection string

```
OFFLINE_IRAN_DB_URL=YOUR_DATABSE_URL
```

#### Step 5: Configure Database Migration

Create `alembic.ini` file 
```
mv alembic.ini.example alembic.ini
```
replace `YOUR_DATABSE_URL` with your postgerSQL
```
sqlalchemy.url = YOUR_DATABSE_URL
```

#### Step 6: Running the Scraper
```
python -m Scrapers.Offline_Iran.offline_iran
```
---
## 🤝 Contributing

We welcome contributions from researchers, developers. Before submitting, please review the guidelines below to ensure your contribution can be integrated smoothly.

### Types of Contributions
- **Code Improvements** - Bug fixes, optimizations, new features
- **Report Bug**: Report bugs using a comprehensive template
- **Data Collection** - Help expand data sources and coverage
- **Documentation** - Improve guides, examples, and tutorials
- **Testing** - Test edge cases and report issues

### 🪴 How to Contribute? 

#### 🛡️ Step 0 – Avoid Duplicate Work
1. **Search open Issues & Pull Requests** – look for keywords related to your idea.  
2. **Check the Project Board** – if an issue is in the `In Progress` column, it’s already taken.  
3. **Claim the task before coding** – comment exactly `/claim` on the issue.  
   - A maintainer will assign you or add the `in progress` label.  
   - Do **not** start until you see that label.  
4. **If no issue exists**, create one first and wait for acknowledgment.  
5. **Already started?** Open a [Draft Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests) immediately with `[WIP]` in the title — this makes your work visible to others.

> ⚡ **Why this matters:** It prevents the awful feeling of discovering someone else already implemented the same thing.  
> If two people accidentally start the same task, we’ll coordinate in the issue thread and merge the best of both. No effort is wasted.

#### 🌿 Contribution Labels

| Label | Meaning |
|-------|---------|
| `in progress` | Someone is actively working on this — please pick something else. |
| `up for grabs` | Ready for anyone to claim. |
| `help wanted` | Extra hands are welcome; coordinate in the issue. |

---

### 🧑‍💻 Step-by-Step (After Your Task Is Claimed)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/aydakikio/Iran_digital_blackout_sentiment.git
   ```

2. **Create a feature branch**  
   ```bash
   git checkout -b feature/descriptive-name
   ```
   Use prefixes like `fix/`, `feat/`, `docs/` for clarity.

3. **Implement your changes**  
   - Follow the coding standards in our [Developer Guidelines](#‍-developer-guidelines).  
   - Run the tests on the provided sample data

4. **Write meaningful commits**  
   ```
   git commit -m "Fix: Resolve rate limit issue in Citizen scraper"
   ```

5. **Push your branch**  
   ```
   git push origin feature/descriptive-name
   ```

6. **Open a Pull Request**  
   - Use the PR template (if available).  
   - Clearly describe what changed and how you tested it.  
   - Reference the original issue (e.g., `Closes #12`).  
   - If your work is still in progress, mark it as a **draft**.

7. **Review & Iterate**  
   - Maintainers will review and may request changes.  
   - Once approved, your PR will be merged. Awesome! 🎉


#### 🔧 Need Help?
If anything in this process is unclear, just open a **Discussions** thread or comment on the issue itself.  
We’re here to make contributing a pleasant experience — you’re doing great!

 
**Pull Request Requirements:**
- Code compiles without warnings
- Follows existing code style and naming conventions
- Includes comments for complex logic
- No debug code or commented-out sections


### Bug Reports 🐛

When reporting bugs, provide complete technical details to enable efficient reproduction and resolution.

**Required Information:**

```
## Bug Description
[Clear, concise description of the issue]

## Reproduction Steps
1. [First step, e.g., run a specific script or send a request to a URL]
2. [Second step, e.g., input a specific Persian comment into the pipeline]
3. [Additional steps...]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- **OS:** [Windows 10 / Ubuntu 22.04 / macOS 13]
- **Python Version:** [e.g., 3.10.11]
- **Virtual Environment:** [venv / conda / poetry]
- **Key Libraries & Versions:**
  - Scrapy / BeautifulSoup4: [version]
  - Transformers / Hazm / Parsivar: [version]
  - Database adapter (psycopg2, sqlite3): [version]
  - Dashboard framework (Streamlit / Dash / Flask): [version]
  - Other relevant libraries (pandas, numpy, etc.)
- **Database Type & Version:** [SQLite 3.35 / PostgreSQL 15]
- **Scraping Target:** [Citna / Zoomit / Digiato / Offline Iran] (and the specific page/API if relevant)

## Data Context
- **Sample Input (if applicable):** [The Persian comment text that caused the error]
- **Data Volume:** [Approximate number of comments / size of dataset being processed]
- **Pipeline Stage:** [Scraping / Preprocessing / Aspect Extraction / Sentiment Classification / DB Storage / Dashboard]

## Logs / Error Messages

## Scraper-Specific Information (if scraping issue)
- **Configuration Files Modified:** [Yes/No – specify]
- **Proxy/VPN Used:** [Yes/No – details if yes]
- **robots.txt Respect:** [Yes/No]
- **Headers / User-Agent Override:** [Specify]
- **Anti-bot Measures Encountered:** [CAPTCHA, 403, redirect, etc.]

## Model / NLP Details (if analysis issue)
- **Model Name/Version:** [e.g., bert-base-fa-sentiment, custom model hash]
- **Tokenizer:** [Hazm / Parsivar / bert-tokenizer]
- **Aspect List Used:** [e.g., "government policy", "network quality", "economic impact"]
- **Preprocessing Flags:** [e.g., emoji removal enabled, half-space normalization]

## Automation / Scheduler (if Kaggle update issue)
- **Workflow Engine:** [GitHub Actions / Cron / Airflow]
- **Scheduled Time:** [UTC time]
- **Last Successful Run:** [date/time]
- **Error Log from Scheduler:** [paste if available]

## Attempted Solutions
[What you've already tried to fix the issue]

## Additional Context
- Does the problem occur consistently or intermittently?
- Any manual code modifications that might be relevant.
- Screenshots of the dashboard (if applicable).
- Relevant `pip freeze` or `requirements.txt` output.
```


### Feature Requests

For new features, open an issue describing:
- **Use case and benefits** – what problem does it solve and how does it improve the project?
- **Proposed implementation approach** – which module(s) would be affected (scrapers, preprocessing, ABSA pipeline, dashboard, etc.) and a rough technical plan.
- **Performance/resource impact** – expected effect on memory consumption, processing time, database size, or model inference speed.
- **Data and language considerations** – any impact on Persian text handling, new data sources, or compatibility with existing aspects.


### Contribution Areas

**High Priority:**
- Scraper robustness and efficiency improvements (handling anti-bot measures, reducing request time)
- Memory and speed optimizations in the preprocessing/ABSA pipeline
- Critical bug fixes (data corruption, silent failures in extraction, dashboard crashes)
- Improvements to aspect extraction accuracy (especially for rare or overlapping aspects)

**Accepted Contributions:**
- New scraper modules for additional Persian-language sources (news sites, forums, social media)
- Enhanced sentiment classification with newer Persian NLP models (e.g., fine-tuned BERT variants)
- Additional aspect categories and automatic aspect discovery methods
- Dashboard visualizations and filtering options (time range, source, sentiment distribution)
- Multilingual support (adding English translations or extending to other languages)
- Auto-labelling or active learning tools to assist dataset growth
- Database backend extensions (e.g., PostgreSQL migration scripts, schema versioning)
- Automated model retraining and evaluation pipelines

**Documentation:**
- Scraper setup and configuration guides
- Database schema and data dictionary documentation
- ABSA pipeline architecture and flow diagrams
- Kaggle dataset usage and update frequency documentation
- Local development environment setup (Python version, dependencies, virtual environment)
- Troubleshooting guides for common scraping or preprocessing issues
- Code architecture documentation (module interactions, data flow)

---
## 👨‍💻 Developer Guidelines

### Coding Standards
- Use **snake case** conventions for floders, variables, classes and functions
- Add **type hints** to function signatures and complex variables (`def preprocess(text: str) -> List[str]:`).
- **Import order**: standard library → third-party → local modules, each group separated by a blank line.
- Use absolute imports from the project root (e.g., from Scrapers.Offline_Iran.Modules.Extractor import offline_iran_extractor), as shown in the existing scrapers.
- Write comments that explain the confusing part of codes

### Branch Naming

### Branch Naming Convention

We use a **structured branch naming** convention to make it immediately clear what a branch is for.
Every branch name starts with a **type prefix** followed by a short, hyphenated description.

**Examples you'll see in the repository:**

| Branch Name | What It Means |
|-------------|---------------|
| `feature/add-aspect-extraction` | A new feature: adding aspect extraction to the pipeline. |
| `bugfix/fix-persian-encoding` | A bug fix: correcting problems with Persian text encoding. |
| `docs/update-installation-guide` | A documentation-only change: updating the installation guide. |
| `refactor/optimize-pipeline` | Code refactoring: making the pipeline faster or cleaner without changing behavior. |

**Why we do this:**
- **Scannability** — anyone can glance at the branch list and know what’s in progress.
- **Automatic changelogs** — tools can group commits by type when generating release notes.
- **No guesswork** — you don't have to open a branch to understand its purpose.

**Allowed prefixes:**
- `feature/` – new functionality
- `bugfix/` or `fix/` – bug repairs
- `docs/` – documentation only
- `refactor/` – code restructuring (no new features, no bug fixes)
- `chore/` – maintenance tasks (dependency updates, config changes)
- `test/` – adding or updating tests

When you create a branch, follow exactly this pattern:
```
git checkout -b prefix/short-descriptive-name

```

### Commit Message Format

```
<type>(<scope>): <subject>

<explanation>
```

- **Types:** feat, fix, docs, style, refactor, test, chore
- **Scopes:** scraper, preprocessing, analysis, models, tests

**Example:**

```
feat(scraper): add Telegram channel support

Implemented async data collection from Telegram channels
with rate limiting and error handling.
```

### Testing Requirements

All new features must include tests:

```
# Run all tests
pytest

# Run specific test file
pytest tests/test_aspect_extractor.py

# Run with coverage
pytest --cov=src --cov-report=html
```

### Performance Considerations

- ⚡ Optimize for processing 1000+ comments/hour
- 💾 Minimize memory footprint with generators
- 🔄 Cache preprocessed data and models
- 📊 Profile code with `cProfile` before optimization

### Documentation

- Add docstrings to all functions and classes
- Update README for major changes
- Document API endpoints and parameters
- Include examples in docstrings

---
<p align="center">
  <a href="#iran-digital-blackout-sentiment-%EF%B8%8F">Back to top ↑</a>
</p>
