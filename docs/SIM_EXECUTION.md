# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_T2F_R1_FLATTENED_FIXTURE_BUILD_ONLY_AWAIT_AUTH

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
CST251_AUTHORIZED: false

T2S final:
HOLD_R1E1A4A_AR0_B1R_T2S_LINUX_HISTORY_REPLAY

Formal CST launches: 1
Solver_HF_Tet kernel starts: 0
Automatic retries: 0
S-parameters produced: no

Root cause:
CST251 Linux headless replayed inherited legacy project history and failed at historical Transform.AutoDestination with ActiveX Automation error 10091 before the HF tetrahedral solver started.

This is not an RF result.

Required next node:
T2F-R1 fresh/history-independent flattened fixture BUILD-ONLY, with six-solid + three-port equivalence audit to accepted T2F.

Evidence:
evidence/r1e1a4a_ar0_b1r_t2s_251_20260927_run01/

Remote HOLD root:
 /data/jlding/gnss_ar0_b1r_t2s_20260927

Stop:
AWAIT EXPLICIT T2F-R1 BUILD-ONLY AUTHORIZATION.
