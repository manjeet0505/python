from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street= "Kirti ngar sec-15 part-1",
    city = "Gurugram",
    postal_code = "10001"
)
user = User(
    id = 23,
    name = "Manjeet",
    address = address
)