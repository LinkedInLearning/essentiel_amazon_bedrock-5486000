# Schémas d'I/O avec Pydantic pour sécuriser le passage d'états.
# ---------------------------------------------------------------------------

from pydantic import BaseModel, Field
from typing import List

class Step(BaseModel):
    name: str = Field(..., description="Nom de l'étape")
    input: dict = Field(default_factory=dict)
    output_keys: List[str] = Field(default_factory=list)

class Plan(BaseModel):
    steps: List[Step]
