from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from src.config.db_connect import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Store tokens in DB
    access_token = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)

    # Relationship (must match Note.user)
    notes = relationship("Note", back_populates="user", cascade="all, delete")