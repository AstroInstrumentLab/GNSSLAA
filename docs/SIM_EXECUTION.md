# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D2_MANUFACTURABLE_GROUND_MERGE_AWAIT_AUTH

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false

Canonical T1R1 geometry authority:
fbf375c605acff4f53e46fedefba7acf24ef871b427a579091144b7833dd149e

Geometry correction:
- Pol-A backside ground height = -0.035 mm
- Pol-B backside ground height = +0.035 mm
- all four ground/prong volumetric intersections = 0

D1R1-A:
PASS_R1E1A4A_AR0_B1R_R3_D1R1A_CHARACTERIZED
solved SHA256 4f3cde7d98bb84ecc9294271bc6a98e230eaa678100d6e8e7bc2f4bb80d67cb4
scientific verdict NEEDS_OPTIMIZATION
worst S11 -4.003 dB
Zin decision band 124.68..158.87 + j(133.93..196.26) ohm
worst normalized excess loss 0.01737 dB

D1R1-B:
PASS_R1E1A4A_AR0_B1R_R3_D1R1B_CHARACTERIZED
solved SHA256 284453ae96f6bb3a0c2cb14e39c644547a4d66edbca119b61c9ddd27e8e8aa35
scientific verdict NEEDS_OPTIMIZATION
worst S11 -5.661 dB
Zin decision band 111.00..120.52 + j(94.22..132.49) ohm
worst amplitude imbalance 0.00198 dB
worst phase error 0.04196 deg
worst CMR -68.324 dB
worst normalized excess loss 0.01838 dB

Conclusion:
correct ground placement removes the prior strong capacitive pathology.
The corrected transition is low-loss and highly symmetric but inductive.
Downstream common-ground closure materially improves match.

Next:
design a manufacturable lower-stalk ground merge on supported FR4, then qualify it before releasing matching variables.

No sweep authorized.
