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

## Features

- Upload property listing text and photos
- AI-powered text analysis for risk detection
- Image analysis for property condition assessment
- Cap rate calculation and financial metrics
- Voice-interactive recommendations
- Downloadable analysis reports

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

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to the provided local URL
3. Paste property listing text and upload photos
4. Click "Analyze Deal" to start the analysis
5. Use the "Ask DealSense" button for voice recommendations
6. Download the analysis report if needed

## API Integration

This application uses:
- VAPI for voice interaction
- Gumloop AI for text and image analysis

## Development

The application is built with:
- Streamlit for the frontend
- Python for backend processing
- Various AI APIs for analysis

### Temporal
```sh
 # start server
 temporal server start-dev --db-filename mytemporal.db
 # start worker
 python run_worker.py
 #start workflow
 python run_workflow.py
```
