"""
Fetches data from NewsData.io API and publishes to Redis.

 The API rate limit of free users is 30 credits per 15 minutes 
 which means the free user can request up to 300 articles per 
 15 minutes.
"""
import time, requests, os, redis
from prometheus_client import start_http_server, Summary, Counter
import dateutil.parser

API_KEY = "pub_85972c96728467d85a5ea79e130719b6cc1b1"
print(f"api key set")
FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 120)) # 1req/2mins = 7.5/15 mins
TOPIC = "technology"
r = redis.Redis(
    host='localhost',  # or redis-master-0
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
    db=0
)
r.ping()

REQUEST_TIME = Summary('news_fetch_latency_seconds', 'Time spent fetching news')
FETCH_ERRORS = Counter('news_fetch_errors_total', 'Total fetch errors')

@REQUEST_TIME.time()
def fetch_news():
    resp = None
    
    try:
        print(f"starting news fetch")
        resp = requests.get(f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={TOPIC}&language=en")
        articles = resp.json().get("results", [])
        print(f"results at {r}")
        
        for article in articles:
            article_id = article['article_id'] 
            article_key = f"article:{article_id}"
            
            article_category = article.get("category", [""])[0]
            article_country = article.get("country", [""])[0]

            print(f"Article Country: {article_country}")
            
            r.hset(article_key, mapping={
                "title": article.get("title", ""),
                "pubDate": article.get("pubDate", ""),
                "category": article_category,
                "country": article_country
            })
            
            # Add articles to set group by category for heatmap purposes
            article_category_dashed = article_country.replace(" ", "_")  # Replacing spaces with underscores
            article_country_dashed = article_country.replace(" ", "_")  # Replacing spaces with underscores

            r.sadd(f"category:{article_category_dashed}", article_key)
            r.sadd(f"country:{article_country_dashed}", article_key)
            
            timestamp = dateutil.parser.parse(article["pubDate"]).timestamp()
            r.zadd("news:by_time", {f"article:{article_id}": timestamp})
            
            print(f"pushing new")
            r.lpush("news", str(article))
        
    except Exception as e:
        # FETCH_ERRORS.inc()
        print("Status code:", resp.status_code)
        # print("Response body:", resp.text)
        # print("Error fetching news:", e)

if __name__ == '__main__':
    start_http_server(8001)
    while True:
        fetch_news()
        time.sleep(FETCH_INTERVAL)