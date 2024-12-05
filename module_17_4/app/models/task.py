from app.backend.db import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = 'tasks'
    tid = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.uid'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    user = relationship('User', back_populates='tasks')
