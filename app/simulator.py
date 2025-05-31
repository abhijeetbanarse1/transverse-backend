from app.rules_engine import apply_rules
from app.schemas import SimulationInput

def run_simulation(data: SimulationInput) -> dict:
    route_data = {
        "distance_km": 1158,
        "duration_minutes": 820,
        "path": ["Antwerp", "Brussels", "Zurich", "Lyon", "Milan"],
        "base_cost": 520.0
    }
    return apply_rules(route_data, data.scenario, data.vehicle_type)
