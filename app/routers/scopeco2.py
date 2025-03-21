from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter(prefix="/scopeco2", tags=["SCOPECO2"])

# Modelo de entrada
class ConsumoElectricoInput(BaseModel):
    anio: int = Field(..., ge=2000, le=datetime.now().year + 1)
    comercializadora: int
    consumo_anual_kwh: float = Field(..., gt=0)
    contador: str
    uso: int
    garantia_origen_id: int
    porcentaje: float = Field(..., ge=0, le=100)

# Modelo de salida
class ConsumoElectricoOutput(BaseModel):
    total_emisiones: float
    unidad: str = "kg CO2"
    detalle: dict

@router.post("/calculos/consumo_electrico", response_model=ConsumoElectricoOutput)
def calcular_consumo_electrico(data: ConsumoElectricoInput):
    """
    Calcula las emisiones de CO2 basadas en el consumo eléctrico anual,
    teniendo en cuenta la garantía de origen.
    """

    # Aquí puedes definir factores reales por comercializadora
    # Por ahora, usamos uno fijo
    factor_emision = 0.00025  # en toneladas por kWh

    # Validación extra si quisieras:
    if not (2000 <= data.anio <= datetime.now().year + 1):
        raise HTTPException(status_code=400, detail="El año ingresado no es válido.")

    # Cálculo
    total_emisiones = (data.consumo_anual_kwh * factor_emision * 1000) * (1 - data.porcentaje / 100)

    return ConsumoElectricoOutput(
        total_emisiones=round(total_emisiones, 4),
        detalle={
            "año": data.anio,
            "comercializadora_id": data.comercializadora,
            "consumo_kwh": data.consumo_anual_kwh,
            "uso_id": data.uso,
            "contador": data.contador,
            "garantia_origen_id": data.garantia_origen_id,
            "porcentaje_compensado": data.porcentaje,
            "factor_emision_utilizado": factor_emision
        }
    )
