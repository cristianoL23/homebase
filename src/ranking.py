"""Candidate ranking — intentionally incomplete.

Your job: turn applicants + ratings + written materials into a ranked list
the business owner can trust on the dashboard.

Hints from the interview prompt:
- Barista experience > other customer service / restaurant roles
- Availability should favor part-time fit
- On-the-job education signals: petty cash, keyholder, etc.
- Keyword rubric: espresso machine, drip coffee, pour over, syrups, latte art
"""

from __future__ import annotations

from .keywords import CAFE_SKILL_KEYWORDS, EXPERIENCE_HINTS
from .models import Applicant, RankedApplicant


def score_keyword_rubric(resume: str, cover_letter: str) -> float:
    """Score café skill keywords found in written materials.

    TODO: Implement keyword matching against CAFE_SKILL_KEYWORDS.
    Ideas:
    - case-insensitive search across resume + cover letter
    - partial credit for related phrases
    - normalize / return a value in a consistent range (e.g. 0–5 or 0–1)
    """
    _ = (resume, cover_letter, CAFE_SKILL_KEYWORDS)
    # Placeholder so the app runs — replace with real scoring.
    return 0.0


def score_experience(applicant: Applicant) -> float:
    """Score relevant work experience.

    TODO: Prefer previous barista experience over other CS / restaurant roles.
    You can use applicant.ratings.relevant_work_experience AND/OR scan
    resume/cover letter with EXPERIENCE_HINTS["barista"] and
    EXPERIENCE_HINTS["customer_service_or_restaurant"].
    """
    _ = (applicant, EXPERIENCE_HINTS)
    if applicant.ratings is None:
        return 0.0
    # Placeholder: returns the raw rating with no weighting logic.
    return float(applicant.ratings.relevant_work_experience)


def score_availability(applicant: Applicant) -> float:
    """Score availability fit for part-time hours.

    TODO: Favor part-time (and maybe flexible) availability.
    Combine applicant.availability_preference with ratings.availability.
    """
    if applicant.ratings is None:
        return 0.0
    # Placeholder: ignores preference enum entirely.
    return float(applicant.ratings.availability)


def score_on_the_job_education(applicant: Applicant) -> float:
    """Score on-the-job education signals (petty cash, keyholder, etc.).

    TODO: Combine ratings.on_the_job_education with keyword/hint matches
    from EXPERIENCE_HINTS["on_the_job_education"].
    """
    _ = EXPERIENCE_HINTS
    if applicant.ratings is None:
        return 0.0
    return float(applicant.ratings.on_the_job_education)


def overall_score(applicant: Applicant) -> tuple[float, dict[str, float]]:
    """Combine component scores into one overall score.

    TODO: Choose weights that match the business priorities.
    Currently a naive sum with no weighting or keyword influence.
    """
    breakdown = {
        "experience": score_experience(applicant),
        "availability": score_availability(applicant),
        "on_the_job_education": score_on_the_job_education(applicant),
        "keyword_rubric": score_keyword_rubric(
            applicant.resume, applicant.cover_letter
        ),
    }
    # Placeholder: keyword_rubric is computed but not included in the total.
    total = (
        breakdown["experience"]
        + breakdown["availability"]
        + breakdown["on_the_job_education"]
    )
    return total, breakdown


def rank_applicants(applicants: list[Applicant]) -> list[RankedApplicant]:
    """Return applicants ordered best → worst for the owner dashboard.

    TODO:
    - Sort by overall_score (desc)
    - Assign dense ranks (1, 2, 3, ...)
    - Decide how to break ties
    - Decide what to do when ratings are missing

    Current behavior: preserves input order and assigns a placeholder score.
    """
    ranked: list[RankedApplicant] = []
    for index, applicant in enumerate(applicants, start=1):
        score, breakdown = overall_score(applicant)
        ranked.append(
            RankedApplicant(
                applicant=applicant,
                score=score,
                rank=index,  # placeholder: not sorted by score yet
                breakdown=breakdown,
            )
        )
    return ranked
