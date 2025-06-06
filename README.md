# FIAP-2025-MLET-FASE4: Stock Price Prediction with LSTM

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)

A machine learning project that uses LSTM (Long Short-Term Memory) neural networks to predict stock prices. The project includes data collection, model training, and a production-ready API for making predictions.

## 🎯 Project Overview

This project demonstrates the complete lifecycle of a machine learning application, from data collection to production deployment. It focuses on predicting Tesla (TSLA) stock prices using historical data and deep learning techniques.

### Key Features

- 📊 Historical stock data collection using yfinance
- 🧮 Data preprocessing and feature engineering
- 🤖 LSTM model for time series prediction
- 🚀 REST API for real-time predictions
- 📈 Performance monitoring and metrics
- 🐳 Containerized deployment
- 📝 Structured logging with request tracking
- 🔍 Prometheus metrics integration

## 🏗️ Project Structure

```
FIAP-2025-MLET-FASE4/
├── notebooks/
│   ├── Data_Collection_and_Preparation.ipynb    # Data collection and preprocessing
│   └── Model_Training_and_Evaluation.ipynb      # Model training and evaluation
├── stock_prediction_api/                        # API implementation
│   ├── api/
│   │   ├── models/                             # Pydantic models
│   │   ├── services/                           # Business logic
│   │   ├── middleware/                         # Request logging and metrics
│   │   └── routes/                             # API endpoints and metrics
│   ├── tests/
│   │   ├── unit/                              # Unit tests
│   │   └── integration/                        # Integration tests
│   ├── Dockerfile                              # Container definition
│   └── requirements.txt                        # API dependencies
├── models/                                     # Saved models directory
│   ├── tesla_lstm_model.keras                 # Trained LSTM model
│   └── scaler.joblib                          # Fitted data scaler
├── data/                                      # Dataset storage
└── tasks/                                     # Project documentation
    ├── data_preparation_tasks.md              # Data preparation steps
    ├── model_development_tasks.md             # Model development guide
    └── api_development_tasks.md               # API implementation tasks
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker 20.10+
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/FIAP-2025-MLET-FASE4.git
cd FIAP-2025-MLET-FASE4
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📚 Usage

### Data Collection and Model Training

1. Run the data collection notebook:
```bash
jupyter notebook notebooks/Data_Collection_and_Preparation.ipynb
```

2. Train the LSTM model:
```bash
jupyter notebook notebooks/Model_Training_and_Evaluation.ipynb
```

### Running the API

#### Local Development

```bash
cd stock_prediction_api
uvicorn api.main:app --reload
```

#### Using Docker

```bash
docker-compose up --build
```

### Making Predictions

```python
import requests

data = {
    "sequence": [
        {
            "open": 150.0,
            "high": 155.0,
            "low": 149.0,
            "close": 153.0,
            "volume": 1000000.0
        }
        # ... 60 days of data
    ]
}

response = requests.post("http://localhost:8000/predict", json=data)
prediction = response.json()
print(f"Predicted close: ${prediction['predicted_close']:.2f}")
```

## 📊 Model Performance

- Training Loss: 0.0013
- Validation Loss: 0.0032
- Mean Absolute Error (MAE): Varies by market conditions
- Root Mean Squared Error (RMSE): Varies by market conditions

## 🔍 API Endpoints

- `POST /predict`: Make stock price predictions
- `GET /health`: API health check
- `GET /metrics`: Prometheus metrics

## 📈 Monitoring

The API includes comprehensive monitoring features:

### Request Tracking
- JSON formatted logs with request IDs
- Response time tracking
- Error logging and categorization

### Metrics
- Total requests by endpoint
- Request latency histograms
- Prediction success/failure counts
- Model inference time

### Health Checks
- API availability monitoring
- Model loading status
- Dependencies health status

## 🚢 Deployment

For detailed deployment instructions, see [DEPLOY.md](DEPLOY.md).

Supported platforms:
- Railway
- Render
- Any platform supporting Docker

## 👥 Team

* [Ricardo Matos RM359670](https://www.linkedin.com/in/ricardo-matos-mobile-dev/)
* [José Diôgo RM359671](https://www.linkedin.com/in/jozediogo/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 References

- [LSTM Neural Networks](https://www.tensorflow.org/tutorials/structured_data/time_series)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Stock Market Data Analysis](https://www.investopedia.com/terms/t/technical-analysis-of-stocks-and-trends.asp)
- [Prometheus Monitoring](https://prometheus.io/docs/introduction/overview/) 