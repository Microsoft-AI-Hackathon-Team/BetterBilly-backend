from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import example

app = FastAPI()
app.include_router(example.router, prefix="/example")
# TODO: INSECURE, DEVELOPMENT ONLY
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def read_root():
    return {"message": "OK"}
