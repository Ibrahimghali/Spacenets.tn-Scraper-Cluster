import redis
import sys

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379)

# List of start URLs
urls = [
    'https://spacenet.tn/18-ordinateur-portable',
    'https://spacenet.tn/145-serveurs-cloud-informatique-tunisie',
    'https://spacenet.tn/8-imprimante-tunisie',
    'https://spacenet.tn/132-meuble-de-bureau'
]

# Push URLs to Redis list
for url in urls:
    r.lpush('spacenets:start_urls', url)

print(f"Added {len(urls)} URLs to Redis queue")