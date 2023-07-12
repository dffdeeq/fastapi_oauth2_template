from decouple import config


class Settings:
    POSTGRES_HOST = config('POSTGRES_HOST', cast=str, default='localhost')
    POSTGRES_USER = config('POSTGRES_USER', cast=str, default='postgres')
    POSTGRES_PORT = config('POSTGRES_PORT', cast=str, default='5433')
    POSTGRES_DB = config('POSTGRES_DB', cast=str, default='postgres')
    POSTGRES_PASSWORD = config('POSTGRES_PASSWORD', cast=str, default='root')

    JWT_SECRET = config('JWT_SECRET', cast=str, default='myjwtsecret')


settings = Settings()
