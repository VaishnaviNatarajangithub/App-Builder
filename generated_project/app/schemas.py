'''Pydantic models for request validation and response serialization.

These schemas are used throughout the FastAPI application for type hinting,
validation of incoming request bodies, and serialization of ORM objects in
responses.
'''

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    """Base schema shared by creation and update operations.

    Attributes:
        title: Title of the post, limited to 200 characters.
        content: Full text content of the post.
    """

    title: str = Field(..., max_length=200)
    content: str


class PostCreate(PostBase):
    """Schema for creating a new post.

    Inherits all fields from ``PostBase`` without modification.
    """

    pass


class PostUpdate(BaseModel):
    """Schema for updating an existing post.

    All fields are optional to allow partial updates.
    """

    title: Optional[str] = None
    content: Optional[str] = None


class PostOut(PostBase):
    """Schema for returning post data to clients.

    Extends ``PostBase`` with database‑generated fields.
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


__all__ = ["PostBase", "PostCreate", "PostUpdate", "PostOut"]
