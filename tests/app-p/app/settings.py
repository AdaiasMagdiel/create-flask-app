from flask import Flask
from dotenv import dotenv_values


class Config:
    def init_app(self, app: Flask) -> None:
        for key, value in dotenv_values().items():
            app.config[key] = value
            setattr(self, key, value)


settings = Config()
