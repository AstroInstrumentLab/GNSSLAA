# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_T2F_HUMAN_FIXTURE_REVIEW_AWAIT_USER

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false

AR0-B1R-T2F status:
PASS_R1E1A4A_AR0_B1R_T2F_FIXTURE_BUILD_ONLY

Formal fixture-build invocations total: 1
Solver invocations total: 0

The original fixture itself passed geometry and port audits.
The original HOLD was caused only by CST 2022 delaying derived parameter t2f_output_z in the immediate-build parameter enumeration.
Audit-only recovery used the existing artifact; no rebuild occurred.

Fixture:
- 6 exact retained T1 solids
- 3 ports after build and fresh reopen
- P1 100-ohm balanced input
- P2/P3 50-ohm grounded outputs

Evidence:
evidence/r1e1a4a_ar0_b1r_t2f_nw_20260927_build01/

Stop boundary:
Await human fixture review. No solve.
