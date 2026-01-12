
from pydantic import BaseModel

# v1
class LibroV1(BaseModel):
    id: int
    titulo: str
    """
    class Config:
        orm_mode = True
    """
    model_config = {
        "from_attributes": True
    }

# v2
class LibroV2(LibroV1):
    autor: str
