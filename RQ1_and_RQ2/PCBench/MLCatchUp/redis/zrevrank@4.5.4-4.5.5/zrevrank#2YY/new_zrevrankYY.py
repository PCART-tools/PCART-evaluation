from redis import Redis
client = Redis(host='localhost', port=6379, db=0)
result = client.zrevrank('my_sorted_set', value='element', withscore=False)
