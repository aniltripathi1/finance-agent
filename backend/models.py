from pydantic import BaseModel
from datetime import datetime

class User(Basemodel):
    id:int
    email:str
    hashed_pass:str
    created_at:datetime

class Transaction(BaseModel):
    