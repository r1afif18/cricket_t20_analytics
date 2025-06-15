# 🏏 T20 Cricket Analytics: From EDA to Interactive Web App

This repository documents the end-to-end process of a T20 cricket data analysis project.  
It showcases a complete data science workflow, beginning with in-depth Exploratory Data Analysis (EDA) in a Jupyter Notebook and culminating in a user-friendly, interactive Streamlit Web Application.

---

## 🗂️ Project Structure

cricket_t20_analytics/
├── data/ # All CSV data files
├── notebooks/
│ └── 01-eda-cricket.ipynb # EDA & initial analysis
├── dashboard.py # Main Streamlit web app
├── requirements.txt # Dependencies for easy install
└── README.md


---

## 📓 1. Exploratory Data Analysis (EDA)

Open `notebooks/01-eda-cricket.ipynb` to follow:
- Data understanding and quality checks
- Cleaning anomalies and missing values
- Discovering key patterns and trends (team & player performance)
- Preparing data for the dashboard

This notebook demonstrates the Python data science workflow — perfect for interviews or learning references!

---

## 🚀 2. Interactive Dashboard Application

The core insights from EDA are brought to life in an interactive Streamlit web app.

**Live Application:**  
[https://crickett20analytics.streamlit.app/](https://crickett20analytics.streamlit.app/)

**Dashboard Features:**
- **Overall Tournament Insights:**  
  See aggregate stats for all matches, including top run-scorers and wicket-takers.
- **Team vs Team Head-to-Head:**  
  Compare any two teams’ historical performance.
- **Detailed Player Analytics:**  
  Dive into individual batting & bowling stats.
- **Dynamic Filtering:**  
  Filter by team, player, or year to generate custom insights on the fly.
- **Responsive UI:**  
  Clean layout ready for desktop and mobile.

**Preview:**  
*(Replace this placeholder with a real dashboard screenshot for best impact)*

![Dashboard Screenshot](https://placehold.co/800x450/2d3748/ffffff?text=Your+Application+Screenshot)

---

## 🛠️ Technology Stack

- **Data Analysis:** Python, Pandas, NumPy, Jupyter Notebook
- **Data Visualization:** Plotly, Matplotlib, Seaborn
- **Web Application:** Streamlit
- **Deployment:** Streamlit Community Cloud

---

## ⚡ How To Run Locally

```sh
git clone https://github.com/r1afif18/cricket_t20_analytics.git
cd cricket_t20_analytics

# (Recommended) Create and activate a virtual environment
# Windows:
python -m venv venv
venv\Scripts\activate

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run dashboard.py

\\\



## 📑 Dataset

- Public T20 cricket match data  
- Sourced from [Codebasics Power BI Project](https://github.com/codebasics/py/tree/master/pandas/11_power_bi_projects)  
- CSVs included: match summaries, player info, batting and bowling stats

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Connect with Me

Developed by **Muhammad Rafif Sudanta**  
- [GitHub: @r1afif18](https://github.com/r1afif18)
- [LinkedIn: linkedin.com/in/rafif-sudanta](https://www.linkedin.com/in/rafif-sudanta/)

_Made with ❤️ for cricket fans and data enthusiasts worldwide!_


