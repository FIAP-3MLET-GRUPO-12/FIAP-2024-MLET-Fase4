import numpy as np
from pathlib import Path
from tensorflow.keras.models import load_model
from joblib import load
import logging
from typing import Tuple, Dict

logger = logging.getLogger(__name__)

class PredictionService:
    def __init__(self, model_path: str = "models/tesla_lstm_model.keras", 
                 scaler_path: str = "models/scaler.joblib"):
        """Initialize the prediction service with model and scaler paths."""
        self.model_path = Path(model_path)
        self.scaler_path = Path(scaler_path)
        self.model = None
        self.scaler = None
        self._load_artifacts()

    def _load_artifacts(self):
        """Load the LSTM model and scaler."""
        try:
            self.model = load_model(self.model_path)
            self.scaler = load(self.scaler_path)
            logger.info("Model and scaler loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model or scaler: {str(e)}")
            raise RuntimeError("Failed to load model artifacts")

    def preprocess_input(self, sequence: np.ndarray) -> np.ndarray:
        """Preprocess the input sequence using the saved scaler."""
        if self.scaler is None:
            raise RuntimeError("Scaler not loaded")
        
        # Reshape if needed and scale
        scaled_data = self.scaler.transform(sequence)
        return np.expand_dims(scaled_data, axis=0)  # Add batch dimension

    def postprocess_output(self, prediction: np.ndarray) -> Tuple[float, Dict[str, float]]:
        """Convert the scaled prediction back to original scale and calculate confidence interval."""
        if self.scaler is None:
            raise RuntimeError("Scaler not loaded")

        # Create dummy array for inverse transform
        dummy = np.zeros((1, 5))  # 5 features: OHLCV
        dummy[:, 3] = prediction  # 3 is the index for Close price
        
        # Inverse transform
        unscaled_pred = self.scaler.inverse_transform(dummy)[0, 3]
        
        # Calculate simple confidence interval (you might want to use a more sophisticated method)
        std_dev = 0.02 * unscaled_pred  # Using 2% as example
        confidence_interval = {
            "lower": float(unscaled_pred - 1.96 * std_dev),
            "upper": float(unscaled_pred + 1.96 * std_dev)
        }
        
        return float(unscaled_pred), confidence_interval

    def predict(self, sequence: np.ndarray) -> Tuple[float, Dict[str, float]]:
        """Make a prediction for the given sequence."""
        if self.model is None:
            raise RuntimeError("Model not loaded")

        try:
            # Preprocess
            processed_sequence = self.preprocess_input(sequence)
            
            # Make prediction
            prediction = self.model.predict(processed_sequence, verbose=0)[0, 0]
            
            # Postprocess
            predicted_price, confidence_interval = self.postprocess_output(prediction)
            
            return predicted_price, confidence_interval
            
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise RuntimeError(f"Prediction failed: {str(e)}")

# Function to save model and scaler (to be used after training)
def save_artifacts(model, scaler, 
                  model_path: str = "models/tesla_lstm_model.keras",
                  scaler_path: str = "models/scaler.joblib"):
    """Save the trained model and scaler to files."""
    try:
        # Create directories if they don't exist
        Path(model_path).parent.mkdir(parents=True, exist_ok=True)
        Path(scaler_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Save artifacts
        model.save(model_path)
        load(scaler, scaler_path)
        
        logger.info("Model and scaler saved successfully")
    except Exception as e:
        logger.error(f"Error saving artifacts: {str(e)}")
        raise RuntimeError(f"Failed to save artifacts: {str(e)}") 