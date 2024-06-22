from fastapi import APIRouter, HTTPException, status

from app.models.example import ExampleDto

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "OK"}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_example(example: ExampleDto):
    return example.model_dump()
