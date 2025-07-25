#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the FastAPI application
uvicorn app.main:app --reload
