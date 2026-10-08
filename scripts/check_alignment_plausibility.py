#!/usr/bin/env python3
"""Regression checks for alignment result-integrity guardrails."""

from dataclasses import dataclass
from enum import Enum
from math import atan, degrees, isfinite, radians, sin


DAKOTA_CAM_ADJUSTMENT_SCALE_DEG = 2.0
DAKOTA_ABSURD_CASTER_TRIPWIRE_DEG = 45.0


class ResultState(str, Enum):
    IN_SPEC = "IN-SPEC"
    OUT_OF_SPEC_BELIEVABLE = "OUT-OF-SPEC / BELIEVABLE"
    SUSPECT = "SUSPECT"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class SweepRecord:
    wheel: str
    c1_deg: float
    c2_deg: float
    t1_deg: float
    t2_deg: float
    road_wheel_angles_measured: bool
    declared_direction_order_ok: bool = True
    prescribed_half_sweep_deg: float | None = None
    allowed_turn_error_deg: float | None = None
    symmetry_tolerance_deg: float | None = None


@dataclass(frozen=True)
class GatedCaster:
    caster_deg: float | None
    state: ResultState
    reason: str


def caster_symmetric_exact_deg(c1_deg: float, c2_deg: float, t1_deg: float, t2_deg: float) -> float:
    numerator = sin(radians(c1_deg)) - sin(radians(c2_deg))
    denominator = sin(radians(t2_deg)) - sin(radians(t1_deg))
    if denominator == 0.0:
        raise ValueError("zero caster sweep")
    return degrees(atan(numerator / denominator))


def outside_distance(value: float, low: float, high: float) -> float:
    if low <= value <= high:
        return 0.0
    if value < low:
        return low - value
    return value - high


def validate_sweep(record: SweepRecord) -> str | None:
    values = (record.c1_deg, record.c2_deg, record.t1_deg, record.t2_deg)
    if not all(isfinite(value) for value in values):
        return "non-finite raw input"
    if record.wheel not in {"LF", "RF"}:
        return "wheel must be LF or RF"
    if not record.road_wheel_angles_measured:
        return "actual individual road-wheel angles were not measured"
    if not record.declared_direction_order_ok:
        return "sweep direction/position labels do not match the declared formula convention"
    if not (record.t1_deg < 0.0 < record.t2_deg):
        return "caster sweep must straddle the declared zero/reference"
    if record.symmetry_tolerance_deg is None:
        return "measurement method supplied no sweep-symmetry tolerance"
    if record.symmetry_tolerance_deg < 0.0:
        return "sweep-symmetry tolerance cannot be negative"
    if abs(abs(record.t1_deg) - abs(record.t2_deg)) > record.symmetry_tolerance_deg:
        return "caster sweep does not meet the measurement method symmetry tolerance"
    if record.prescribed_half_sweep_deg is not None:
        tolerance = record.allowed_turn_error_deg
        if tolerance is None:
            return "instrument sweep target supplied without an allowed turn error"
        for actual in (abs(record.t1_deg), abs(record.t2_deg)):
            if abs(actual - record.prescribed_half_sweep_deg) > tolerance:
                return "actual road-wheel sweep does not meet the instrument procedure"
    return None


def gate_dakota_caster(
    record: SweepRecord,
    *,
    spec_low_deg: float | None,
    spec_high_deg: float | None,
) -> GatedCaster:
    problem = validate_sweep(record)
    if problem:
        return GatedCaster(None, ResultState.INVALID, problem)

    caster = caster_symmetric_exact_deg(
        record.c1_deg,
        record.c2_deg,
        record.t1_deg,
        record.t2_deg,
    )

    if abs(caster) >= DAKOTA_ABSURD_CASTER_TRIPWIRE_DEG:
        return GatedCaster(
            caster,
            ResultState.INVALID,
            "caster trips the 45 degree Dakota data-integrity stop",
        )

    if spec_low_deg is None or spec_high_deg is None:
        return GatedCaster(
            caster,
            ResultState.UNKNOWN,
            "exact vehicle-specific service envelope not verified",
        )
    if spec_low_deg > spec_high_deg:
        return GatedCaster(None, ResultState.INVALID, "service envelope is reversed")

    distance = outside_distance(caster, spec_low_deg, spec_high_deg)
    if distance == 0.0:
        return GatedCaster(caster, ResultState.IN_SPEC, "inside supplied verified service envelope")
    if distance <= DAKOTA_CAM_ADJUSTMENT_SCALE_DEG:
        return GatedCaster(
            caster,
            ResultState.OUT_OF_SPEC_BELIEVABLE,
            "outside service envelope but within one ordinary Dakota cam adjustment scale",
        )
    return GatedCaster(
        caster,
        ResultState.SUSPECT,
        "more than one ordinary Dakota cam adjustment scale beyond the service envelope",
    )


