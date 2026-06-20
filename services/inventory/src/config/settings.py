from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    rabbitmq_host: str
    rabbitmq_port: int
    rabbitmq_exchange: str


    class Config:
        env_file = ".env"



settings = Settings()