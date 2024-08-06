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
    createdAt = Column(String)
    updated_at = Column(String)
    last_seen = Column(String)
    score = Column(Integer)
    cid = Column(Integer)


class Interest(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, index=True)
    interest_label = Column(String)
    category_id = Column(Integer)
    is_custom = Column(Boolean)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    is_custom = Column(Boolean)


class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String)
    school_img_url = Column(String)
    is_custom = Column(Boolean)


class UserEducation(Base):
    __tablename__ = "user_education"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    school_id = Column(Integer)
    major = Column(Integer)
    minor = Column(Integer)
    graduated_year = Column(Integer)
    expected_grad_year = Column(Integer)
    updated_at = Column(TIMESTAMP)
    location = Column(String)
    description = Column(Text)


class UserExperience(Base):
    __tablename__ = "user_experiences"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    company = Column(String)
    position = Column(String)
    position_bio = Column(Text)
    updated_at = Column(TIMESTAMP)
    company_logo_key = Column(String)
    location = Column(String)


class UserInterest(Base):
    __tablename__ = "user_interests"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    interest_id = Column(Integer)
    updated_at = Column(TIMESTAMP)
