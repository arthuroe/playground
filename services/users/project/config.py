# services/users/project/config.py
import os


class BaseConfig:
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    """Development configuration class."""
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(BaseConfig):
    """Testing configuration class."""
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration class."""
    DEBUG = False
