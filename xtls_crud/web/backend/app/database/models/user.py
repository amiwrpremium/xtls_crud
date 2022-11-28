from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, text

from datetime import datetime


from ..db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, server_default=text("CURRENT_TIMESTAMP"), nullable=False)
