from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello world!"}


@router.get("/health")
async def health():
    return {"message": "You are healthy!"}