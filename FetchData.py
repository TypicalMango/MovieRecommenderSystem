import tmdbsimple as tmdb
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
tmdb.API_KEY = '01f1b62444c170838b3fffa722cf2aa3'
"""
search = tmdb.Search()

response1 = search.company(query='Sony Pictures')
print("------------------------------------------------------------------")
print(response1['results'][0:2])
print("------------------------------------------------------------------")
"""

discover = tmdb.Discover()
response2 = discover.movie(year=2023)
for value in response2['results']:
    print(value['title'])
print(len(response2['results']))
