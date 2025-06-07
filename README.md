# 📰 Financial News Impact Analysis

This repository contains the setup and development for **Financial News Impact Analysis**, a hands-on financial analytics challenge.

The project explores how real-world financial news headlines influence stock price movements by combining **Natural Language Processing (NLP)**, **technical indicators**, and **quantitative correlation analysis**.

It includes:

- A reproducible Python data science environment
- Proper `.gitignore` and dependency management
- GitHub Actions CI workflow for clean installs and testing
- Structured code for sentiment analysis, EDA, and time-series modeling

The goal is to uncover actionable insights by linking headline sentiment to daily stock returns and suggesting predictive strategies for future price movement.

---

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Tensaey-sol/financial-news-impact-analysis.git
cd financial-news-impact-analysis
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧱 Project Structure

```
financial-news-impact-analysis/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions workflow
├── .gitignore                 # Ignore rules for Git
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── notebooks/                 # Jupyter notebooks
│   └── README.md
├── tests/                     # Testing utilities
│   ├── __init__.py
├── scripts/                   # Script utilities
│   ├── __init__.py
│   └── README.md
├── data/                      # Raw and processed datasets (ignored via .gitignore)
└── .venv/                     # Local virtual environment (excluded from version control)
```

---

## ⚙️ GitHub Actions CI

A continuous integration workflow is configured to automatically run when changes are pushed to a branch:

- Uses **Python 3.13.1**
- Installs dependencies from `requirements.txt`
- Runs basic tests from `/tests`
- Workflow is defined in `.github/workflows/ci.yml`

You can view its status in the **Actions** tab of the GitHub repository.

---

## 🛠 Tools Used

- Python **3.13.1**
- **VSCode** (Recommended editor)
- `venv` for isolated Python environments
- Git & GitHub for version control
- GitHub Actions for automation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Questions?

If you have any questions, suggestions, or contributions, feel free to open an issue or submit a pull request.
