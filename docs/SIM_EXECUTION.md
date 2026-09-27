# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D2_M2_RETURN_PATH_FIXTURE_MECHANISM_PROBE_AWAIT_AUTH

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false

D2-M1 execution:
Pol-A formal solve count = 1
Pol-B formal solve count = 1
automatic retries = 0

Pol-A:
PASS_R1E1A4A_AR0_B1R_R3_D2_M1A_CHARACTERIZED
solved SHA256 004aea3571dfaa4616c3e225b01b74a9acc323496f47cf4187c9d50bc30a869e
final Delta-S 7.7989e-6, 7.2766e-6
worst S11 -0.2891 dB
worst amp imbalance 0.02760 dB
worst phase error 0.02152 deg
worst CMR -55.97 dB
worst normalized excess loss 1.2923 dB

Pol-B:
HOLD_R1E1A4A_AR0_B1R_R3_D2_M1B_QUALIFICATION
solved SHA256 8e14b35185d07d1ceb470aa98197131cfb8a06bb24bf9dc893c2fdc93186990b
final Delta-S 0.0292048, 6.5632e-6
No retry authorized.
RF values are diagnostic only.

A/B diagnostic comparison:
max abs delta S11 over 1.15..1.65 GHz = 0.02761 dB
L5 delta Zin B-A = -0.35 + j2.14 ohm
L2 delta Zin B-A = -0.53 + j1.70 ohm
L1 delta Zin B-A = -168.21 - j154.50 ohm

Interpretation:
A/B lower-stalk asymmetry is not the dominant observed problem.
Both polarizations share severe mismatch after the long lower-ground / remote common-return network is introduced.
Large delta-Z maxima occur in a near-total-reflection region and are not a robust standalone asymmetry metric.

Compared with D1R1-B local diagnostic closure, the remote manufacturable return network changes the RF response dramatically.

Next proposed stage:
AR0_B1R_R3_D2_M2_RETURN_PATH_FIXTURE_MECHANISM_PROBE

Goal:
separate local closure, long ground continuation, remote merge, and passive-fixture/loading effects before any matching sweep.

No build or solve authorized.
