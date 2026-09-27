# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_T2F_R2_OUTPUT_PORT_ENDPOINT_FIX_BUILD_ONLY_AWAIT_AUTH

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
CST251_AUTHORIZED: false

T2S NW final:
HOLD_R1E1A4A_AR0_B1R_T2S_NW_OUTPUT_PORT_MESH_CORRUPTION

Formal NW solver invocations: 1
Automatic retries: 0
HF solver started: yes
Adaptive pass reached: 1
S-parameters produced: no

Root cause:
Ports 2/3 discrete-port lines used the outer surfaces of the finite-thickness signal and backside-ground copper. CST warned that their endpoint(s) were not connected to a good conductor and aborted adaptive pass 1 with a corrupted-mesh error near lumped element 2.

Required port-only recovery:
P1 unchanged.
P2/P3 signal endpoint n: +0.035 -> 0.0 mm.
P2/P3 ground endpoint n: -1.035 -> -1.0 mm.
The corrected port line spans FR4 only.

No T1 geometry change is required.

Evidence:
evidence/r1e1a4a_ar0_b1r_t2s_nw_20260927_solve01/

Stop:
AWAIT EXPLICIT T2F-R2 PORT-ENDPOINT BUILD-ONLY AUTHORIZATION.
