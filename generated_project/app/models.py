"""SQLAlchemy ORM model definitions for the blog application.

This module defines the `Post` model representing a blog post. It is used by the
schemas for type hints, the CRUD utilities for database operations, and the
application entry point for creating tables.
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from .database import Base


class Post(Base):
    """ORM model for a blog post.

    Attributes:
        id: Primary key identifier.
        title: Title of the post, max length 200 characters.
        content: Full text content of the post.
        created_at: Timestamp when the post was created.
        updated_at: Timestamp when the post was last updated.
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


__all__ = ["Post"]
