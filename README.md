# Iran Digital Blackout Sentiment 🕊️

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

---
## 🐧 Scraper Installation 
### Prerequisites
- python 3.8+
- pip 26.1.1+ package manager
- chrome browser
- Git

---

### Step 1: Clone the Repository
```
git clone https://github.com/aydakikio/Iran_digital_blackout_sentiment.git

cd Iran_digital_blackout_sentiment
```

### Step 2: Create Virtual Environment
```
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
There are multiple ways to install the required packages, depending on which website do you consider to scrape.

- **offline iran Scraper**
```
cd Scrapers/Offline_Iran/
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

- **offline iran Scraper**
Create a `.env` file in `Scrapers/Offline_Iran` and Set this variable,replace YOUR_DATABASE_URL with your actual database connection string, e.g., postgresql://user:pass@localhost/dbname
```
OFFLINE_IRAN_DB_URL=YOUR_DATABSE_URL
```
### Step 5: Configure Database Migration (SQL based databased)

### Step 6: Running the Scraper
- **Offline Iran Scraper**
```
python -m Scrapers.Offline_Iran.offline_iran
```
---
## 🤝 Contributing
we welcome contributions from researchers, developers. 

### Types of Contributions
- **Code Improvements** - Bug fixes, optimizations, new features
- **Report Bug**: Report bugs using a comprehensive template
- **Data Collection** - Help expand data sources and coverage
- **Documentation** - Improve guides, examples, and tutorials
- **Testing** - Test edge cases and report issues

---
## 👨‍💻 Developer Guidelines

