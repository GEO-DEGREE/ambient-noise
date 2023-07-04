from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime
from pydantic import BaseModel, PositiveInt

from .processing_config import PreProcessingModel
from .station import Station

if TYPE_CHECKING:
    import numpy as np


class Correlograms(BaseModel):
    '''Describes a time-timelag constelation of correlograms'''

    start_time: datetime
    end_time: datetime

    station_1: Station
    stations_2: Station

    n_traces: PositiveInt

    pre_processing: PreProcessingModel

    def get_data(self) -> np.ndarray:
        # Load on-demand from zarr file
        ...


class StackedCorrelogram(BaseModel):
    '''Describes a single stacked correlogram'''

    start_time: datetime
    end_time: datetime

    station_1: Station
    stations_2: Station

    n_traces: PositiveInt

    pre_processing: PreProcessingModel
