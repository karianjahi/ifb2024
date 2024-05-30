#!/bin/bash

# Activate virtual environment (if not already activated)
source venv/bin/activate

# Run Gunicorn to serve the Flask app
gunicorn --bind 0.0.0.0:80 application:app
