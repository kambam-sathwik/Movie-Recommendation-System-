import streamlit as st
import pickle
import joblib
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommendation System")

# Load files
with open("movies.pickle", "rb") as f:
    movies = pickle.load(f)

tfidf = joblib.load("tfidf.joblib")
tfidf_matrix = joblib.load("tfidf_matrix.joblib")

movie_names = movies['title'].values

movie_name = st.selectbox("Enter the movie name", movie_names)


def recommend(movie_name, top_n=5):

    # Find movie index
    movie_index = movies[movies['title'] == movie_name].index[0]

    # Compute cosine similarity ONLY for selected movie
    similarity_scores = cosine_similarity(
        tfidf_matrix[movie_index],
        tfidf_matrix
    ).flatten()

    # Sort similarity scores
    movie_list = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    recommendations = []

    for movie in movie_list:
        recommendations.append(
            movies.iloc[movie[0]]['title']
        )

    return recommendations


if st.button("Recommend"):

    recommendations = recommend(movie_name)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)