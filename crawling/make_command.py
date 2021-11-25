

location = 'cd Desktop/tmdb_test\n'
base = 'start /b python get_movies.py --start'

numli = [10000 + 30000 * i for i in range(5)]
ans = ''
for num in numli:
    ans += base + f' {num}\n'
location += ans
print(location)
