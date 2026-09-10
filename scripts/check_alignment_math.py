#!/usr/bin/env python3
"""Reproduce numeric examples in the A4 alignment measurement-validity notes."""

from math import asin, atan, degrees, pi, radians, sin, sqrt, tan

PSI_TO_KPA = 6.894757293168
G = 9.81

DAKOTA_FRONT_TRACK_MM = 1594.5
DAKOTA_REAR_TRACK_MM = 1598.0
DAKOTA_WHEELBASE_MM = 3335.3


def slope_degrees(height_mm: float, span_mm: float) -> float:
    return degrees(atan(height_mm / span_mm))


def front_cross_bias_degrees(height_mm: float) -> float:
    return 2.0 * slope_degrees(height_mm, DAKOTA_FRONT_TRACK_MM)


def height_for_cross_bias_mm(cross_degrees: float) -> float:
    return DAKOTA_FRONT_TRACK_MM * tan(radians(cross_degrees / 2.0))



def rectangular_twist_mm(
    z_lf: float,
    z_rf: float,
    z_lr: float,
    z_rr: float,
) -> float:
    """Rectangular equal-track twist indicator; zero for a planar rectangle."""
    return z_lf + z_rr - z_rf - z_lr


def caster_symmetric_exact_degrees(
    c1_degrees: float,
    c2_degrees: float,
    t1_degrees: float,
    t2_degrees: float,
) -> float:
    """SAE Eq. 7 approximation after the symmetric-turn restriction."""
    numerator = sin(radians(c1_degrees)) - sin(radians(c2_degrees))
    denominator = sin(radians(t2_degrees)) - sin(radians(t1_degrees))
    return degrees(atan(numerator / denominator))


def caster_small_angle_factor(half_sweep_degrees: float) -> float:
    return (180.0 / pi) / (2.0 * half_sweep_degrees)


def caster_sine_factor(half_sweep_degrees: float) -> float:
    return 1.0 / (2.0 * sin(radians(half_sweep_degrees)))


def rhyne_stiffness_n_per_mm(
    pressure_psi: float,
    footprint_width_mm: float,
    outside_diameter_mm: float,
) -> float:
    pressure_kpa = pressure_psi * PSI_TO_KPA
    return (
        0.00028
        * pressure_kpa
        * G
        * sqrt(footprint_width_mm * outside_diameter_mm)
        + 33.84
    )


def tire_deflection_mm(
    pressure_psi: float,
    load_n: float,
    footprint_width_mm: float,
    outside_diameter_mm: float,
) -> float:
    return load_n / rhyne_stiffness_n_per_mm(
        pressure_psi,
        footprint_width_mm,
        outside_diameter_mm,
    )


def pressure_for_extra_drop_psi(
    baseline_pressure_psi: float,
    extra_drop_mm: float,
    load_n: float,
    footprint_width_mm: float,
    outside_diameter_mm: float,
) -> float:
    baseline_deflection = tire_deflection_mm(
        baseline_pressure_psi,
        load_n,
        footprint_width_mm,
        outside_diameter_mm,
    )
    target_deflection = baseline_deflection + extra_drop_mm
    target_stiffness = load_n / target_deflection

    slope_n_per_mm_per_kpa = (
        0.00028 * G * sqrt(footprint_width_mm * outside_diameter_mm)
    )
    target_pressure_kpa = (target_stiffness - 33.84) / slope_n_per_mm_per_kpa
    return target_pressure_kpa / PSI_TO_KPA


def assert_close(actual: float, expected: float, tol: float = 0.01) -> None:
    assert abs(actual - expected) <= tol, (actual, expected)


