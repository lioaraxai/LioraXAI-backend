#!/bin/bash

# LioraXAI Project Setup Script
# This script sets up the entire LioraXAI project including static files

# Display colored output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================${NC}"
echo -e "${BLUE}    LioraXAI Project Setup Script        ${NC}"
echo -e "${BLUE}=========================================${NC}"
echo

# Check if the script is being run from the project root
if [ ! -f "manage.py" ]; then
    echo -e "${YELLOW}⚠️  Warning: This script should be run from the LioraXAI project root.${NC}"
    echo -e "${YELLOW}Current directory: $(pwd)${NC}"
    echo -e "${YELLOW}Please change to the project root directory and try again.${NC}"
    exit 1
fi

echo -e "${GREEN}Step 1: Setting up static file directories...${NC}"
mkdir -p lioraxai_app/static/css
mkdir -p lioraxai_app/static/images
mkdir -p lioraxai_app/static/js
mkdir -p staticfiles
echo -e "${GREEN}✓ Static directories created${NC}"
echo

# Create minimal static files if they don't exist
echo -e "${GREEN}Step 2: Setting up minimal static files...${NC}"

# Create a minimal CSS file if it doesn't exist
if [ ! -f "lioraxai_app/static/css/mobile.css" ]; then
    cat > lioraxai_app/static/css/mobile.css << 'EOF'
/* Minimal responsive mobile styling */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  max-width: 100%;
  padding: 15px;
  margin: 0 auto;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #121212;
    color: #f5f5f5;
  }
}
EOF
    echo -e "${GREEN}✓ Created minimal CSS file${NC}"
fi

# Create a minimal JS file for essential functionality
if [ ! -f "lioraxai_app/static/js/main.js" ]; then
    cat > lioraxai_app/static/js/main.js << 'EOF'
// Minimal JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
  console.log('LioraXAI application initialized');
  
  // Mobile menu toggle if it exists
  const menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      document.body.classList.toggle('menu-open');
    });
  }
});
EOF
    echo -e "${GREEN}✓ Created minimal JavaScript file${NC}"
fi

# Create a placeholder image
if [ ! -f "lioraxai_app/static/images/placeholder.svg" ]; then
    cat > lioraxai_app/static/images/placeholder.svg << 'EOF'
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#EEEEEE"/>
  <text x="100" y="100" font-family="Arial" font-size="16" text-anchor="middle">LioraXAI</text>
</svg>
EOF
    echo -e "${GREEN}✓ Created placeholder image${NC}"
fi

# Create a logo image if it doesn't exist
if [ ! -f "lioraxai_app/static/images/logo.svg" ]; then
    cat > lioraxai_app/static/images/logo.svg << 'EOF'
<svg width="150" height="35" xmlns="http://www.w3.org/2000/svg">
  <rect width="30" height="30" x="5" y="3" rx="5" fill="#4f46e5"/>
  <circle cx="20" cy="18" r="8" fill="white"/>
  <text x="40" y="24" font-family="Arial, sans-serif" font-weight="700" font-size="18" fill="#111827">LIORAXAI</text>
</svg>
EOF
    echo -e "${GREEN}✓ Created logo image${NC}"
fi

# Optional: Clone the website repository if requested
if [ "$1" == "--with-website" ]; then
    echo -e "${GREEN}Step 3: Checking for website repository...${NC}"
    if [ ! -d "website" ]; then
        echo -e "${GREEN}Cloning website repository...${NC}"
        git clone https://github.com/lioaraxai/LioraXAI.git website
        
        # Copy CSS files
        if [ -f "website/docs/css/mobile.css" ]; then
            cp website/docs/css/mobile.css lioraxai_app/static/css/
            echo -e "${GREEN}✓ CSS files copied from website${NC}"
        fi
        
        # Copy images
        if [ -d "website/docs/static/images" ]; then
            cp -r website/docs/static/images/* lioraxai_app/static/images/ 2>/dev/null
            echo -e "${GREEN}✓ Images copied from website${NC}"
        fi
        
        # Copy JavaScript files
        if [ -d "website/docs/js" ]; then
            cp website/docs/js/* lioraxai_app/static/js/ 2>/dev/null
            echo -e "${GREEN}✓ JavaScript files copied from website${NC}"
        fi
    else
        echo -e "${GREEN}Website repository already exists.${NC}"
        echo -e "${GREEN}Updating static files from website...${NC}"
        
        # Copy CSS files
        if [ -f "website/docs/css/mobile.css" ]; then
            cp website/docs/css/mobile.css lioraxai_app/static/css/
            echo -e "${GREEN}✓ CSS files updated${NC}"
        fi
        
        # Copy images
        if [ -d "website/docs/static/images" ]; then
            cp -r website/docs/static/images/* lioraxai_app/static/images/ 2>/dev/null
            echo -e "${GREEN}✓ Images updated${NC}"
        fi
        
        # Copy JavaScript files
        if [ -d "website/docs/js" ]; then
            cp website/docs/js/* lioraxai_app/static/js/ 2>/dev/null
            echo -e "${GREEN}✓ JavaScript files updated${NC}"
        fi
    fi
else
    echo -e "${YELLOW}Skipping website repository clone.${NC}"
    echo -e "${YELLOW}To use the complete frontend, run: ./setup.sh --with-website${NC}"
    echo -e "${YELLOW}Using minimal static files for basic functionality.${NC}"
fi
echo

# Create favicon and touch icons if they don't exist
echo -e "${GREEN}Step 4: Creating favicon and touch icons...${NC}"
touch lioraxai_app/static/favicon.ico
touch lioraxai_app/static/apple-touch-icon.png
touch lioraxai_app/static/apple-touch-icon-precomposed.png
echo -e "${GREEN}✓ Favicon and touch icons created${NC}"
echo

# Set up virtual environment
echo -e "${GREEN}Step 5: Setting up virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${GREEN}Step 6: Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo

# Install dependencies
echo -e "${GREEN}Step 7: Installing dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo

# Collect static files
echo -e "${GREEN}Step 8: Collecting static files...${NC}"
python manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"
echo

# Apply migrations
echo -e "${GREEN}Step 9: Applying database migrations...${NC}"
python manage.py migrate
echo -e "${GREEN}✓ Migrations applied${NC}"
echo

# Check if superuser exists
echo -e "${GREEN}Step 10: Checking for superuser...${NC}"
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