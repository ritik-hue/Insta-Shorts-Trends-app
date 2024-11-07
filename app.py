import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import plotly.express as px

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(layout='wide')
jsonimg=load_lottieurl(r"https://lottie.host/09ec6681-782d-4195-b30e-ffd7b5d38c18/pZpcu7LN8v.json")

jsonimg2=load_lottieurl(r"https://lottie.host/e7c858a3-fc08-4e22-9101-df32226ff017/vqpic3aP3I.json")

st.sidebar.markdown(r"<div><img src='https://download.logo.wine/logo/Instagram/Instagram-Logo.wine.png' width=200 height 200 /><h1 style='display:inline-block'>Instagram Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown(r"This dashboard allows you to analyse trending 📈 Instagram Reels using Python and Streamlit.")
st.sidebar.markdown(r"To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)


hashtag = st.text_input('Search for a hashtag here', value="")
col1, col2 = st.columns(2)

# Add the first Lottie animation to the first column
with col1:
    st_lottie(jsonimg, height=300, width=200)

# Add the second Lottie animation to the second column
with col2:
    st_lottie(jsonimg2, height=300, width=200)


if st.button('Get Data'):

    # Load in existing data to test it out
    df = pd.read_csv(r"C:\Users\ADMIN\OneDrive\Documents\insta-reels\analytics.csv")

    if hashtag:  # Only filter if a hashtag is entered
        filtered_df = df[df['desc'].str.contains(hashtag, case=False, na=False)]
    else:
        filtered_df = df  # Use entire dataset if no hashtag is entered

    # Display filtered results
    st.write(f"Displaying results for hashtag: **{hashtag}**")
    st.write(filtered_df)

    # Plot histogram of filtered data
    fig = px.histogram(filtered_df, x='desc', hover_data=['desc'], y='stats_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)

    # Create two columns for additional charts
    left_col, right_col = st.columns(2)

    # First scatter plot for video stats
    scatter1 = px.scatter(
        filtered_df, 
        x='stats_shareCount', 
        y='stats_commentCount', 
        hover_data=['desc'], 
        size='stats_playCount', 
        color='stats_playCount'
    )
    left_col.plotly_chart(scatter1, use_container_width=True)

    # Second scatter plot for author stats
    scatter2 = px.scatter(
        filtered_df, 
        x='authorStats_videoCount', 
        y='authorStats_heartCount', 
        hover_data=['author_nickname'], 
        size='authorStats_followerCount', 
        color='authorStats_followerCount'
    )
    right_col.plotly_chart(scatter2, use_container_width=True)