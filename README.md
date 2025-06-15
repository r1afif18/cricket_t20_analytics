T20 Cricket Analytics: From EDA to Interactive Dashboard
This repository documents the end-to-end process of a T20 cricket data analysis project. It showcases a complete data science workflow, beginning with in-depth Exploratory Data Analysis (EDA) in a Jupyter Notebook and culminating in a user-friendly, interactive Streamlit Web Application.

Project Structure: Analysis & Application
This project is built on two core components, demonstrating both analytical depth and the ability to deliver actionable insights.

1. The Analysis 🔬 (main.ipynb)
The foundation of this project is a comprehensive Exploratory Data Analysis performed in the main.ipynb Jupyter Notebook. This document details the entire investigation process.

Key objectives of the analysis included:

Data Cleaning & Preprocessing: Handling missing values, correcting data types, and structuring the raw data for analysis.

Feature Engineering: Creating new, meaningful features from existing data to uncover deeper insights.

Insight Discovery: Answering key questions about team and player performance, such as:

Identifying the most successful teams and players.

Analyzing head-to-head match-ups and historical performance.

Understanding factors that contribute to winning matches.

2. The Interactive Dashboard 📊 (app.py)
The insights from the analysis are brought to life in an interactive web application built with Streamlit. The dashboard's purpose is to make the complex data accessible and explorable for any user, regardless of their technical background.

Live Application: https://crickett20analytics.streamlit.app/

Dashboard Capabilities:

Overall Tournament Insights: Explore high-level statistics, including top run-scorers and wicket-takers across all matches.

Team vs. Team Head-to-Head: Select any two teams to see a detailed comparison of their historical performance against each other.

Detailed Player Analytics: Dive into the career statistics of individual players to analyze their batting and bowling performance over time.

Dynamic Filtering: Interactively filter the data by team, player, or year to generate custom visualizations and insights on the fly.

📸 Application Preview
Here is a glimpse of the dashboard's interface.

![Image of the Cricket T20 Analytics Dashboard]([https://placehold.co/800x450/2d3748/ffffff?text=Your+Application+Screenshot](https://github.com/user-attachments/assets/6f4bf83a-a42b-4e21-9909-d7b07b9dd106))

(Recommendation: Replace this placeholder with an actual screenshot of your application for maximum impact.)

🛠️ Technology Stack
Data Analysis: Python, Pandas, NumPy, Jupyter Notebook

Data Visualization: Plotly, Matplotlib, Seaborn

Web Application: Streamlit

Deployment: Streamlit Community Cloud

🚀 How to Run Locally
To run this project on your local machine, follow these steps:

Clone the Repository

git clone https://github.com/r1afif18/cricket_t20_analytics.git
cd cricket_t20_analytics

Set Up a Virtual Environment (Recommended)

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies
Ensure you have a requirements.txt file in your repository.

pip install -r requirements.txt

Run the Streamlit Application

streamlit run app.py

The application will open in your web browser at http://localhost:8501.

📄 License
This project is licensed under the MIT License.

👤 Connect with Me
Muhammad Rafif Sudanta

GitHub: [@r1afif18
](https://github.com/r1afif18)
LinkedIn: [linkedin.com/in/muhammad-afif-rusyadi](https://www.linkedin.com/in/rafif-sudanta/)
