#!/bin/bash

# Display colored output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}    Nirdhar Deployment Script          ${NC}"
echo -e "${BLUE}=========================================${NC}"
echo

# Check if the website directory exists and the user wants to use it
if [ "$1" == "--with-website" ]; then
    if [ ! -d "website" ]; then
        echo -e "${YELLOW}Website directory not found. Cloning it...${NC}"
        git clone https://github.com/shardulkulkarni14/DocChat.git website
    else
        echo -e "${GREEN}Website directory found. Pulling latest changes...${NC}"
        cd website
        git pull
        cd ..
    fi
    
    echo -e "${GREEN}Updating static files from website repository...${NC}"
    # Update static files from website if it exists
    if [ -d "website/docs/css" ]; then
        cp -r website/docs/css/* nirdhar_app/static/css/ 2>/dev/null
    fi
    
    if [ -d "website/docs/static/images" ]; then
        cp -r website/docs/static/images/* nirdhar_app/static/images/ 2>/dev/null
    fi
    
    if [ -d "website/docs/js" ]; then
        cp -r website/docs/js/* nirdhar_app/static/js/ 2>/dev/null
    fi
else
    echo -e "${GREEN}Using backend's built-in static files...${NC}"
    echo -e "${YELLOW}To use the frontend repository, run: ./deploy.sh --with-website${NC}"
fi

# Collect static files
echo -e "${GREEN}Collecting static files...${NC}"
python manage.py collectstatic --noinput

# Make migrations
echo -e "${GREEN}Making migrations...${NC}"
python manage.py makemigrations

# Apply migrations
echo -e "${GREEN}Applying migrations...${NC}"
python manage.py migrate

echo -e "${GREEN}Deployment preparation complete!${NC}"
echo
echo -e "${BLUE}For PythonAnywhere deployment:${NC}"
echo -e "1. Clone the repository: ${YELLOW}git clone https://github.com/shardulkulkarni14/nirdhar-backend.git${NC}"
echo -e "2. Run setup.sh: ${YELLOW}./setup.sh${NC}"
echo -e "3. Configure your STATIC_ROOT path in PythonAnywhere's web app settings"
echo -e "4. Set the environment variable ${YELLOW}DJANGO_SETTINGS_MODULE=nirdhar_project.settings_production${NC}"
echo -e "5. Remember to set ${YELLOW}DEBUG=False${NC} in production" 