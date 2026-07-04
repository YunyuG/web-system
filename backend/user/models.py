from dbutil import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "user"
    __table_args__ = {"schema": "websystem"}
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    email: str

class UserCreate(UserCreate):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int