from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import passlib.hash as _hash


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password = mapped_column(String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)
