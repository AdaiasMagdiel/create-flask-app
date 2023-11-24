import os
from flask import Flask
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        for key, value in os.environ.items():
            self.__setattr__(key, value)

    def init_app(self, app: Flask):
        app.config.from_object(self)


settings = Config()
