# Experiment 6 - Setting up LLM Deployment Infrastructure

This project implements a simple Large Language Model deployment workflow using:

- Python
- Hugging Face Transformers
- FastAPI
- Uvicorn
- Docker

## Aim

To create an inference application for an LLM, expose it through a REST API, and package it in Docker.

## Project Structure

- `app.py` - FastAPI application with `/` and `/generate` endpoints
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions
- `test_api.py` - Script to test five sample prompts against the API

## Model Used

- `google/flan-t5-small`

## Run Locally

Important: use Python 3.11 or 3.12 for this experiment. PyTorch may fail on Python 3.14 on Windows.

1. Open the terminal in the `LLM_Deployment` folder.
2. Create and activate a virtual environment using Python 3.11 or 3.12.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Start the API:
   - `uvicorn app:app --reload`
5. Open Swagger UI:
   - `http://127.0.0.1:8000/docs`
6. Test `/generate` with a prompt.

## Test Prompts

Use `test_api.py` after starting the server to test these prompts:

1. What is artificial intelligence?
2. Explain machine learning in simple words.
3. What is a neural network?
4. Explain the Transformer model.
5. What is natural language processing?

## Run with Docker

1. Build the image:
   - `docker build -t llm-api .`
2. Run the container:
   - `docker run -p 8000:8000 llm-api`
3. Open Swagger UI:
   - `http://localhost:8000/docs`
4. Test the `/generate` endpoint again.

## Expected Outcome

A working LLM inference service accessible through a FastAPI REST API, both locally and inside Docker.
