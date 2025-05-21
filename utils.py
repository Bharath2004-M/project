import requests

API_KEY = '4e3ac53e6711051a3a2d9a519d3ad868'  

def fetch_poster(movie_title):
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        response = requests.get(search_url)
        data = response.json()
        
        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return "https://via.placeholder.com/500x750?text=No+Poster"
    
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750?text=Error"
