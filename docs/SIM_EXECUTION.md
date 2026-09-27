# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D0_DIAGNOSTIC_FIXTURE_REVIEW_AWAIT_USER

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false

R3-D0:
PASS_R1E1A4A_AR0_B1R_R3_D0_DIAGNOSTIC_FIXTURES_BUILD_ONLY

Formal fixture builds: 2
Solver invocations: 0

D0-A:
- exact T1 six-solid transition
- 2 ports
- P1 100-ohm differential at v=0
- P2 100-ohm differential at v=10 mm
- grounds remain passive and electrically separate
- SHA256 f983eb43a3450c511387073a760e946bf60c16d8df1424d26692c8db7d9e3863

D0-B:
- exact T1 six solids + one diagnostic copper bridge
- 3 ports using corrected R2 conductor-interface endpoints
- bridge u=-1.2..+1.2 mm, n=-1.035..-1.0 mm, v=11..12 mm
- bridge volume 0.084 mm^3
- SHA256 66f7b9d1b0f4c8ba6b36a5e25f271dcec88c1f7f4efc38e13973175ca62cfd32

All fresh-reopen geometry/port audits passed.
No result tree exists in either fixture.

Purpose:
D0-A tests differential/odd-mode behavior without single-ended ground-reference assumptions.
D0-B tests whether explicit downstream G+/G- closure removes the severe capacitive input mismatch.

The D0-B bridge is diagnostic only and is not product geometry.

Stop:
AWAIT FIXTURE REVIEW AND SEPARATE SOLVE AUTHORIZATION.
