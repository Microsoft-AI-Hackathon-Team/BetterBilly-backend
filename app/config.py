from pydantic_settings import BaseSettings


class Config(BaseSettings):
    EXAMPLE: str = "example"


config = Config()
