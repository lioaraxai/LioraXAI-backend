#!/bin/bash

# Nirdhar Project Setup Script
# This script sets up the entire Nirdhar project including static files

# Display colored output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}    Nirdhar Project Setup Script        ${NC}"
echo -e "${BLUE}=========================================${NC}"
echo

# Check if the script is running from the project root
if [ ! -f "manage.py" ]; then
    echo -e "${YELLOW}⚠️  Warning: This script should be run from the Nirdhar project root.${NC}"
    echo -e "${YELLOW}Current directory: $(pwd)${NC}"
    echo -e "${YELLOW}Please change to the project root directory and try again.${NC}"
    exit 1
fi

echo -e "${GREEN}Step 1: Setting up static file directories...${NC}"
mkdir -p nirdhar_app/static/css
mkdir -p nirdhar_app/static/images
mkdir -p nirdhar_app/static/js
echo -e "${GREEN}✓ Static directories created${NC}"
echo

# Check if the website directory exists
if [ -d "website" ]; then
    echo -e "${GREEN}Step 2: Copying static files from the website repository...${NC}"
    
    # Copy CSS files
    if [ -f "website/docs/css/mobile.css" ]; then
        cp website/docs/css/mobile.css nirdhar_app/static/css/
        echo -e "${GREEN}✓ CSS files copied${NC}"
    else
        echo -e "${YELLOW}⚠️  Warning: mobile.css not found in website/docs/css/${NC}"
    fi
    
    # Copy images
    if [ -d "website/docs/static/images" ]; then
        cp -r website/docs/static/images/* nirdhar_app/static/images/ 2>/dev/null
        echo -e "${GREEN}✓ Images copied${NC}"
    else
        echo -e "${YELLOW}⚠️  Warning: images directory not found in website/docs/static/${NC}"
    fi
    
    # Copy JavaScript files
    if [ -d "website/docs/js" ]; then
        cp website/docs/js/* nirdhar_app/static/js/ 2>/dev/null
        echo -e "${GREEN}✓ JavaScript files copied${NC}"
    else
        echo -e "${YELLOW}⚠️  Warning: js directory not found in website/docs/${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Warning: website directory not found. Skipping static file copying.${NC}"
    echo -e "${YELLOW}If you need the static files, clone the frontend repository:${NC}"
    echo -e "${YELLOW}git clone https://github.com/shardulkulkarni14/DocChat.git website${NC}"
fi
echo

# Create favicon and touch icons if they don't exist
echo -e "${GREEN}Step 3: Creating favicon and touch icons...${NC}"
touch nirdhar_app/static/favicon.ico
touch nirdhar_app/static/apple-touch-icon.png
touch nirdhar_app/static/apple-touch-icon-precomposed.png
echo -e "${GREEN}✓ Favicon and touch icons created${NC}"
echo

# Set up virtual environment
echo -e "${GREEN}Step 4: Setting up virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${GREEN}Step 5: Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo

# Install dependencies
echo -e "${GREEN}Step 6: Installing dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo

# Collect static files
echo -e "${GREEN}Step 7: Collecting static files...${NC}"
python manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"
echo

# Apply migrations
echo -e "${GREEN}Step 8: Applying database migrations...${NC}"
python manage.py migrate
echo -e "${GREEN}✓ Migrations applied${NC}"
echo

# Check if superuser exists
echo -e "${GREEN}Step 9: Checking for superuser...${NC}"
SUPERUSER_EXISTS=$(python -c "
import django
django.setup()
from django.contrib.auth.models import User
print(User.objects.filter(is_superuser=True).exists())
" 2>/dev/null)

if [ "$SUPERUSER_EXISTS" = "True" ]; then
    echo -e "${GREEN}✓ Superuser already exists${NC}"
else
    echo -e "${YELLOW}No superuser found. You should create one with:${NC}"
    echo -e "${YELLOW}python manage.py createsuperuser${NC}"
fi
echo

echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}✅ Setup complete!${NC}"
echo -e "${BLUE}=========================================${NC}"
echo
echo -e "To start the server, run:"
echo -e "${YELLOW}source venv/bin/activate && python manage.py runserver${NC}"
echo
echo -e "Or use the run_server.sh script:"
echo -e "${YELLOW}./run_server.sh${NC}"
echo
echo -e "Access the site at: ${BLUE}http://127.0.0.1:8000/${NC}"
echo -e "Admin panel at: ${BLUE}http://127.0.0.1:8000/admin/${NC}"
echo 