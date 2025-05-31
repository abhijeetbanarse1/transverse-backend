from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import SimulationRequest
from app.simulator import simulate_transport

app = FastAPI()

# CORS setup to allow frontend access from S3
origins = [
    "https://transverse-ai-ui.s3.us-east-2.amazonaws.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/simulate")
async def simulate(request: SimulationRequest):
    result = simulate_transport(request)
    return {"result": result}
