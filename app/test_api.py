# test_api_auth.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader

app = FastAPI(title="Test API Auth")

API_KEY = "test_secret_key"
API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

@app.get("/test", dependencies=[Depends(get_api_key)])
def test():
    return {"message": "Authentication works!"}