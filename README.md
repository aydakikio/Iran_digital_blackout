# Iran Digital Blackout 🕊️

<p align="center">
  
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow?style=for-the-badge&logo=gnu&logoColor=white)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=ffd343)](https://python.org)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://kaggle.com/your-link)
[![Botasaurus](https://img.shields.io/badge/Botasaurus-Scraper-6C3483?style=for-the-badge&logo=python&logoColor=white)](https://github.com/omkarcloud/botasaurus)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)](https://neo4j.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
<br>
</p>

<p align="center">
  <a href="#-overview">Overview🦤</a> •
  <a href="#-features">Features✨</a> •
  <a href="#-dataset">Dataset🪿</a> •
  <a href="#-scraper-installation">Installation🐧</a> •
  <a href="#-contributing">Contribute🤝</a> •
  <a href="#‍-developer-guidelines">Developer Guidelines🐳</a>
</p>

For the shouts of innocent people that faded into the darkness of Internet blackout 🕊️

A collection of Persian public comments on internet blackouts in Iran — scraped, cleaned, and published for open research.

> [!WARNING]
> This project is in active development. Data coverage, scraper behavior, and documentation may change at any time. The dataset is not yet complete. Do not treat current releases as final or exhaustive.

---

## 📖 Overview

Iran has experienced slow, heavily filtered internet and holds the record for the longest nationwide internet blackout (72 days). Many online businesses were destroyed and more people fell into poverty from losing their jobs. There is no official announcement on when connection will be restored. Leaked documents suggest this process was created to increase censorship and expand suppression horizontally.

This project collects Persian public comments from news and tech websites that covered internet blackouts in Iran. The goal is to build a clean, open, and well-documented dataset that can be used by researchers studying digital rights, censorship, or Persian NLP.

### 🗝️ Project Goals
- Scrape Persian comments from multiple sources covering internet blackouts
- Clean and normalize collected text (UTF-8, Persian-specific character handling)
- Publish the dataset openly on Kaggle and GitHub for community use
- Maintain a reproducible and extensible scraper architecture

---

## ✨ Features
- **Persian Language Support**: Full UTF-8 support and a dedicated preprocessing pipeline for Persian text (normalization, half-space handling, deduplication).
- **Public Dataset**: All collected data is published on Kaggle and GitHub to enable open access and reproducibility.
- **Scraper Architecture Documentation**: All scraper architecture documents are available in the repository.
- **Modular Scraper Design**: Scrapers are independent modules — easy to extend with new sources without touching existing ones.
- **Multi-Database Support**: Supports multiple storage backends (SQLite for prototyping, PostgreSQL for production) with separate tables for raw comments and metadata.
- **Automated Kaggle Updates**: The Kaggle dataset refreshes automatically with newly scraped data via scheduled GitHub Actions workflows.
- **Resumable Scraping**: Scrapers track progress and can resume from where they left off after interruption.

---

## 📊 Dataset

Data collection started Feb 27, 2026.  
*(status: ongoing / to be updated)*

### Data Sources
- **[Offline Iran](https://offlineiran.com/)**
- **[Digiato](https://digiato.com/)**
- **[Citna](https://www.citna.ir/)**
- **[Zoomit](https://www.zoomit.ir/)**

### 🦤 Scrape Schedule

| Website Name | Session | Data From | Data To | Scrape Start | Scrape End | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Offline Iran](https://offlineiran.com/) | **#1** | Feb 28 2026 | May 10 2026 | 10 May 2026 (10:19Z) | 10 May 2026 (19:01Z) | 🟢 Finished |
| [Offline Iran](https://offlineiran.com/) | **#2** | May 10 2026 | May 22 2026 | Jul 7 2026 (11:02Z) | Jul 7 2026 (11:25Z) | 🟢 Finished |
| [Offline Iran](https://offlineiran.com/) | **#3** | Jan 23 2026 | Feb 2 2026 | Jul 7 2026 (14:30Z) | Jul 7 2026 (18:30Z) | 🟢 Finished |
| [Citna](https://www.citna.ir/) | **#1** | - | - | - | - | 🟠 Not started |
| [Zoomit](https://www.zoomit.ir/) | **#1** | - | - | - | - | 🟠 Not started |
| [Digiato](https://digiato.com/) | **#1** | - | - | - | - | 🟠 Not started |

### 🧭 Accessing the Dataset

#### 1. Kaggle
🔗 [Iran Internet Shutdown Narratives on Kaggle](https://www.kaggle.com/datasets/aydakikio/iran-internet-shutdown-narratives)

#### 2. GitHub Release
🔗 [GitHub Releases](https://github.com/aydakikio/Iran_digital_blackout_sentiment/releases)

#### 3. Clone the Repository

**Step 1: Clone**
```bash
git clone https://github.com/aydakikio/Iran_digital_blackout_sentiment.git
```

**Step 2: Navigate to data**
```bash
cd Iran_digital_blackout_sentiment/data
```

### 🫖 Citation

If you use this dataset in your research or project, please cite it as:
```
@misc{
https://doi.org/10.34740/kaggle/dsv/16280371,
doi = {10.34740/KAGGLE/DSV/16280371},
url = {https://www.kaggle.com/dsv/16280371},
author = {{Ayda Khoshkhan}},
title = {Iran Internet Shutdown Narratives},
publisher = {Kaggle},
year = {2026}
}
```

---

## 🐧 Scraper Installation

### Offline Iran Scraper

#### Prerequisites
- Python 3.8+
- pip 26.1.1+
- Chrome browser
- PostgreSQL
- Git

#### Step 1: Clone the Repository
```bash
git clone https://github.com/aydakikio/Iran_digital_blackout_sentiment.git
cd Iran_digital_blackout_sentiment
```

#### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
cd Scrapers/Offline_Iran/
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables
Create a `.env` file:
```bash
nano .env
```

Set the following variable, replacing `YOUR_DATABASE_URL` with your actual connection string:
```
OFFLINE_IRAN_DB_URL=YOUR_DATABASE_URL
```

#### Step 5: Configure Database Migration
```bash
mv alembic.ini.example alembic.ini
```

Replace `YOUR_DATABASE_URL` with your PostgreSQL connection string inside `alembic.ini`:
```
sqlalchemy.url = YOUR_DATABASE_URL
```

#### Step 6: Run the Scraper
```bash
python -m Scrapers.Offline_Iran.offline_iran
```

---

## 🤝 Contributing

We welcome contributions from researchers and developers. Please review the guidelines below before submitting.

### Types of Contributions
- **Code Improvements** — Bug fixes, optimizations, new features
- **Bug Reports** — Report issues using the template below
- **Data Collection** — Help expand source coverage
- **Documentation** — Improve guides, examples, and setup instructions
- **Testing** — Test edge cases and report unexpected behavior

### 🪴 How to Contribute

#### 🛡️ Step 0 – Avoid Duplicate Work
1. **Search open Issues & Pull Requests** for keywords related to your idea.
2. **Check the Project Board** — if an issue is `In Progress`, it's already taken.
3. **Claim the task before coding** — comment exactly `/claim` on the issue. Wait for the `in progress` label before starting.
4. **If no issue exists**, open one first and wait for acknowledgment.
5. **Already started?** Open a [Draft Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests#draft-pull-requests) with `[WIP]` in the title immediately.

> ⚡ **Why this matters:** It prevents the awful feeling of discovering someone else already built the same thing. If two people accidentally start the same task, we'll coordinate in the issue thread and merge the best of both. No effort is wasted.

#### 🌿 Contribution Labels

| Label | Meaning |
|-------|---------|
| `in progress` | Someone is actively working on this — please pick something else. |
| `up for grabs` | Ready for anyone to claim. |
| `help wanted` | Extra hands are welcome; coordinate in the issue. |

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

3. **Implement your changes** following the [Developer Guidelines](#-developer-guidelines).

4. **Write meaningful commits**
   ```
   git commit -m "Fix: Resolve rate limit issue in Citna scraper"
   ```

5. **Push your branch**
   ```bash
   git push origin feature/descriptive-name
   ```

6. **Open a Pull Request**
   - Clearly describe what changed and how you tested it.
   - Reference the original issue (e.g., `Closes #12`).
   - If still in progress, mark it as a **draft**.

7. **Review & Iterate** — maintainers will review and may request changes. Once approved, it gets merged. 🎉

**Pull Request Requirements:**
- Code compiles without warnings
- Follows existing code style and naming conventions
- Includes comments for complex logic
- No debug code or commented-out sections

#### 🔧 Need Help?
Open a **Discussions** thread or comment on the issue. We're here to make contributing a pleasant experience!

### Contribution Areas

**High Priority:**
- Scraper robustness and efficiency (anti-bot handling, reduced request times, retry logic)
- Resumable scraping and crash recovery
- Critical bug fixes (data corruption, silent failures, duplicate records)
- Data deduplication and cleaning improvements

**Accepted Contributions:**
- New scraper modules for additional Persian-language sources (news sites, forums)
- Database backend extensions (schema versioning, migration scripts)
- Kaggle dataset automation improvements
- Documentation and setup guides

### Bug Reports 🐛

```
## Bug Description
[Clear, concise description of the issue]

## Reproduction Steps
1. [First step]
2. [Second step]
3. [Additional steps...]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- **OS:** [e.g., Ubuntu 22.04]
- **Python Version:** [e.g., 3.10.11]
- **Virtual Environment:** [venv / conda / poetry]
- **Key Libraries & Versions:**
  - Botasaurus: [version]
  - SQLAlchemy / psycopg2: [version]
  - pandas, requests, etc.: [versions]
- **Database Type & Version:** [e.g., PostgreSQL 15]
- **Scraping Target:** [Citna / Zoomit / Digiato / Offline Iran]

## Scraper Details
- **Configuration Files Modified:** [Yes/No — specify]
- **Proxy/VPN Used:** [Yes/No — details if yes]
- **robots.txt Respected:** [Yes/No]
- **Anti-bot Measures Encountered:** [CAPTCHA, 403, redirect, etc.]
- **Approximate Data Volume at Time of Error:** [number of records / pages]

## Logs / Error Messages
[paste here]

## Attempted Solutions
[What you've already tried]

## Additional Context
- Does the problem occur consistently or intermittently?
- Relevant `pip freeze` output if dependency-related.
```

### Feature Requests

For new features, open an issue describing:
- **Use case and benefits** — what problem does it solve?
- **Proposed implementation** — which module(s) would be affected and a rough technical plan.
- **Performance/resource impact** — effect on memory, processing time, or database size.

---

## 👨‍💻 Developer Guidelines

### Coding Standards
- Use **snake_case** for folders, variables, classes, and functions.
- Add **type hints** to function signatures (`def fetch_page(url: str) -> str:`).
- **Import order**: standard library → third-party → local modules, separated by blank lines.
- Use absolute imports from the project root (e.g., `from Scrapers.Offline_Iran.Modules.Extractor import offline_iran_extractor`).
- Write comments that explain the *why*, not just the *what*.

### Branch Naming

| Branch Name | What It Means |
|-------------|---------------|
| `feature/add-zoomit-scraper` | New feature: adding a Zoomit scraper. |
| `bugfix/fix-persian-encoding` | Bug fix: correcting Persian text encoding. |
| `docs/update-installation-guide` | Documentation update only. |
| `refactor/optimize-db-writes` | Refactoring: cleaner/faster DB writes, no behavior change. |

**Allowed prefixes:** `feature/`, `bugfix/`, `fix/`, `docs/`, `refactor/`, `chore/`, `test/`

```bash
git checkout -b prefix/short-descriptive-name
```

### Commit Message Format

```
<type>(<scope>): <subject>

<explanation>
```

- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **Scopes:** `scraper`, `preprocessing`, `database`, `pipeline`, `tests`

**Example:**
```
feat(scraper): add Zoomit scraper module

Implemented async comment collection from Zoomit article pages
with rate limiting, retry logic, and resume support.
```

### Testing Requirements

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_offline_iran_scraper.py

# Run with coverage
pytest --cov=src --cov-report=html
```

### Performance Considerations
- ⚡ Optimize for 1000+ records/hour throughput
- 💾 Use generators to minimize memory footprint
- 🔄 Cache session state to support resumable runs
- 📊 Profile with `cProfile` before optimizing

### Documentation
- Add docstrings to all functions and classes
- Update README for any major change
- Document database schema and field definitions
- Include usage examples in docstrings

---

<p align="center">
  <a href="#iran-digital-blackout--data-collection-%EF%B8%8F">Back to top ↑</a>
</p>
