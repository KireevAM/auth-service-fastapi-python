class Settings:
    PROJECT_NAME = "Auth Service"
    DATABASE_URL = "postgresql://auth_user:auth_password@db:5432/auth_db"  # PostgreSQL URL
    SECRET_KEY = "your-secret-key-here-change-in-production"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()