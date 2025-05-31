
from pydantic import BaseModel

class SimulationRequest(BaseModel):
    origin: str
    destination: str
    vehicle_type: str
    scenario: str
