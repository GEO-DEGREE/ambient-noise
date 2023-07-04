from __future__ import annotations

from pydantic import BaseModel


class Station(BaseModel):
    network: str
    station: str
    location: str

    latitude: float
    longitude: float
    elevation: float
