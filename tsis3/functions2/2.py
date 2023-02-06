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

def top_kinch(movies):
    result = []
    for film in movies:
        if film["imdb"] > 5.5:
            result.append(film)
    return result


print(top_kinch(movies))