import pickle
from pathlib import Path


def _get_file_dump_path(file: str) -> Path:
    return Path(f"model/{file}.pkl")

def dump_data(data: dict, file_name: str):
    with open(_get_file_dump_path(file_name), 'wb') as file:
        pickle.dump(data, file) #type: ignore

def load_data(file_name: str) -> dict:
    with open(_get_file_dump_path(file_name), 'rb') as file:
        return pickle.load(file)
