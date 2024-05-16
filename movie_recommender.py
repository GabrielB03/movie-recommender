import pandas as pd
from tkinter import * # type: ignore

# Load data from CSV files using Pandas
movies_df = pd.read_csv('C:/Users/Samsung/Desktop/Gabriel/Projetos para Portfólio/Python/Sistema de Recomendação de Filmes e Livros/csv/movies.csv')

# Function to recommend movies for a user
def recommend_movies(user_id):
    recommended_movies = []
    # Iterate over each movieId and title in the movies DataFrame
    for movie_id, title in zip(movies_df['movieId'], movies_df['title']):
        recommended_movies.append(f"Movie ID: {movie_id}, Title: {title}")
    return recommended_movies

# Interface
def show_recommendation():
    user_id = int(entry.get())
    recommended_movie_titles = recommend_movies(user_id)
    # Clear previous recommendations
    result_text.delete(1.0, END)
    # Show recommended movie titles in the Text widget
    for title in recommended_movie_titles:
        result_text.insert(END, title + '\n')

root = Tk()
root.title("Movie Recommendation")

frame = Frame(root)
frame.pack(pady=20)

label = Label(frame, text="Enter User ID:")
label.grid(row=0, column=0)

entry = Entry(frame, width=30)
entry.grid(row=0, column=1)

button = Button(frame, text="Recommend", command=show_recommendation)
button.grid(row=1, columnspan=2, pady=10)

result_text = Text(root, wrap=WORD, width=50, height=10)
result_text.pack(pady=20)

root.mainloop()
