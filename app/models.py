from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base


class PaymentToken(Base):
    """One-time access token generated after successful payment.
    
    Flow:
    1. User pays via x402 at /app
    2. Server generates a PaymentToken with unique temp_id
    3. Returns JSON: {"message": "congrats payment succeeded", "redirect": "/app/{temp_id}"}
    4. User visits /app/{temp_id} and creates vault
    5. Token is consumed (is_consumed = True), can never be used again
    """
    __tablename__ = "payment_tokens"

    id = Column(Integer, primary_key=True, index=True)
    temp_id = Column(String, unique=True, index=True)  # The unique access token (URL-safe)
    is_consumed = Column(Boolean, default=False)  # Once used, can't be used again
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    consumed_at = Column(DateTime(timezone=True), nullable=True)  # When it was used
    expires_at = Column(DateTime(timezone=True))  # Tokens expire after 1 hour


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    beneficiary_email = Column(String)
    shard_c = Column(String)  # AES-GCM encrypted, key derived from heartbeat_token
    
    # IMMUTABILITY PROTECTION: Hash of original config
    # Hash = SHA256(beneficiary_email + shard_c + created_at)
    # If attacker modifies beneficiary_email, hash won't match
    config_hash = Column(String)  # Immutable commitment
    
    last_heartbeat = Column(DateTime(timezone=True), server_default=func.now())
    is_dead = Column(Boolean, default=False)
    heartbeat_token = Column(String)  # Simple token for authentication via email link
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
