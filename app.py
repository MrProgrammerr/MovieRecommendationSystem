import streamlit as st
import numpy as np
import pickle
import requests
# https://api.themoviedb.org/3/movie/65?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US
def fetch_poster(movie_id):
    res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = res.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie) :
    recommended = []
    posters = []
    movie_index = movie_names.index(movie)
    similiar = np.argsort(-similiarity[movie_index])[:11]
    for i in similiar[1:]:
        recommended.append(movie_names[i])
        posters.append(fetch_poster(i))
    return recommended,posters

st.title("Welcome to Movie Recommendation System")
with open('movies.pkl','rb') as f:
    movie_names = pickle.load(f)
with open('similiarity.pkl','rb') as f:
    similiarity = np.array(pickle.load(f))

selected_movie = st.selectbox(label="Choose Movie Name :",options=movie_names)

if st.button("Recommend") :
    # recommended_movies,posters = recommend(selected_movie)
    # for i in recommended_movies:
    #     st.write(f"Movie : {i}")
    # for i in posters:
    #     st.write(i)
    st.write(fetch_poster(0))
