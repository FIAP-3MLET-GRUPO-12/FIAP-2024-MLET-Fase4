# Stock Price Prediction API

A FastAPI-based REST API for serving LSTM model predictions for stock prices.

## 🏗️ Architecture

```
api/
├── models/              # Pydantic models for request/response
├── services/           # Business logic and model handling
├── middleware/         # Request logging and metrics
├── routes/            # API endpoints
└── main.py            # FastAPI application
```

## 🚀 Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
uvicorn api.main:app --reload
```

### Docker

```bash
docker-compose up --build
```

## 🔍 API Endpoints

### POST /predict

Make a prediction for the next day's closing price.

**Request:**
```json
{
    "sequence": [
        {
            "open": 150.0,
            "high": 155.0,
            "low": 149.0,
            "close": 153.0,
            "volume": 1000000.0
        }
    ]
}
```

**Response:**
```json
{
    "predicted_close": 155.50,
    "confidence_interval": {
        "lower": 153.25,
        "upper": 157.75
    }
}
```

### GET /health

Check API health status.

**Response:**
```json
{
    "status": "healthy",
    "timestamp": "2023-11-22T10:00:00.000Z"
}
```

### GET /metrics

Prometheus metrics endpoint.

## 📊 Monitoring

### Metrics Available

- `api_requests_total`: Total number of API requests
- `api_request_latency_seconds`: Request latency histogram
- `model_predictions_total`: Total predictions made

### Logging

- JSON formatted logs
- Request ID tracking
- Response time monitoring
- Error tracking

## 🔒 Security

- Input validation with Pydantic
- CORS configuration
- Rate limiting (configurable)
- Non-root Docker user

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

## 🚢 Configuration

Environment variables:
- `PORT`: API port (default: 8000)
- `ENVIRONMENT`: deployment environment
- `MODEL_PATH`: path to LSTM model
- `SCALER_PATH`: path to data scaler

## 📚 Documentation

- API documentation: `http://localhost:8000/docs`
- OpenAPI spec: `http://localhost:8000/openapi.json`

## 🔧 Development

1. Create a new branch
2. Make your changes
3. Add tests
4. Create a PR

For more details about deployment options and monitoring, see the main project [README.md](../README.md).

## Estrutura do Projeto

```
stock_prediction_api/
├── api/
│   ├── models/
│   │   └── stock_data.py      # Modelos Pydantic para validação
│   ├── services/
│   │   └── prediction.py      # Serviço de predição
│   └── main.py               # Aplicação FastAPI
├── models/
│   ├── tesla_lstm_model.keras # Modelo LSTM salvo
│   └── scaler.joblib         # Scaler para normalização
├── tests/
│   ├── integration/
│   ├── unit/
│   └── test_api.py           # Testes da API
└── requirements.txt          # Dependências do projeto
```

## Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Modelo LSTM treinado
- Scaler ajustado aos dados

## Instalação

1. Clone o repositório:
```bash
git clone <repository-url>
cd stock_prediction_api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Salvando o Modelo

Após treinar seu modelo LSTM, salve-o junto com o scaler:

```python
from api.services.prediction import save_artifacts

# Após treinar seu modelo
save_artifacts(model, scaler)
```

## Exemplo de Uso

```python
import requests
import json

# Dados de exemplo (60 dias)
data = {
    "sequence": [
        {
            "open": 150.0,
            "high": 155.0,
            "low": 149.0,
            "close": 153.0,
            "volume": 1000000.0
        }
        # ... mais 59 dias
    ]
}

# Fazer previsão
response = requests.post("http://localhost:8000/predict", json=data)
prediction = response.json()
print(f"Previsão de fechamento: ${prediction['predicted_close']:.2f}")
```

## Detalhes da Implementação

### 1. Validação de Dados
- Utiliza Pydantic para validação de entrada
- Requer exatamente 60 dias de dados históricos
- Valida tipos e formatos dos dados

### 2. Processamento de Dados
- Normalização automática usando o scaler salvo
- Conversão para formato numpy adequado ao modelo
- Desnormalização dos resultados

### 3. Previsão
- Carrega modelo LSTM e scaler automaticamente
- Processa dados de entrada
- Calcula intervalo de confiança
- Retorna previsão desnormalizada

### 4. Tratamento de Erros
- Validação de entrada
- Erros de carregamento do modelo
- Erros durante a previsão
- Logging de erros

## Melhorias Futuras

1. **Segurança**:
   - Adicionar autenticação
   - Limitar requisições por IP
   - Configurar CORS apropriadamente

2. **Performance**:
   - Implementar cache de modelo
   - Otimizar processamento de dados
   - Adicionar rate limiting

3. **Funcionalidades**:
   - Suporte a diferentes modelos
   - Métricas de confiança mais sofisticadas
   - Endpoints para métricas e monitoramento

## Contribuindo

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Crie um Pull Request

 