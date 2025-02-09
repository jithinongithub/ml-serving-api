from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.utils import data_serialization




@patch("src.utils.data_serialization._get_file_dump_path")
def test_data_dump(mock_file_dump_path: Mock):
    mock_file_dump_path.return_value = Path("local-test-data/test_data.pkl")
    test_data = {
        "model_name" : "test_model",
        "model_type" : "classification",
        "model_params" : {
            "n_estimators" : 100,
            "max_depth" : 10
        },
        "model_weights" : [0.1, 0.2, 0.3]
    }
    data_serialization.dump_data(test_data, "test_data.pkl")
    data_loaded = data_serialization.load_data("test_data.pkl")
    assert test_data == data_loaded

