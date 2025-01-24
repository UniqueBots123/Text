import os

API_ID    = os.environ.get("API_ID", "25888462")
API_HASH  = os.environ.get("API_HASH", "50620d85a99c79e74972df60f0a11da1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7996387931:AAEBqSwxKRa8mT74NVJ7t2RAbGeoaE4nZwk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
