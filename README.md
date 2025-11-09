# Real-Time Bitcoin Price Streaming Pipeline

A real-time data streaming pipeline that fetches Bitcoin price data from an [external API](https://freecryptoapi.com/), streams it via Redpanda, processes it with Apache Flink, and stores it in PostgreSQL — all containerized using Docker Compose.

## Project Overview

This project demonstrates a complete end-to-end data engineering workflow:

- Fetching real-time cryptocurrency data (Bitcoin) from a public API
- Streaming and buffering the data via Redpanda (Kafka-compatible)
- Processing the data stream with Apache Flink
- Persisting results into PostgreSQL for analysis
- Running everything with Docker Compose

## How it works
+ The crypto_api.py file fetches Bitcoin data from
```bash
https://api.freecryptoapi.com/v1/getData?symbol=BTC
```
+ Data is sent to Redpanda via the Python confluent_kafka library.
+ Flink listens to the Redpanda topic, processes and filters data.
+ PostgreSQL stores the structured and cleaned data.

## Project Structure

```kotlin
data-streaming-pipeline/
├── api/
│   └── crypto_api.py
├── redpanda/
│   └── producer.py
├── Dockerfile
├── docker-compose.yaml
└── README.md
```


## Installation
Prerequisites :
- Docker and Docker Compose installed
- Python 3.12+ (for development or testing locally)

## Setup and Run
```bash
# Clone the repository
git clone https://github.com/your-username/data-streaming-pipeline.git
cd data-streaming-pipeline

# Build and run the entire stack
docker compose up --build
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author
Trody — Data Engineer & Developer

## License

[MIT](https://choosealicense.com/licenses/mit/)