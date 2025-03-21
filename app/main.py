from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from app.routers import crm, ecodes, scopeco2  # importa scopeco2
from app.dependencies import verify_api_key, api_key_header

# 🔥 Inicializar la aplicación FastAPI
app = FastAPI(
    title="FastAPI Ecodes API",
    version="0.1.0",
    description="API de Ecodes con autenticación por API Key"
)

# 🔐 Aplicar autenticación a todas las rutas del router CRM
app.include_router(crm.router, dependencies=[Depends(verify_api_key)])
app.include_router(ecodes.router, dependencies=[Depends(verify_api_key)])
app.include_router(scopeco2.router, dependencies=[Depends(verify_api_key)])

# 🔧 Definir la personalización de OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # 🔐 Agregar el esquema de seguridad solo si no existe
    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})["ApiKeyAuth"] = {
        "type": "apiKey",
        "in": "header",
        "name": api_key_header.model.name  # Reutilizamos `api_key_header`
    }

    # 🔒 Aplicar seguridad global a todas las rutas
    openapi_schema["security"] = [{"ApiKeyAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# 🚀 Sobrescribir el esquema OpenAPI
app.openapi = custom_openapi

# 🌍 Endpoint raíz
@app.get("/", response_model=dict, summary="API Status", description="Verifica si la API está activa.")
def root():
    return {"message": "API is working"}
