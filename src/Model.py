class Model:
    def __init__(self, model_name, model_type, model_params, model_weights):
        self.model_name = model_name
        self.model_type = model_type
        self.model_params = model_params
        self.model_weights = model_weights

    def predict(self, data: list) -> dict:
        return {
            "model_name": self.model_name,
            "prediction" : [a*b for a,b in zip(data, self.model_weights)]
        }