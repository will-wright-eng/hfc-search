from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
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
    cid: Optional[int]
    last_seen: Optional[str]
    score: Optional[float]


# Add other schemas similarly...
