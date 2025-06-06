from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from datetime import datetime

from .schemas.stock_data import StockDataInput, PredictionResponse
from .services.prediction import PredictionService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Stock Price Prediction API",
    description="API for predicting stock prices using LSTM model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize prediction service
try:
    prediction_service = PredictionService()
except Exception as e:
    logger.error(f"Failed to initialize prediction service: {str(e)}")
    raise RuntimeError("Failed to initialize prediction service")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(data: StockDataInput):
    """
    Predict the next day's closing price based on the input sequence.
    
    Args:
        data: Sequence of daily stock data points (OHLCV values)
        
    Returns:
        Predicted closing price and confidence interval
    """
    try:
        # Convert input data to numpy array
        sequence = data.to_numpy()
        
        # Make prediction
        predicted_price, confidence_interval = prediction_service.predict(sequence)
        
        return PredictionResponse(
            predicted_close=predicted_price,
            confidence_interval=confidence_interval
        )
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 