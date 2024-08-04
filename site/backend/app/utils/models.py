from sqlalchemy import TIMESTAMP, Text, Column, String, Boolean, Integer

from app.utils.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    pnoun = Column(String)
    phone_num = Column(String)
    location = Column(String)
    user_type = Column(String(1))
    public = Column(Boolean)
    profile_bio = Column(Text)
    onboarded = Column(Boolean)
    createdAt = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    cid = Column(Integer)
    last_seen = Column(TIMESTAMP)
    score = Column(Integer)


class Interest(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, index=True)
    interest_label = Column(String)
    category_id = Column(Integer)
    is_custom = Column(Boolean)


# Add other models similarly...
