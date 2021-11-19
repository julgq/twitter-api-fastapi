
# python
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastAPI
from fastapi import FastAPI


app = FastAPI()

# Models

class UserBase(BaseModel):
	user_id: UUID
	email: EmailStr = Field(...)

class UserLogin(UserBase):
	password: str = Field(..., min_length=8, max_length=64)

class User(UserBase):
	first_name: str = Field(..., min_length=50, max_length=50)
	birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
	tweet_id: UUID = Field(...)
	content: str = Field(..., max_length=256, min_length=1)
	created_at: datetime = Field(default=date.now())
	update_at: Optional[datetime] = Field(default=None)
	by: User = Field(...)


@app.get(path="/")
def home():
	return {"Twitter API": "working!"}
