# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import fetch_poster

# Load data
movies = pd.read_csv('movies.csv')
movies['combined'] = movies['genres'] + ' ' + movies['overview']
movies = movies.dropna(subset=['combined'])

# TF-IDF + Cosine Similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(title):
    idx = movies[movies['title'].str.lower() == title.lower()].index
    if idx.empty:
        raise ValueError("Movie not found.")
    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    
    titles = movies['title'].iloc[movie_indices].tolist()
    posters = [fetch_poster(movies['id'].iloc[i]) for i in movie_indices]
    return titles, posters
