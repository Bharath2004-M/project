# app.py

import streamlit as st
from recommender import recommend
from utils import fetch_poster

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 AI-Powered Movie Recommendation System")

st.markdown(
    "Enter the name of a movie you like, and get recommendations based on its content."
)

# Input box for movie name
movie_name = st.text_input("Enter a movie name:")

# When the Recommend button is clicked
if st.button("Recommend"):
    if movie_name:
        try:
            titles, posters = recommend(movie_name)
            st.subheader("Recommended Movies")
            cols = st.columns(5)
            for i in range(len(titles)):
                with cols[i % 5]:
                    st.image(posters[i], use_container_width=True)
                    st.caption(titles[i])
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a movie name.")
