
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Use "*" only in development/testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
