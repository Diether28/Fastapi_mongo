from typing import Optional
from pydantic import BaseModel

class Vet(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str