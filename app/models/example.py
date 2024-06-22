from typing import Union
from pydantic import BaseModel


class ExampleDto(BaseModel):
    example: Union[str, None] = None
