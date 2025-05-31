
from app.schemas import SimulationRequest

def simulate_transport(request: SimulationRequest):
    # Basic dummy simulation logic
    base_time = 60  # minutes
    base_cost = 100  # currency units

    if request.scenario == "traffic_jam":
        base_time *= 1.5
    elif request.scenario == "fuel_price_spike":
        base_cost *= 1.3
    elif request.scenario == "weather_delay":
        base_time *= 1.8
        base_cost *= 1.2

    if request.vehicle_type == "truck":
        base_cost *= 1.5
    elif request.vehicle_type == "reefer":
        base_cost *= 2.0

    return {
        "origin": request.origin,
        "destination": request.destination,
        "vehicle_type": request.vehicle_type,
        "scenario": request.scenario,
        "estimated_time_minutes": round(base_time, 2),
        "estimated_cost": round(base_cost, 2)
    }
