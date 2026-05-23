# Movie Recommendation System

A Movie Recommendation System built using **Collaborative Filtering** with **Cosine Similarity** on the MovieLens Latest Small Dataset.
This project recommends similar movies based on user rating patterns.

---

# Project Overview

This project uses an **Item-Based Collaborative Filtering** approach to recommend movies to users.

The recommendation system:

* analyzes user rating behavior
* finds similar movies using cosine similarity
* recommends movies based on similarity scores

The project also includes:

* Exploratory Data Analysis (EDA)
* Data preprocessing
* Flask web application
* Cold start handling
* Movie name suggestions for misspelled inputs

---

# Dataset

Dataset used:
[MovieLens Latest Small Dataset](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip?utm_source=chatgpt.com)

Dataset contains:

* movies metadata
* user ratings
* movie genres
* tags

Main files used:

* `movies.csv`
* `ratings.csv`

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* HTML/CSS
* Matplotlib

---

# Recommendation Technique

This project uses:

# Item-Based Collaborative Filtering

Workflow:

1. Create movie-user pivot table
2. Compute cosine similarity between movies
3. Recommend movies with highest similarity scores

---

# Features

* Movie recommendation system
* Similar movie suggestions
* Collaborative filtering
* Cosine similarity
* Flask web application
* EDA and visualizations
* Cold start handling
* Misspelled movie suggestions

---

# Data Preprocessing

To improve recommendation quality:

* considered users with minimum 100 ratings
* considered movies with minimum 20 ratings
* removed sparse/noisy interactions

This helps improve recommendation accuracy.

---

# Exploratory Data Analysis

Performed:

* rating distribution analysis
* most rated movies
* highest average rated movies
* active users analysis

---

# Project Structure

```bash
movie-recommendation-system/

│
├── app.py
├── requirements.txt
├── pt.pkl
├── similarity_score.pkl
├── README.md
│
├── data/
│   ├── movies.csv
│   └── ratings.csv
│
├── notebooks/
│   └── recommendation_system.ipynb
│
├── templates/
   └── index.html

```

---

# Installation

Clone repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```

Move into project directory:

```bash
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# Example Recommendation

Input:

```python
recommend("Toy Story (1995)")
```

Output:

```python
1. Bug's Life, A (1998)
2. Aladdin (1992)
3. Monsters, Inc. (2001)
4. Finding Nemo (2003)
5. Shrek (2001)
```

---

# Cold Start Problem

This recommendation system can only recommend movies already present in the dataset.

For unseen/new movies:

* similarity cannot be computed
* recommendations cannot be generated

This is known as the **Cold Start Problem** in recommendation systems.

To improve usability:

* movie existence validation added
* spelling suggestion support added

---

# Future Improvements

Possible improvements:

* Hybrid recommendation system
* Content-based filtering
* Deep learning recommendation models
* TMDb API integration for posters
* User authentication
* Real-time recommendations
---

# Author

Tushar : https://github.com/KHITOLIA
---

# License

This project is for educational and learning purposes.
