from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .models import ApplicantCreate, AvailabilityPreference, Ratings
from .ranking import rank_applicants
from .storage import add_applicant, get_applicant, load_applicants

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI(
    title="Homebase Interview Prep — Candidate Ranking",
    description="Starter scaffold for coffee shop candidate ranking.",
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request) -> HTMLResponse:
    applicants = load_applicants()
    ranked = rank_applicants(applicants)
    return TEMPLATES.TemplateResponse(
        request,
        "dashboard.html",
        {"ranked": ranked},
    )


@app.get("/apply", response_class=HTMLResponse)
def apply_form(request: Request) -> HTMLResponse:
    return TEMPLATES.TemplateResponse(request, "apply.html", {})


@app.post("/apply")
def submit_application(
    name: str = Form(...),
    email: str = Form(...),
    resume: str = Form(...),
    cover_letter: str = Form(...),
    availability_preference: str = Form("unknown"),
    relevant_work_experience: int | None = Form(None),
    availability: int | None = Form(None),
    on_the_job_education: int | None = Form(None),
) -> RedirectResponse:
    ratings = None
    if (
        relevant_work_experience is not None
        and availability is not None
        and on_the_job_education is not None
    ):
        ratings = Ratings(
            relevant_work_experience=relevant_work_experience,
            availability=availability,
            on_the_job_education=on_the_job_education,
        )

    payload = ApplicantCreate(
        name=name.strip(),
        email=email.strip(),
        resume=resume.strip(),
        cover_letter=cover_letter.strip(),
        availability_preference=AvailabilityPreference(availability_preference),
        ratings=ratings,
    )
    add_applicant(payload)
    return RedirectResponse(url="/", status_code=303)


@app.get("/api/applicants")
def api_list_applicants():
    return load_applicants()


@app.get("/api/rankings")
def api_rankings():
    return rank_applicants(load_applicants())


@app.get("/api/applicants/{applicant_id}")
def api_get_applicant(applicant_id: str):
    applicant = get_applicant(applicant_id)
    if applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant


@app.post("/api/applicants")
def api_create_applicant(payload: ApplicantCreate):
    return add_applicant(payload)
