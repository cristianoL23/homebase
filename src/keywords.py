"""Café skill keywords used by the LLM-style ranking rubric.

Feel free to expand this list as you refine the ranking logic.
"""

CAFE_SKILL_KEYWORDS: list[str] = [
    "espresso machine",
    "drip coffee",
    "pour over",
    "syrups",
    "latte art",
]

# Experience / ops signals that may appear in resumes or cover letters.
# These are hints for your scoring logic — not wired up yet.
EXPERIENCE_HINTS: dict[str, list[str]] = {
    "barista": [
        "barista",
        "baristas",
        "coffee shop",
        "café",
        "cafe",
        "espresso",
    ],
    "customer_service_or_restaurant": [
        "customer service",
        "server",
        "waitress",
        "waiter",
        "host",
        "hostess",
        "restaurant",
        "retail",
        "cashier",
    ],
    "on_the_job_education": [
        "petty cash",
        "keyholder",
        "key holder",
        "opening",
        "closing",
        "shift lead",
        "training",
        "pos",
        "point of sale",
    ],
}
