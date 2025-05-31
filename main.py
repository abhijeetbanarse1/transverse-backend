from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.simulator import simulate_transport
from app.schemas import SimulationRequest

app = FastAPI()

# ✅ Replace this with your actual S3 frontend URL
origins = [
    "https://transverse-ai-ui.s3.us-east-2.amazonaws.com"
]

# CORS Middleware to fix the frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to TransVerse AI"}

@app.post("/simulate")
async def simulate_route(request: SimulationRequest):
    result = simulate_transport(request)
    return result
