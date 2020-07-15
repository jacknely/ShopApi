import os


class BaseConfig:
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "testing")


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
