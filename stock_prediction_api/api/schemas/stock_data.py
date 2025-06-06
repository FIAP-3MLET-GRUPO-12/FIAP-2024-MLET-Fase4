from pydantic import BaseModel, Field
from typing import List, Dict
import numpy as np

class StockDataInput(BaseModel):
    """
    Schema for stock price prediction input data.
    Expects a sequence of daily stock data points.
    """
    sequence: List[Dict[str, float]] = Field(
        ...,
        description="Sequence of daily stock data points with OHLCV values",
        min_items=60,  # Minimum sequence length
        max_items=60   # Maximum sequence length
    )

    class Config:
        json_schema_extra = {
            "example": {
                "sequence": [
                    {
                        "open": 150.0,
                        "high": 155.0,
                        "low": 149.0,
                        "close": 153.0,
                        "volume": 1000000.0
                    }
                    # ... more days
                ]
            }
        }

    def to_numpy(self) -> np.ndarray:
        """Convert the input sequence to numpy array format required by the model."""
        return np.array([
            [day["open"], day["high"], day["low"], day["close"], day["volume"]]
            for day in self.sequence
        ])

class PredictionResponse(BaseModel):
    """Schema for stock price prediction response."""
    predicted_close: float = Field(..., description="Predicted closing price for the next day")
    confidence_interval: Dict[str, float] = Field(
        ...,
        description="95% confidence interval for the prediction"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "predicted_close": 155.50,
                "confidence_interval": {
                    "lower": 153.25,
                    "upper": 157.75
                }
            }
        } 