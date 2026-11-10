from __future__ import annotations

import json
import uuid
from pathlib import Path

from .models import Applicant, ApplicantCreate

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "applicants.json"


def _ensure_data_file() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        DATA_PATH.write_text("[]\n", encoding="utf-8")


def load_applicants() -> list[Applicant]:
    _ensure_data_file()
    raw = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    return [Applicant.model_validate(item) for item in raw]


def save_applicants(applicants: list[Applicant]) -> None:
    _ensure_data_file()
    payload = [a.model_dump(mode="json") for a in applicants]
    DATA_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def add_applicant(payload: ApplicantCreate) -> Applicant:
    applicants = load_applicants()
    applicant = Applicant(id=str(uuid.uuid4()), **payload.model_dump())
    applicants.append(applicant)
    save_applicants(applicants)
    return applicant


def get_applicant(applicant_id: str) -> Applicant | None:
    for applicant in load_applicants():
        if applicant.id == applicant_id:
            return applicant
    return None
