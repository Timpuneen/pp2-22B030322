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

def filter (movies):
    result = 0
    for film in movies:
        result += film["imdb"]
    return result/len(movies)

print(filter(movies))