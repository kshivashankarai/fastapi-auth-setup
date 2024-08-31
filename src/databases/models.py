import uuid
from datetime import datetime, date
from typing import List, Optional

from sqlmodel import SQLModel, Field, Column, Relationship, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, TIMESTAMP, CHAR

import sqlalchemy as sa


class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(CHAR(36), nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    email: str = Field(sa_column=Column(VARCHAR(255), nullable=False, unique=True))
    first_name: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    last_name: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    role: str = Field(
        sa_column=Column(VARCHAR(255), nullable=False, server_default="user")
    )
    is_verified: bool = Field(default=False)
    password_hash: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(
        sa_column=Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    )
    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self):
        return f"<User {self.uid}>"


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(CHAR(36), nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    author: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    publisher: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    published_date: date = Field(sa_column=Column(sa.DATE, nullable=False))
    page_count: int = Field(sa_column=Column(sa.INTEGER, nullable=False))
    language: str = Field(sa_column=Column(VARCHAR(255), nullable=False))
    user_uid: Optional[uuid.UUID] = Field(
        sa_column=Column(CHAR(36), ForeignKey("users.uid"), nullable=False)
    )
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(
        sa_column=Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    )
    user: Optional[User] = Relationship(back_populates="books")

    def __repr__(self):
        return f"<Review {self.title}>"
