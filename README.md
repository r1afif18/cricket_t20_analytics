# 🏏 T20 Cricket Analytics: From EDA to Interactive Web App

**This repository contains a complete data analytics project for T20 International Cricket matches — starting from data cleaning and exploration (EDA) in Jupyter Notebook to a fully interactive Streamlit web app for everyone to use.**

---

## 🚀 [Live Web App](https://crickett20analytics.streamlit.app/)

---

## 📊 Project Overview

This project has two main components:

1. **Exploratory Data Analysis (EDA):**
   - A Jupyter Notebook that documents the process of cleaning, exploring, and discovering insights from raw T20 cricket match data.
   - Prepares clean, ready-to-use data for further analysis or dashboarding.

2. **Interactive Web Application:**
   - Built with Streamlit to visualize and interactively explore cricket data.
   - Lets users filter, visualize, and analyze key stats for teams and players.

---

## 📓 EDA Notebook

The notebook (`notebooks/01-eda-cricket.ipynb`) covers:
- Understanding the structure and quality of the dataset
- Cleaning anomalies and missing values
- Discovering key patterns and trends (team & player performance)
- Prepping data for visualization and app

---

## ✨ Main Features (Web App)

- **Overall Analysis:**  
  See aggregate stats for all matches, including total runs, wickets, and team summaries.
- **Team vs Team (Head-to-Head):**  
  Compare two teams' stats and match histories (upgrade this in dashboard as needed!).
- **Player Performance:**  
  Detailed batting & bowling analysis per player.
- **Interactive Visualizations:**  
  Easy-to-read charts and plots using Plotly.
- **Dynamic Filtering:**  
  Slice data by team, player, or year to find specific insights.
- **Responsive UI:**  
  Clean, modern layout ready for desktop and mobile.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Jupyter Notebook, Pandas, NumPy
- **Data Visualization:** Plotly, Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Deployment:** Streamlit Community Cloud

---

## ⚡ How To Run Locally

```sh
git clone https://github.com/r1afif18/cricket_t20_analytics.git
cd cricket_t20_analytics

# (Optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

# Run the Streamlit app
streamlit run dashboard.py
Open your browser and go to http://localhost:8501.

📑 Dataset
Public T20 cricket match data

Sourced from Codebasics Power BI Project

CSVs included: match summaries, player info, batting and bowling stats

📸 App Screenshots
(Tip: Add screenshots of your dashboard here for extra visual impact!)

📄 License
MIT License — free for educational and portfolio use.

👤 About Me
Developed by Rafif Sudanta

GitHub

LinkedIn

Made with ❤️ for cricket fans and data enthusiasts worldwide!

