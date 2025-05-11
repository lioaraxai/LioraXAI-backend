#!/bin/bash

# Add Poetry to the PATH
export PATH="$HOME/.local/bin:$PATH"
 
# Run the server with Poetry
echo "Starting LioraXAI Django server with Poetry..."
poetry run python manage.py runserver 8080 