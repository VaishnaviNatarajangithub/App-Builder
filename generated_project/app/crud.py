"""CRUD (Create, Read, Update, Delete) operations for the blog application.

This module provides helper functions that operate on SQLAlchemy ``Session``
objects to interact with the ``Post`` model. The functions are used by the API
routers to perform database actions.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from . import schemas
from .models import Post

__all__ = [
    "get_posts",
    "get_post",
    "create_post",
    "update_post",
    "delete_post",
]


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> List[Post]:
    """Return a list of ``Post`` objects.

    Args:
        db: SQLAlchemy session.
        skip: Number of records to skip (for pagination).
        limit: Maximum number of records to return.

    Returns:
        List of ``Post`` instances.
    """
    return db.query(Post).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int) -> Optional[Post]:
    """Retrieve a single ``Post`` by its primary key.

    Args:
        db: SQLAlchemy session.
        post_id: Identifier of the post.

    Returns:
        The ``Post`` instance if found, otherwise ``None``.
    """
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, post: schemas.PostCreate) -> Post:
    """Create a new ``Post`` record in the database.

    Args:
        db: SQLAlchemy session.
        post: Pydantic schema containing the data for the new post.

    Returns:
        The newly created ``Post`` instance.
    """
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, db_post: Post, updates: schemas.PostUpdate) -> Post:
    """Apply updates to an existing ``Post``.

    Only fields that are not ``None`` in ``updates`` are applied.

    Args:
        db: SQLAlchemy session.
        db_post: The existing ``Post`` object fetched from the database.
        updates: Pydantic schema with optional fields to update.

    Returns:
        The updated ``Post`` instance.
    """
    update_data = updates.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_post, field, value)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, db_post: Post) -> None:
    """Delete a ``Post`` from the database.

    Args:
        db: SQLAlchemy session.
        db_post: The ``Post`` instance to delete.
    """
    db.delete(db_post)
    db.commit()
