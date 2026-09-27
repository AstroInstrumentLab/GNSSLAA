# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D2_M0R1_BUILD_ONLY_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false

M0 HOLD:
lower rails correct, but both 0.049-mm^3 common-ground bridges were fully embedded in own FR4.

Root cause:
bridge polygon winding opposite to validated rail polygon winding.

M0R1:
fresh build from T1R1.
All geometry dimensions unchanged.
Only A/B bridge polygon point order is reversed to restore outward backside extrusion.

Qualification:
12 independent temporary-copy Boolean pairs:
6 D2 copper vs own FR4
6 D2 copper vs opposite stalk
All 12 must have zero positive-volume overlap.

No solve.
No sweep.
