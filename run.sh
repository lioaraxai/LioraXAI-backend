#!/bin/bash

# Simple script to run the Django development server using Poetry
# Usage: ./run.sh [port]
# Example: ./run.sh 8080

PORT=${1:-8000}  # Default to port 8000 if not specified

echo "Starting Django development server on port $PORT..."
poetry run python manage.py runserver $PORT 