def assert_close(actual: float | None, expected: float, tolerance: float = 0.01) -> None:
    assert actual is not None
    assert abs(actual - expected) <= tolerance, (actual, expected)


def fixture_record(c1: float, c2: float) -> SweepRecord:
    return SweepRecord(
        wheel="LF",
        c1_deg=c1,
        c2_deg=c2,
        t1_deg=-15.0,
        t2_deg=15.0,
        road_wheel_angles_measured=True,
        prescribed_half_sweep_deg=15.0,
        allowed_turn_error_deg=0.25,
        symmetry_tolerance_deg=0.25,  # synthetic fixture tolerance, not a universal rule
    )


def main() -> None:
    # Synthetic envelope used only to test state transitions. It is NOT a Dakota spec.
    test_spec_low = 3.0
    test_spec_high = 4.0

    normal = gate_dakota_caster(
        fixture_record(+0.5, -1.3),
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert_close(normal.caster_deg, 3.47285)
    assert normal.state == ResultState.IN_SPEC

    # Regression: +0.5 copied as +5.0 yields nearly +12 degrees. Arithmetic is valid;
    # plausibility must stop the pipeline and force a return to the raw observation.
    decimal_error = gate_dakota_caster(
        fixture_record(+5.0, -1.3),
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert_close(decimal_error.caster_deg, 11.98048)
    assert decimal_error.state == ResultState.SUSPECT

    sign_error = gate_dakota_caster(
        fixture_record(-0.5, +1.3),
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert_close(sign_error.caster_deg, -3.47285)
    assert sign_error.state == ResultState.SUSPECT

    direction_swap = SweepRecord(
        wheel="LF",
        c1_deg=+0.5,
        c2_deg=-1.3,
        t1_deg=+15.0,
        t2_deg=-15.0,
        road_wheel_angles_measured=True,
        declared_direction_order_ok=False,
        prescribed_half_sweep_deg=15.0,
        allowed_turn_error_deg=0.25,
        symmetry_tolerance_deg=0.25,
    )
    swapped = gate_dakota_caster(
        direction_swap,
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert swapped.caster_deg is None
    assert swapped.state == ResultState.INVALID

    assumed_ratio = SweepRecord(
        wheel="LF",
        c1_deg=+0.5,
        c2_deg=-1.3,
        t1_deg=-(360.0 / 17.4),
        t2_deg=+(360.0 / 17.4),
        road_wheel_angles_measured=False,
    )
    ratio_result = gate_dakota_caster(
        assumed_ratio,
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert ratio_result.caster_deg is None
    assert ratio_result.state == ResultState.INVALID

    wrong_sweep = SweepRecord(
        wheel="LF",
        c1_deg=+0.5,
        c2_deg=-1.3,
        t1_deg=-14.0,
        t2_deg=+14.0,
        road_wheel_angles_measured=True,
        prescribed_half_sweep_deg=15.0,
        allowed_turn_error_deg=0.25,
        symmetry_tolerance_deg=0.25,
    )
    wrong_sweep_result = gate_dakota_caster(
        wrong_sweep,
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert wrong_sweep_result.state == ResultState.INVALID

    absurd = gate_dakota_caster(
        fixture_record(+20.0, -20.0),
        spec_low_deg=test_spec_low,
        spec_high_deg=test_spec_high,
    )
    assert_close(absurd.caster_deg, 52.88389)
    assert absurd.state == ResultState.INVALID

    no_spec = gate_dakota_caster(
        fixture_record(+0.5, -1.3),
        spec_low_deg=None,
        spec_high_deg=None,
    )
    assert no_spec.state == ResultState.UNKNOWN

    print("normal caster regression: ok")
    print("decimal/sign/direction regressions: ok")
    print("unmeasured/wrong sweep regressions: ok")
    print("absurd-result tripwire: ok")
    print("missing-spec stop: ok")
    print("all alignment plausibility checks passed")


if __name__ == "__main__":
    main()
