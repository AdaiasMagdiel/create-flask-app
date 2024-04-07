import os
from flask import Flask
from dotenv import load_dotenv


class Config:
    ENV_MODE: str
    DETA_PROJECT_KEY: str
    CACHE_TABLE: str

    def init_app(self, app: Flask) -> None:
        load_dotenv()

        for key, value in os.environ.items():
            self.__set_flask_configs(app, key, value)
            setattr(self, key, value)

    def __set_flask_configs(self, app: Flask, key: str, value: str) -> None:
        if 'FLASK_' in key.upper():
            key = key.replace('FLASK_', '')
            app.config[key] = value


settings = Config()
