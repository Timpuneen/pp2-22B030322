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

def filter (movies, category):
    result = []
    for film in movies:
        if film["category"] == category:
            result.append(film)
    return result

print(filter(movies, "Romance"))