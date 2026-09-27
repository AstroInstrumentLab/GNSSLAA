# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D0_DIAGNOSTIC_FIXTURES_BUILD_ONLY_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false

Purpose:
diagnose whether T2S-R2 capacitive mismatch is a transition problem or a separated-ground return-path fixture problem.

D0-A:
exact T1 six-solid Pol-A transition.
2 x 100-ohm differential ports at v=0 and v=10 mm.
Ground rails remain passive and separate.

D0-B:
exact T1 six solids plus diagnostic backside copper bridge.
3-port R2 topology retained.
Bridge:
u=-1.2..+1.2 mm
n=-1.035..-1.0 mm
v=11..12 mm
diagnostic only; not product geometry.

Parent T1 SHA256:
3144672323cbd4123d6413e7d9ae8f4842b78707d3a71b641748c7250ca2a8f6

No solver.
Stop after D0-A/B build qualification and review.
