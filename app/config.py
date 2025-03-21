import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field

# Cargar variables de entorno desde .env
load_dotenv()

class MySQLSettings(BaseSettings):
    HOST: str = Field(..., alias="MYSQL_HOST")
    PORT: int = Field(..., alias="MYSQL_PORT")
    USER: str = Field(..., alias="MYSQL_USER")
    PASSWORD: str = Field(..., alias="MYSQL_PASSWORD")
    DATABASE: str = Field(..., alias="MYSQL_DATABASE")

class ActiveCampaignSettings(BaseSettings):
    API_URL: str = Field(..., alias="ACTIVE_CAMPAIGN_URL")
    API_KEY: str = Field(..., alias="ACTIVE_CAMPAIGN_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

class AnotherAPISettings(BaseSettings):
    API_URL: str = Field(..., alias="ANOTHER_API_URL")
    API_KEY: str = Field(..., alias="ANOTHER_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

class GeneralSettings(BaseSettings):
    SECRET_KEY: str = Field(..., alias="API_SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

# 🔥 Mover la inicialización de `settings` al final del archivo
active_campaign = ActiveCampaignSettings()
another_api = AnotherAPISettings()
general_settings = GeneralSettings()
mysql_settings = MySQLSettings()