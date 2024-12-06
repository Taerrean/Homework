from app.backend.db import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    tasks = relationship('Task', back_populates='user')
