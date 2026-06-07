from datetime import datetime

from pydantic import BaseModel


class UsageRecordCreate(BaseModel):
    provider: str
    model_name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost: float
    request_count: int


class UsageRecordResponse(BaseModel):
    id: int
    provider: str
    model_name: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost: float
    request_count: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }