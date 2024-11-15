
from pydantic import BaseModel, field_validator

class UserModel(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list[str]
    tags: list[dict]
    status: str

    @field_validator("id", "category", "name", "photoUrls", "tags", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError(f"Field is empty")
        else:
            return value