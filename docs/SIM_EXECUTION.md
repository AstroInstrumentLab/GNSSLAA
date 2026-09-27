# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D1R1_CORRECTED_BUILD_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false
CONDITIONAL_SOLVE_AUTHORIZED_AFTER_BUILD_PASS: true

Prior D1:
HOLD_R1E1A4A_AR0_B1R_R3_D1_BUILD
Reason: using -0.035 mm extrusion for both polarizations corrected Pol-A but embedded Pol-B.

Verified original geometry:
Pol-A original +0.035 mm -> full ground/FR4 overlap.
Pol-B original +0.035 mm -> zero overlap.

D1R1 frozen signs:
Pol-A = -0.035 mm
Pol-B = +0.035 mm

Acceptance requires zero own-prong volumetric intersection for all four ground tapers.

If full D1R1 build PASS:
D1R1-A and D1R1-B one-shot NW solves are already authorized.
No retry.
No sweep.
