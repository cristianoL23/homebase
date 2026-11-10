"""Smoke tests for the unfinished ranking module.

These assert current placeholder behavior so the scaffold stays runnable.
Replace / expand them as you implement real ranking.
"""

from src.models import Applicant, AvailabilityPreference, Ratings
from src.ranking import overall_score, rank_applicants, score_keyword_rubric


def _sample(name: str = "Test Candidate") -> Applicant:
    return Applicant(
        id="t1",
        name=name,
        email="test@example.com",
        resume="Worked espresso machine and latte art at a café.",
        cover_letter="Looking for part-time hours.",
        availability_preference=AvailabilityPreference.PART_TIME,
        ratings=Ratings(
            relevant_work_experience=5,
            availability=4,
            on_the_job_education=3,
        ),
    )


def test_keyword_rubric_is_placeholder():
    score = score_keyword_rubric(
        "espresso machine, drip coffee, pour over, syrups, latte art",
        "I love coffee",
    )
    assert score == 0.0


def test_overall_score_ignores_keywords_for_now():
    total, breakdown = overall_score(_sample())
    assert breakdown["keyword_rubric"] == 0.0
    assert total == 5 + 4 + 3


def test_rank_applicants_preserves_input_order():
    first = _sample("First")
    second = _sample("Second")
    second.ratings = Ratings(
        relevant_work_experience=1,
        availability=1,
        on_the_job_education=1,
    )
    ranked = rank_applicants([first, second])
    assert [item.applicant.name for item in ranked] == ["First", "Second"]
    assert [item.rank for item in ranked] == [1, 2]
