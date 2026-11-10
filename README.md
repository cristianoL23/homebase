# Homebase Interview Prep — Candidate Ranking Starter

Starter codebase for a **coffee shop** hiring ranking system. The framework is wired up end-to-end so you can run the app and explore sample data, but the **core ranking logic is intentionally incomplete** for you to finish.

## Problem

Build a ranking system that recommends the best candidates for an open barista / café role to the business owner.

Applicants submit a **resume** and **cover letter** through an online portal. Each applicant can be rated **1–5** in:

| Area | Guidance |
|------|----------|
| **Relevant work experience** | Previous barista experience is most valuable; other customer service / restaurant roles are next |
| **Availability** | Part-time hours |
| **On-the-job education** | Petty cash, keyholder, etc. |

The business owner should see a **dashboard of top candidates** to review.

An LLM-style rubric may also consider café skill keywords in written materials, for example:

- espresso machine
- drip coffee
- pour over
- syrups
- latte art

## What's already in place

- Applicant data model + sample applicants (`data/applicants.json`)
- Keyword list for the rubric (`src/keywords.py`)
- Stub ranking module with clear `TODO`s (`src/ranking.py`)
- FastAPI app with:
  - Applicant submission portal (API + simple form)
  - Owner dashboard that lists candidates (currently unsorted / incomplete scores)
- Minimal HTML UI under `static/`

## What you should implement

Open `src/ranking.py` and complete:

1. **Experience scoring** — weight barista history highest, then CS / restaurant
2. **Availability scoring** — favor part-time fit
3. **On-the-job education scoring** — petty cash, keyholder, similar signals
4. **Keyword / rubric score** — detect skill keywords in resume + cover letter
5. **Overall rank** — combine ratings + rubric into a ranked list for the dashboard

Suggested stretch goals:

- Configurable weights
- Explainability (why was this candidate ranked #1?)
- Deduplicating / normalizing keyword matches
- Unit tests under `tests/`

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.app:app --reload
```

Then open:

- Owner dashboard: http://127.0.0.1:8000/
- Apply portal: http://127.0.0.1:8000/apply

## Project layout

```
data/applicants.json   # sample applicants (edit freely)
src/
  models.py            # Pydantic models
  keywords.py          # café skill keywords
  ranking.py           # ← main work happens here
  storage.py           # load / save applicants
  app.py               # FastAPI routes
static/                # dashboard + apply form
tests/                 # add your tests here
```

## Notes

This is a **practice scaffold**, not a production hiring tool. Ranking quality, fairness, and compliance considerations are out of scope for the exercise unless you choose to explore them.
