from fastapi import APIRouter

router = APIRouter()

@router.post("")
def chat():
    # Temporary placeholder
    return {"answer": "Chat endpoint placeholder"}
