import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")

# Convert genres into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

# Calculate similarity
similarity = cosine_similarity(matrix)

print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

movie_name = input("Enter a movie name: ")

if movie_name in df["title"].values:

    index = df[df["title"] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))

    sorted_scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:\n")

    count = 0

    for movie in sorted_scores[1:]:
        print(df.iloc[movie[0]].title)
        count += 1

        if count == 5:
            break

else:
    print("Movie not found in database.")