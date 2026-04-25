# AI Run Tracker API

## Overview

The goal is to grow it into a small AI-ready API with database, testing, Docker, and cloud deployment.

## Current Features

- FastAPI application entrypoint
- Health endpoint for local verification
- More API features will be added in later sprint tasks


## Setup:

pip install -r requirements.txt


## Run Locally: 

uvicorn app.main:app --reload


## Verify the API:

http://127.0.0.1:8000/health


## A successful response returns JSON: 

{"message":"You are healthy!"} 

