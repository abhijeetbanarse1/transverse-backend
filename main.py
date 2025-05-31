
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.simulator import simulate_transport
from app.schemas import SimulationRequest

app = FastAPI()

# CORS middleware to allow frontend calls from S3
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/simulate")
def simulate(request: SimulationRequest):
    result = simulate_transport(request)
    return result
