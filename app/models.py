from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    beneficiary_email = Column(String)
    shard_c = Column(String)  # Stored encrypted shard
    last_heartbeat = Column(DateTime(timezone=True), server_default=func.now())
    is_dead = Column(Boolean, default=False)
    heartbeat_token = Column(String) # Simple token for authentication via email link

    created_at = Column(DateTime(timezone=True), server_default=func.now())
