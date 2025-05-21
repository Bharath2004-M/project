# utils.py
import requests

TMDB_API_KEY = 'YOUR_TMDB_API_KEY'  # Replace with your actual TMDB API key

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
