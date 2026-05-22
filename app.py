from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load pickle files
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_score = pickle.load(open('score.pkl', 'rb'))


def recommend(movie_name):

    movie_name = movie_name.lower().strip()

    # partial movie matching
    matched_movies = [

        movie for movie in pt.index

        if movie_name in movie.lower()

    ]

    # if no movie found
    if len(matched_movies) == 0:

        return ["Movie not found in dataset"]

    # first matched movie
    selected_movie = matched_movies[0]

    # movie index
    index = np.where(
        pt.index == selected_movie
    )[0][0]

    # similarity scores
    similar = sorted(

        enumerate(similarity_score[index]),

        key=lambda x: x[1],

        reverse=True

    )[1:6]

    # recommendations
    recommendations = [

        pt.index[movie[0]]

        for movie in similar

    ]

    return recommendations


@app.route('/', methods=['GET', 'POST'])

def home():

    recommendations = []

    if request.method == 'POST':

        movie_name = request.form['movie_name']

        recommendations = recommend(movie_name)

    return render_template(

        'index.html',

        recommendations=recommendations

    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug =True)