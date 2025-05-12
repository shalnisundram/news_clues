from flask import Flask, jsonify
import redis
import json
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

API_HITS = Counter('news_api_hits_total', 'Total API hits')
API_ERRORS = Counter('news_api_errors_total', 'Total API errors')

@app.route('/news')
def get_news():
    API_HITS.inc()
    try:
        articles = r.lrange("news", 0, 9)  # get 10 most recent
        parsed = [json.loads(a.replace("'", '"')) for a in articles]
        return jsonify(parsed)
    except Exception as e:
        API_ERRORS.inc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus metrics on :8000/metrics
    app.run(host='0.0.0.0', port=8000)