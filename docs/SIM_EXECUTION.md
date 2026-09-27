# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D1_CORRECTED_BUILD_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false
CONDITIONAL_SOLVE_AUTHORIZED_AFTER_FULL_BUILD_PASS: true

Confirmed defect:
original T1 backside grounds were 100% embedded in FR4.
Each 1.134 mm^3 ground had 1.134 mm^3 intersection with its prong.

Corrected probe:
Extrude.Height +0.035 -> -0.035 mm
ground volume unchanged
ground/prong volumetric intersection -> 0

D1 build products:
1. dual-pol T1R1 corrected canonical ground-placement artifact
2. D1-A corrected 2-port differential control
3. D1-B corrected 3-port common-ground closure control

If all build gates PASS:
one NW solve D1-A + one NW solve D1-B are already authorized.
No retry.
No sweep.
