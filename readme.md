# ML Serving API

This repository contains the code for a Machine Learning (ML) Serving API. The API allows users to deploy and serve their machine learning models in a scalable and efficient manner.

## Features

- **Model Deployment**: Easily deploy your trained ML models.
- **Scalability**: Handle multiple requests and scale as needed.
- **RESTful API**: Interact with the models using standard HTTP methods.
- **Monitoring**: Track the performance and usage of your models.

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ml-serving-api.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ml-serving-api
    ```
3. Install the required packages using Poetry:
    ```bash
    poetry install
    ```

## Additional Notes  for installing poetry in windows vscode if any issue facing while installing poetry at initial stage
Run this command in Git Bash to install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python -
poetry install
```
Activate poetry virtual env
```bash 
source $(poetry env info --path)\\Scripts\\activate
```
Verify Poetry is now recognized:
```bash
poetry --version
```


### Usage

1. Start the API server:
    ```bash
    python src/main.py
    ```
2. Send a request to the API:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"data": [your_data_here]}' http://localhost:5000/predict
    ```

3. Open the URL
```bash
http://127.0.0.1:8000/docs
```


## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to all the contributors and the open-source community.
