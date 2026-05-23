# Movie Recommendation System 🎬

This project is a hybrid movie recommendation system built using the MovieLens dataset. The main goal was to recommend similar movies by combining both collaborative filtering and content-based filtering approaches.

I built this project as part of an assignment for an Instructor role, and instead of using only one recommendation technique, I tried combining multiple approaches to improve the quality of recommendations.

Live Demo:
[Movie Recommendation Web App](https://recommendation-system.up.railway.app/?utm_source=chatgpt.com)

---

# About the Project

The recommendation system works in three stages:

* Collaborative Filtering
  Recommends movies based on user rating behavior.

* Content-Based Filtering
  Recommends movies using genres and movie tags.

* Hybrid Recommendation Pipeline
  Combines recommendations from both approaches and ranks them based on similarity scores.

The application also supports partial movie name search, so users do not need to type the exact movie title.

---

# Dataset Used

Dataset: [MovieLens Small Dataset](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip?utm_source=chatgpt.com)

Kaggle Version:
[MovieLens Dataset on Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-latest-small?utm_source=chatgpt.com)

Files used from the dataset:

* movies.csv
* ratings.csv
* tags.csv

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Matplotlib
* Pickle

---

# Project Workflow

## 1. Data Preprocessing

* Merged movies, ratings, and tags datasets
* Cleaned missing values
* Combined genres and tags for content-based filtering
* Removed duplicate movie entries

---

## 2. Collaborative Filtering

For collaborative filtering:

* Created a movie-user pivot table
* Filtered active users and popular movies
* Used cosine similarity to find similar movies

This approach recommends movies based on how users rate similar movies.

---

## 3. Content-Based Filtering

For content-based filtering:

* Combined genres and tags into a single text feature
* Applied TF-IDF vectorization
* Calculated cosine similarity between movies

This approach recommends movies with similar metadata and tags.

---

## 4. Hybrid Recommendation System

The final recommendation pipeline:

* fetches top recommendations from collaborative filtering
* fetches top recommendations from content-based filtering
* combines both results
* removes duplicate movies
* sorts movies based on similarity scores
* returns final recommendations

This helped improve recommendation quality compared to using a single approach alone.

---

# Features

* Hybrid recommendation system
* Partial movie search support
* Collaborative filtering
* Content-based filtering
* Flask web application
* Railway deployment

---

# Folder Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── notebook/
│   └── recommendation_system.ipynb
│
├── pt.pkl
├── collaborative_similarity.pkl
├── content_similarity.pkl
└── movie_data.pkl
```

---

# How to Run the Project

## Clone the Repository

```bash
git clone https://github.com/KHITOLIA/Movie-Recommendation-System-using-Collaborative-Filtering.git
```

```bash
cd Movie-Recommendation-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Flask Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

# Example

### Input

```text
Wolverine
```

### Recommendations

```text
Avengers: Infinity War - Part I (2018)
Punisher, The (2004)
Dick Tracy (1990)
Thor (2011)
Incredible Hulk, The (2008)
```

---

# Deployment

The application is deployed on Railway.

Live Application:
[Recommendation System Live Demo](https://recommendation-system.up.railway.app)

---

# Future Improvements

Some improvements that can be added later:

* movie posters using TMDB API
* user-based personalized recommendations
* user login system
* matrix factorization techniques
* deep learning recommendation models

---

# What I Learned

Through this project, one can have a hands-on experience with:

* recommendation systems
* collaborative filtering
* content-based filtering
* hybrid recommendation pipelines
* cosine similarity
* TF-IDF vectorization
* Flask deployment
* Railway deployment

---

# Author

Tushar

GitHub: [GitHub](https://github.com/KHITOLIA)
