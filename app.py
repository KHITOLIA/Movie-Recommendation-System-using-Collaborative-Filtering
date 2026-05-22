from flask import Flask, render_template, request
from difflib import get_close_matches
import pickle
import numpy as np

app = Flask(__name__)

pt = pickle.load(open('pt.pkl', 'rb'))
similarity_score = pickle.load(open('score.pkl', 'rb'))


def recommend(movie_name):
    if movie_name not in pt.index:
        matches = get_close_matches(movie_name, pt.index, n=5, cutoff=0.5)
        return matches  # return close matches (may be empty list)

    index = int(np.where(pt.index == movie_name)[0][0])
    similar = sorted(
        enumerate(similarity_score[index]),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    return [f"{i}. {pt.index[movie[0]]}" for i, movie in enumerate(similar, start=1)]


@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        movie_name = request.form['movie_name'].strip()
        result = recommend(movie_name)
        recommendations = result if result else []

    return render_template('index.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True)