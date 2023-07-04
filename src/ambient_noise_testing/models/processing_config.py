from __future__ import annotations
from typing import Literal

from pydantic import BaseModel, PositiveFloat, PositiveInt, confloat

StackingMethod = Literal["linear", "phase-weighted-stack"]
NormalizationMethod = Literal["none", "one-bit", "mute-median"]
CrossCorrelationMethod = Literal["cross-correlate", "phase-cross-correlate"]


class PreProcessingModel(BaseModel):
    downsample_frequency: PositiveFloat = 50.0

    window_length_seconds: PositiveFloat = 150.0
    window_overlap_seconds: confloat(ge=0.0, le=1.0) = 0.0

    max_lag_time: PositiveFloat = 15.0

    # Pre-Processing
    apply_spectral_whitening: bool = False
    normalization: NormalizationMethod = "one-bit"
    correlation_method: CrossCorrelationMethod = "phase-cross-correlate"

    # Pre-Bandpass filter
    freq_min: PositiveFloat = 4.0
    freq_max: PositiveFloat = 6.0

    processing_software: str = 'kiel//gfz//SeisNoise.jl'


class StackProcessingModel(BaseModel):
    # Post Processing
    stacking_method: StackingMethod = "linear"
    trace_rms_weighting: bool = False
    normalize_stack: bool = True

    # Frequency filter
    freq_min: float = 0.0
    freq_max: float = 6.0
