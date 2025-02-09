import uvicorn
from fastapi import FastAPI

from src.Model import Model
from src.routers.prediction_router import PredictionRouter
from src.utils import data_serialization

app = FastAPI()
app.include_router(PredictionRouter().create_prediction_router())

# Construct the path to the parent directory


def dump_sample_data():
    sample_model = Model("sample_model", "classification", {"n_estimators": 100, "max_depth": 10}, [0.1, 0.2, 0.3])
    data_serialization.dump_data(sample_model, "model")
    model_loaded = data_serialization.load_data("model")
    print(model_loaded.predict([10, 20, 30]))


if __name__ == "__main__":
    # dump_sample_data() if you want to change the current model for running the server with your model
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # Start a simple development server for local use


