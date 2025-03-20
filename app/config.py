import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del .env

class Settings:
    API_URL = os.getenv("ACTIVE_CAMPAIGN_URL")
    API_KEY = os.getenv("ACTIVE_CAMPAIGN_KEY")

settings = Settings()
