from src.utils import data_serialization


def dump_sample_data():
    test_data = {
        "model_name" : "test_model",
        "model_type" : "classification",
        "model_params" : {
            "n_estimators" : 100,
            "max_depth" : 10
        },
        "model_weights" : [0.1, 0.2, 0.3]
    }
    data_serialization.dump_data(test_data, "test_data")




if __name__ == "__main__":
    dump_sample_data()
    # Start a simple development server for local use


