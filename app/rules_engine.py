def apply_rules(route_data, scenario, vehicle_type):
    eta = route_data["duration_minutes"]
    cost = route_data["base_cost"]
    alerts = []
    risk = "Low"
    co2_per_km = {"diesel": 0.27, "electric": 0.05, "reefer": 0.30}
    co2 = round(route_data["distance_km"] * co2_per_km.get(vehicle_type, 0.25), 2)

    if scenario == "fuel_price_spike":
        cost *= 1.25
        alerts.append("Fuel spike simulated: +25%")

    if "Zurich" in route_data["path"]:
        eta += 60
        alerts.append("Heavy snow in Zurich — 60 mins delay")
        risk = "High"

    if scenario == "hub_outage" and "Lyon" in route_data["path"]:
        eta += 90
        alerts.append("Lyon hub outage — reroute via Marseille.")
        risk = "High"

    if eta > 540:
        eta += 75
        alerts.append("Driver fatigue law triggered: +75 mins rest time")

    driver_wage_per_hour = 22
    wage_cost = (eta / 60) * driver_wage_per_hour
    cost += wage_cost
    alerts.append(f"Driver wage added: €{round(wage_cost, 2)}")

    return {
        "adjusted_eta": eta,
        "adjusted_cost": round(cost, 2),
        "co2_emission_kg": co2,
        "risk_level": risk,
        "alerts": alerts,
        "ai_summary": "Simulation based on live logic: fuel price, weather, driver fatigue, and cost factors applied."
    }
