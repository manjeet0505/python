from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel , ConfigDict


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags = List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime : lambda v: v.strftime('%d-%m-%Y-%H:%M:$S')}
    )

user = User(
    id=1,
    name="Manjeet",
    email="mishramanjeet26@gmail.com",
    createdAt=datetime(2025 , 3 ,15,14,30),
    address=Address(
        street="Something",
        city="Jaipur",
        postal_code="0000976"
    ),
    is_active=False,
    tags=["premium","subscriber"]
)

python_dict = user.model_dump()
print(user)
# address = Address(
#     street= "Kirti ngar sec-15 part-1",
#     city = "Gurugram",
#     postal_code = "10001"
# )
# user = User(
#     id = 23,
#     name = "Manjeet",
#     address = address
# )