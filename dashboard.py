import streamlit as st
import pandas as pd
import plotly.express as px
import re

st.set_page_config(page_title="T20 Cricket Analytics", layout="wide")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df_match = pd.read_csv('data/dim_match_summary.csv')
    df_players = pd.read_csv('data/dim_players.csv')
    df_batting = pd.read_csv('data/fact_bating_summary.csv')
    df_bowling = pd.read_csv('data/fact_bowling_summary.csv')
    return df_match, df_players, df_batting, df_bowling

df_match, df_players, df_batting, df_bowling = load_data()

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/190/190411.png", width=80)
st.sidebar.title("T20 Cricket Dashboard")
selected_team = st.sidebar.selectbox(
    "Select Team (All for all teams)",
    options=["All"] + sorted(df_players["team"].dropna().unique().tolist()),
)
st.sidebar.markdown("---")
st.sidebar.info(
    "Dataset: Codebasics T20 Cricket\n\n"
    "Dashboard developed as a data analytics portfolio project by Rafif Sudanta.\n"
    "[LinkedIn](https://www.linkedin.com/in/rafif-sudanta/) | [GitHub](https://github.com/r1afif18)"
)

# --- FILTER BY TEAM ---
if selected_team != "All":
    batting_filtered = df_batting[df_batting["teamInnings"] == selected_team]
    bowling_filtered = df_bowling[df_bowling["bowlingTeam"] == selected_team]
else:
    batting_filtered = df_batting
    bowling_filtered = df_bowling

# --- TABS ---
tab_about, tab1, tab2, tab3, tab4 = st.tabs(
    ["ℹ️ About", "🏏 Top Batsman", "🎯 Top Bowler", "🏆 Winning Teams", "💡 Insights"]
)

with tab_about:
    st.title("T20 Cricket Analytics Dashboard")
    st.markdown("""
#### Project Description
This dashboard was built to analyze team and player performance in International T20 Cricket tournaments.
The dataset is sourced from the [CodeBasic.io](https://codebasics.io/resources/data-analytics-project-for-beginners) and processed using Python & Streamlit.

#### Dataset Structure
- **dim_match_summary.csv**: Match info (teams, winner, margin, venue, date)
- **dim_players.csv**: Player profiles (name, team, batting/bowling style, role)
- **fact_bating_summary.csv**: Player batting statistics per match
- **fact_bowling_summary.csv**: Player bowling statistics per match

#### Dashboard Features
- Explore top batsmen & bowlers (with team filter)
- See the most successful teams
- Auto-generated insights
- Interactive & responsive UI

#### Credits
Dataset by Codebasics, dashboard developed as a data analytics portfolio project by **Rafif Sudanta**.
[LinkedIn](https://www.linkedin.com/in/rafif-sudanta/) | [GitHub](https://github.com/r1afif18)
    """)
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRBh8Xi_j9QGlyOQFMxXVxJ66bWcRK1bMgpQ&s",
        width=280,
        caption="T20 Cricket Match"
    )

with tab1:
    st.subheader("Top 10 Run Scorers")
    top_bat = (
        batting_filtered.groupby("batsmanName")["runs"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    ).reset_index()
    fig_bat = px.bar(
        top_bat,
        x="batsmanName",
        y="runs",
        title="Top 10 Batsmen (Total Runs)",
        labels={"batsmanName": "Batsman", "runs": "Total Runs"},
        text_auto=True
    )
    st.plotly_chart(fig_bat, use_container_width=True)
    st.dataframe(top_bat, hide_index=True)

with tab2:
    st.subheader("Top 10 Bowlers by Wickets")
    top_bowler = (
        bowling_filtered.groupby("bowlerName")["wickets"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    ).reset_index()
    fig_bowler = px.bar(
        top_bowler,
        x="bowlerName",
        y="wickets",
        title="Top 10 Bowlers (Wickets)",
        labels={"bowlerName": "Bowler", "wickets": "Total Wickets"},
        text_auto=True
    )
    st.plotly_chart(fig_bowler, use_container_width=True)
    st.dataframe(top_bowler, hide_index=True)

with tab3:
    st.subheader("Top 10 Winning Teams")
    win_counts = df_match["winner"].value_counts().head(10).reset_index()
    win_counts.columns = ["Team", "Wins"]
    fig_team = px.bar(
        win_counts,
        x="Team",
        y="Wins",
        title="Top 10 Winning Teams",
        labels={"Team": "Team", "Wins": "Number of Wins"},
        text_auto=True
    )
    st.plotly_chart(fig_team, use_container_width=True)
    st.dataframe(win_counts, hide_index=True)

with tab4:
    st.subheader("💡 Auto Insights")
    # Top Scorer
    best_bat = top_bat.iloc[0]
    st.success(f"**Top Scorer:** {best_bat['batsmanName']} with {best_bat['runs']} runs.")
    # Top Bowler
    best_bowler = top_bowler.iloc[0]
    st.success(f"**Top Bowler:** {best_bowler['bowlerName']} with {best_bowler['wickets']} wickets.")
    # Top Winning Team
    best_team = win_counts.iloc[0]
    st.info(f"**Team with most wins:** {best_team['Team']} ({best_team['Wins']} wins).")
    # Biggest win margin (robust)
    st.subheader("Biggest Winning Margin")
    df_match_margin = df_match.copy()
    df_match_margin['margin_num'] = df_match_margin['margin'].astype(str).apply(
        lambda x: int(re.search(r'(\d+)', x).group()) if re.search(r'(\d+)', x) else 0
    )
    idx_max = df_match_margin['margin_num'].idxmax()
    row_max = df_match_margin.loc[idx_max]
    if row_max['winner'] == row_max['team1']:
        opponent = row_max['team2']
    else:
        opponent = row_max['team1']
    st.write(
        f"{row_max['winner']} defeated {opponent} "
        f"by {row_max['margin']} at {row_max['ground']} ({row_max['matchDate']})."
    )

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:grey'>"
    "Dashboard built with  using Streamlit & Plotly • Dataset by Codebasics"
    "</div>",
    unsafe_allow_html=True,
)
