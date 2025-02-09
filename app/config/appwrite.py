from app.config.config import settings
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.services.users import Users
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage


client = Client()

(client
  .set_endpoint(settings.Appwrite_API_ENDPOINT) # Your API Endpoint
  .set_project(settings.APPWRITE_PROJECT_ID) # Your project ID
  .set_key(settings.APPWRITE_API_KEY_SECRET) # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

account = Account(client)
users = Users(client)
databases = Databases(client)
storage = Storage(client)
