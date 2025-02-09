from appwrite.client import Client
from app.config.config import settings

client = Client()

(client
  .set_endpoint(settings.Appwrite_API_ENDPOINT) # Your API Endpoint
  .set_project(settings.APPWRITE_PROJECT_ID) # Your project ID
  .set_key(settings.APPWRITE_API_KEY_SECRET) # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)