# Mikrus API

## Description

This project provides a backend API service.

## Installation

### Using uv

To install project dependencies using `uv`:
```bash
uv pip install -r requirements.txt
```
For development and testing dependencies:
```bash
uv pip install -r requirements-test.txt
```

### Using pip

Alternatively, you can use `pip`:
```bash
pip install -r requirements.txt
```
For development and testing dependencies:
```bash
pip install -r requirements-test.txt
```

## Running Locally

To run the application locally:
```bash
uvicorn app.main:app --reload
```
This command starts a development server that automatically reloads on code changes. The application will be accessible at `http://127.0.0.1:8000`.

## Running Tests

To run the test suite, use `pytest`:
```bash
pytest
```
This command will discover and execute all tests in the `tests/` directory.

## Running with Docker

### Build the Docker image

To build the Docker image for the application:
```bash
docker build -t mikrus-api .
```

### Run the Docker container

To run the application in a Docker container:
```bash
docker run -p 8000:8000 mikrus-api
```
This command maps port 8000 on your host machine to port 8000 in the container, making the API accessible at `http://localhost:8000`.
