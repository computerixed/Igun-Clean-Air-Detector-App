import sys
import os

# Add the parent directory to the path so we can import from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from the root directory
from app import app

# For Vercel serverless functions, we need to export the app
# Vercel automatically handles the WSGI interface
app = app