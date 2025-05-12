# Breaking News Fetcher

A system fetching breaking news by category and country, displaying hot topics and geographic areas of interest. Portable app via Docker, Kubernetes, etc.

### Setup
```
python -m venv newsevn

# Activate venv then install requirements
source venv/bin/activate && python -m pip install -r requirements.txt

# Get Redis via helm
brew install helm
helm install redis bitnami/redis
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo udpate
```


### Run !
```
python3 news_fetcher/app.py  
```
See news articles in Redis db. To view Redis pod, get name from checking pods list 
```
kubectl get pods -n default
```
See the events in pod:
```
kubectl exec -it [redis_master_node_name] -n default -- redis-cli -a $REDIS_PASSWORD
```
Query by country and cateogory:
```
SMEMBERS country:[country name]
SMEMBERS category:[cateogry name]
```

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```
4. Edit `.env` with your API keys for VAPI and Gumloop

## Usage

1. Open redis default port 6379
  ```bash
   kubectl port-forward [redis master node name] 6379:6379 -n [pod namespace name]
   ```
2. Start the Streamlit app:
   ```bash
   python3 news_fetcher/app.py
   ```
3. Exec into kubernetes redis pod
   ```bash
     kubectl exec -it [redis_master_node_name] -n default -- redis-cli -a $REDIS_PASSWORD
   ```
3. Query Redis db to find articles
    ```bash
     SMEMBERS country:[country name]
     SMEMBERS category:[cateogry name]
   ```

## API Integration

This application uses:
- News Data API to fetch breaking news https://newsdata.io/

## Development

The application is built with:
- Python for backend processing
- Various AI APIs for analysis
- Kubernetes for portability and monitoring
- Redis for slick distributed databasing 

