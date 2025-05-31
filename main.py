from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.simulator import run_simulation
from app.schemas import SimulationInput
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace * with your S3 domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/simulate")
async def simulate(data: SimulationInput):
    result = run_simulation(data)
    return JSONResponse(content=result)