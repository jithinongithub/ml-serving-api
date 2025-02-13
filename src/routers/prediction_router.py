from pathlib import Path
import sys
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import cloudpickle as pickle
from src.Model import Model

sys.modules['__main__'].Model = Model

class PredictionRequest(BaseModel):
    input_data: list[int]

class PredictionResponse(BaseModel):
    model_name: str
    prediction: list[float]

class PredictionRouter:
    def __init__(self):
        self.router = APIRouter()
        current_dir = Path(__file__).parent.parent
        parent_dir = current_dir.parent
        model_path = parent_dir / "model/model.pkl"
        print('model_path:', model_path)
        try:
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
            print("✅ Model loaded successfully")
        except FileNotFoundError:
            print(f"❌ Model file NOT FOUND at {model_path}")
            self.model = None
        except AttributeError as e:
            print(f"❌ Pickle loading error: {e}")
            self.model = None


    def create_prediction_router(self) -> APIRouter:
        @self.router.post("/predict", response_model=PredictionResponse)
        async def predict(request: PredictionRequest):
            if self.model is None:
                raise HTTPException(status_code=500, detail="Model not loaded")
            try:
                prediction = self.model.predict(request.input_data)
                return PredictionResponse(
                    model_name=self.model.model_name,
                    prediction=prediction["prediction"]
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        return self.router

    async def predict(self, input_data: list[int]) -> dict:
        if self.model is None:
            raise ValueError("Model not loaded")
        return {"prediction": self.model.predict(input_data)}




