from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from app.config import general_settings
# Definir el esquema de autenticación una sola vez
API_KEY_NAME: str = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    """Verifica que la API Key enviada sea válida."""
    expected_api_key = general_settings.SECRET_KEY.strip() if general_settings.SECRET_KEY else None
    
    if not api_key or api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return api_key  # Retornamos la API Key si es válida
