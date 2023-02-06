movies = [
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "Exam2",
"imdb": 6.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def filter (movies, category):
    result = 0
    divisor = 0
    for film in movies:
        if film["category"] == category:
            result += film["imdb"]
            divisor += 1
    return result/divisor


print(filter(movies, "Thriller"))