from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.simulator import simulate_transport
from app.schemas import SimulationRequest

# Initialize the FastAPI app
app = FastAPI()

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your S3 URL for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define simulation endpoint
@app.post("/simulate")
async def simulate(request: SimulationRequest):
    return simulate_transport(request)
