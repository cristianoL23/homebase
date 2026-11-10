from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AvailabilityPreference(str, Enum):
    PART_TIME = "part_time"
    FULL_TIME = "full_time"
    FLEXIBLE = "flexible"
    UNKNOWN = "unknown"


class Ratings(BaseModel):
    """Manual 1–5 ratings for the three interview rubric areas."""

    relevant_work_experience: int = Field(ge=1, le=5)
    availability: int = Field(ge=1, le=5)
    on_the_job_education: int = Field(ge=1, le=5)


class Applicant(BaseModel):
    id: str
    name: str
    email: str
    resume: str
    cover_letter: str
    availability_preference: AvailabilityPreference = AvailabilityPreference.UNKNOWN
    ratings: Optional[Ratings] = None
    # Populated by the ranking module once you implement it
    score: Optional[float] = None
    rank: Optional[int] = None
    score_breakdown: Optional[dict[str, float]] = None


class ApplicantCreate(BaseModel):
    name: str
    email: str
    resume: str
    cover_letter: str
    availability_preference: AvailabilityPreference = AvailabilityPreference.UNKNOWN
    ratings: Optional[Ratings] = None


class RankedApplicant(BaseModel):
    applicant: Applicant
    score: float
    rank: int
    breakdown: dict[str, float] = Field(default_factory=dict)
