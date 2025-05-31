from pydantic import BaseModel

class SimulationInput(BaseModel):
    origin: str
    destination: str
    vehicle_type: str
    scenario: str
