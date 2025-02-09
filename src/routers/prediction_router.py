from pathlib import Path

from fastapi import APIRouter
import cloudpickle as pickle

class PredictionRouter:
    def __init__(self):
        self.router = APIRouter()
        current_dir = Path(__file__).parent.parent
        parent_dir = current_dir.parent
        model_path = parent_dir / "model/model.pkl"
        self.model = pickle.load(open(model_path, "rb"))

    def create_prediction_router(self) -> APIRouter:
        self.router.post("/predict")(self.predict)
        return self.router

    def predict(self, input_data: list[int]) -> dict:
        return self.model.predict(input_data)




