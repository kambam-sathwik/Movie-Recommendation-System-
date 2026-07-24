import streamlit as st
import pickle
import joblib

st.title("Movie recommendation system")

with open("movies.pickle","rb") as f1:
    movies=pickle.load(f1)

similarity=joblib.load("similarities.joblib")

movie_names=movies['title'].values

movie_name=st.selectbox("Enter the movie name",movie_names)



def recommend(movie_name):
 
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommend_movies=[]
    for i, movie in enumerate(movies_list, start=1):
        recommend_movies.append(movies.iloc[movie[0]]['title'])
    return recommend_movies

if st.button("Recommend"):
    r=recommend(movie_name)
    st.write("The top relatable movies are")

    for i in r:
        st.write(i)