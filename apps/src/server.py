from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.src.router import routers_auth, routers_controle_km

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5050",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers_auth.router)
app.include_router(routers_controle_km.router, prefix='/controleKm')
