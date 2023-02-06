movies = [
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def high_score(movie):
    return movie["imdb"] > 5.5
        

print(high_score(movies[1]))