def main() -> None:
    # Surface sensitivity.
    expected_surface = {
        1.0: (0.03593, 0.07187),
        5.0: (0.17967, 0.35933),
        10.0: (0.35933, 0.71866),
        14.0: (0.50305, 1.00611),
    }
    for height_mm, (expected_slope, expected_cross) in expected_surface.items():
        slope = slope_degrees(height_mm, DAKOTA_FRONT_TRACK_MM)
        cross = front_cross_bias_degrees(height_mm)
        assert_close(slope, expected_slope, 0.0001)
        assert_close(cross, expected_cross, 0.0001)

    for cross, expected_height in {
        0.1: 1.391,
        0.5: 6.957,
        1.0: 13.915,
    }.items():
        assert_close(height_for_cross_bias_mm(cross), expected_height, 0.001)

    for height_mm, expected_pitch in {
        1.0: 0.01718,
        5.0: 0.08589,
        10.0: 0.17179,
        14.0: 0.24050,
    }.items():
        assert_close(
            slope_degrees(height_mm, DAKOTA_WHEELBASE_MM),
            expected_pitch,
            0.0001,
        )

    # A simple planar rectangle has zero twist; lifting one corner does not.
    assert_close(rectangular_twist_mm(0.0, 5.0, 10.0, 15.0), 0.0, 0.0001)
    assert_close(rectangular_twist_mm(0.0, 5.0, 10.0, 16.0), 1.0, 0.0001)

    # Surface-camber sign convention used in the notes:
    # RF higher -> positive rho -> LF raw shifts positive, RF raw shifts negative.
    rho = slope_degrees(10.0, DAKOTA_FRONT_TRACK_MM)
    assert rho > 0.0
    assert_close((+rho) - (-rho), front_cross_bias_degrees(10.0), 0.0001)

    # Caster sweep factors.
    for half_sweep, expected in {
        10.0: 2.86479,
        15.0: 1.90986,
        20.0: 1.43239,
    }.items():
        assert_close(caster_small_angle_factor(half_sweep), expected, 0.0001)

    nominal_one_turn_wheel_angle = 360.0 / 17.4
    assert_close(nominal_one_turn_wheel_angle, 20.68966, 0.0001)
    assert_close(
        caster_small_angle_factor(nominal_one_turn_wheel_angle),
        1.38465,
        0.0001,
    )

    # Verify the SAE symmetric-turn sign convention with a synthetic +4° caster.
    # For T1=-10°, T2=+10°, choose symmetric camber values that satisfy Eq. 7.
    target_caster = 4.0
    half_sweep = 10.0
    half_camber = degrees(
        asin(tan(radians(target_caster)) * sin(radians(half_sweep)))
    )
    recovered = caster_symmetric_exact_degrees(
        +half_camber,
        -half_camber,
        -half_sweep,
        +half_sweep,
    )
    assert_close(recovered, target_caster, 0.0001)
    approx = caster_small_angle_factor(half_sweep) * (2.0 * half_camber)
    assert abs(approx - target_caster) < 0.02

    # Show that the further small-angle factor differs from 1/(2 sin theta).
    assert_close(caster_sine_factor(15.0), 1.93185, 0.0001)

    # Representative tire calculation: 245/70R16, assumed 75% footprint width.
    section_width_mm = 245.0
    aspect_ratio = 0.70
    rim_diameter_mm = 16.0 * 25.4
    outside_diameter_mm = rim_diameter_mm + 2.0 * section_width_mm * aspect_ratio
    footprint_width_mm = 0.75 * section_width_mm
    load_n = 5000.0

    assert_close(outside_diameter_mm, 749.4, 0.0001)
    assert_close(
        rhyne_stiffness_n_per_mm(35.0, footprint_width_mm, outside_diameter_mm),
        279.81,
        0.01,
    )

    baseline_deflection = tire_deflection_mm(
        35.0,
        load_n,
        footprint_width_mm,
        outside_diameter_mm,
    )
    assert_close(baseline_deflection, 17.87, 0.01)

    for pressure, expected_drop in {
        30.0: 2.57,
        25.0: 5.99,
        20.0: 10.80,
    }.items():
        drop = (
            tire_deflection_mm(
                pressure,
                load_n,
                footprint_width_mm,
                outside_diameter_mm,
            )
            - baseline_deflection
        )
        assert_close(drop, expected_drop, 0.01)

    for cross, expected_deficit in {
        0.1: 2.88,
        0.5: 11.16,
        1.0: 17.43,
    }.items():
        needed_drop = height_for_cross_bias_mm(cross)
        pressure = pressure_for_extra_drop_psi(
            35.0,
            needed_drop,
            load_n,
            footprint_width_mm,
            outside_diameter_mm,
        )
        deficit = 35.0 - pressure
        assert_close(deficit, expected_deficit, 0.01)

    print("surface geometry: ok")
    print("caster sweep factors: ok")
    print("representative tire-pressure sensitivity: ok")
    print("all alignment math checks passed")


if __name__ == "__main__":
    main()
