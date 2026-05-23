from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load pickle files
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_score = pickle.load(open('score.pkl', 'rb'))
movie_data = pickle.load(open('movie_data.pkl', 'rb'))
content_similarity = pickle.load(open('content_score.pkl', 'rb'))

def content_recommend(movie_name):
    movie_name = movie_name.lower().strip()

    matched_movies = [movie for movie in movie_data['title'] if movie_name in movie.lower()]

    # if no movie found
    if len(matched_movies) == 0:

        return ["Movie not found in dataset"]

    selected_movie = matched_movies[0]
    idx = movie_data[movie_data['title'] == selected_movie].index[0]

    similar_movies = sorted(enumerate(content_similarity[idx]), key = lambda x: x[1], reverse = True)[1:11]

    recommendations = [ (movie_data['title'].iloc[i[0]], i[1])
        for i in similar_movies]
    return recommendations



def collaborative_recommend(movie_name):

    movie_name = movie_name.lower().strip()

    # partial movie matching
    matched_movies = [movie for movie in pt.index if movie_name in movie.lower()]

    # if no movie found
    if len(matched_movies) == 0:

        return ["Movie not found in dataset"]

    # first matched movie
    selected_movie = matched_movies[0]

    # movie index
    index = np.where(pt.index == selected_movie)[0][0]

    # similarity scores
    similar = sorted(enumerate(similarity_score[index]),key=lambda x: x[1],reverse=True)[1:11]

    # recommendations
    recommendations = [(pt.index[movie[0]], movie[1]) for movie in similar]

    return recommendations



def recommendation_pipeline(movie_name):
    content_movies = content_recommend(movie_name)
    collaborative_movies = collaborative_recommend(movie_name)
    all_movies = list(content_movies + collaborative_movies)
    # remove duplicates using dictionary
    unique_movies = {}

    for movie, score in all_movies:

        # keep highest score
        if movie not in unique_movies:

            unique_movies[movie] = score

        else:

            unique_movies[movie] = max(
                unique_movies[movie],
                score
            )
    

    top_movies = sorted(list(unique_movies.items()), key = lambda x: x[1], reverse = True)[:5]
    recommendations = []
    for movie in top_movies:
        recommendations.append(movie[0])
    return recommendations




@app.route('/', methods=['GET', 'POST'])

def home():

    recommendations = []

    if request.method == 'POST':

        movie_name = request.form['movie_name']

        recommendations = recommendation_pipeline(movie_name)

    return render_template(

        'index.html',

        recommendations=recommendations

    )


if __name__ == '__main__':

    app.run(debug=True)