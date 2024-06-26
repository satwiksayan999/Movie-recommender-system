import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_title):
    response = requests.get("http://www.omdbapi.com/?t={}&apikey=572394a8".format(movie_title))
    data=response.json()
    return data['Poster']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movie_list:
        #movie_id=i[0]
        #fetch poster using id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].title))

    return recommended_movies,recommended_movies_posters



movies_dict=pickle.load(open('movies_dict.pkl' , 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')


option = st.selectbox(
'Which movie do you like best?',
movies['title'].values)

if st.button('Select'):
    names, posters= recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])