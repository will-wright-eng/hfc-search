from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    fname: Optional[str]
    pnoun: Optional[str]
    phone_num: Optional[str]
    location: Optional[str]
    user_type: Optional[str]
    public: Optional[bool]
    profile_bio: Optional[str]
    onboarded: Optional[bool]
    createdAt: Optional[str]
    updated_at: Optional[str]
    last_seen: Optional[str]
    score: Optional[float]
    cid: Optional[int]


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class InterestBase(BaseModel):
    interest_label: Optional[str]
    category_id: Optional[int]
    is_custom: Optional[bool]


class InterestCreate(InterestBase):
    pass


class Interest(InterestBase):
    id: int

    class Config:
        from_attributes = True


class SubjectBase(BaseModel):
    subject: Optional[str]
    is_custom: Optional[bool]


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: int

    class Config:
        from_attributes = True


class SchoolBase(BaseModel):
    school_name: Optional[str]
    school_img_url: Optional[str]
    is_custom: Optional[bool]


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    id: int

    class Config:
        from_attributes = True


class UserEducationBase(BaseModel):
    uid: Optional[int]
    school_id: Optional[int]
    major: Optional[int]
    minor: Optional[int]
    graduated_year: Optional[int]
    expected_grad_year: Optional[int]
    updated_at: Optional[datetime]
    location: Optional[str]
    description: Optional[str]


class UserEducationCreate(UserEducationBase):
    pass


class UserEducation(UserEducationBase):
    id: int

    class Config:
        from_attributes = True


class UserExperienceBase(BaseModel):
    uid: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    company: Optional[str]
    position: Optional[str]
    position_bio: Optional[str]
    updated_at: Optional[datetime]
    company_logo_key: Optional[str]
    location: Optional[str]


class UserExperienceCreate(UserExperienceBase):
    pass


class UserExperience(UserExperienceBase):
    id: int

    class Config:
        from_attributes = True


class UserInterestBase(BaseModel):
    uid: Optional[int]
    interest_id: Optional[int]
    updated_at: Optional[datetime]


class UserInterestCreate(UserInterestBase):
    pass


class UserInterest(UserInterestBase):
    id: int

    class Config:
        from_attributes = True
