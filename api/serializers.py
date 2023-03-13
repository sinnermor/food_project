from typing import List

from pydantic import BaseModel, Field


class FoodRequestModel(BaseModel):
    """Model for request"""
    name: str = Field(description="Product name")
    q: int = Field(description="Product count")


class FreezList(BaseModel):
    products: List[FoodRequestModel]
