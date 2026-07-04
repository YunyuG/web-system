from pydantic_settings import BaseSettings,SettingsConfigDict


class DBSettings(BaseSettings):
    host: str = "localhost"
    port: int = 9091
    username: str = "postgres"
    password: str = "********"
    database: str = "postgres"

    model_config = SettingsConfigDict(
        # case_sensitive = True
        env_prefix = "db_",
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra="ignore"
    )


class BackendSettings(BaseSettings):
    host: str = "localhost"
    port: int = 26704

    model_config = SettingsConfigDict(
        # case_sensitive = True
        env_prefix = "url_",
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra="ignore"
    ) 

db_settings = DBSettings()
backend_settings = BackendSettings()

# print(db_settings)