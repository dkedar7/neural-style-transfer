# Neural Style Transfer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/dkedar7/Data-Analyzer/flask)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/dkedar7/Data-Analyzer/dash)

<!-- ![Data Analyzer Demo](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/Demo.png?raw=true) -->

#### Under active development
Inspired from this PyTorch [tutorial](https://github.com/pytorch/tutorials/blob/master/advanced_source/neural_style_tutorial.py)


## Installation (WIP)

The demo application is currently hosted [here](https://neural-style-transfer-hpn4y2dvda-uc.a.run.app/).

#### Step 1. Clone this repository by running

    git clone https://github.com/dkedar7/neural-style-transfer
    
#### Step 2. Create a virtual environement by running

    python -m venv StyleTransfer
        
#### Step 3. Active this environment, on Windows:

    StyleTransfer\scripts\activate

MacOS or Linux:

    source StyleTransfer/bin/activate
    
#### Step 4. Open the directory and install dependencies

    cd style-transfer/
    pip install -r requirements.txt
    
#### Step 5. Launch the web application

    python run.py
    
Use `localhost:8080` to interact with the application.

## About the demo deployment

The [demo deployment](https://neural-style-transfer-hpn4y2dvda-uc.a.run.app/) uses Google Build to containerize the application, Google Container Registry for storing and managing a container and Google Cloud Run to deploy it as a web endpoint.

![Cloud Run Architecture](https://github.com/dkedar7/Data-Analyzer/blob/master/Analyzer/assets/architecture.png?raw=true)

[More about Google Cloud Run](https://cloud.google.com/run/docs/)

## Limitations (WIP)

## License
Neural Style Transfer uses the [MIT license](https://github.com/dkedar7/neural-style-transfer/blob/master/LICENSE).

## Dependencies

You need [Python 3](https://python3statement.org/) to run this application. Other dependencies can be found in the [requirements.txt](https://github.com/dkedar7/neural-style-transfer/blob/main/style-transfer/requirements.txt) file.