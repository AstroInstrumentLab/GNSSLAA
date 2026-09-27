# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D2_M0R1_HUMAN_REVIEW_AWAIT_USER

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false

D2-M0:
HOLD
Reason: common-ground bridge polygon winding reversed CST extrusion normal; both bridges fully embedded in own FR4.

D2-M0R1:
PASS_R1E1A4A_AR0_B1R_R3_D2_M0R1_MANUFACTURABLE_GROUND_MERGE_BUILD_ONLY

Canonical SHA256:
4ec39ab9965dd9ec6b416d801ded0ee6e56d910d2ffc2ba405cb9dec978cd91e

Pol-A 3-port fixture SHA256:
33294aa6200264135582ec0c0742a1b4e6ca7b2148e1adece2f64388d81d3dd6

Geometry:
- T1R1 feed/head unchanged
- v=12..13 mm lower-ground taper 3.60 -> 3.20 mm
- v=13..40 mm lower rails width 3.20 mm
- A supported bridge v=33.80..34.30 mm
- B supported bridge v=34.85..35.35 mm
- bridge u=-1.40..+1.40 mm
- no via
- no reflector ground bond

Interference:
12 independent destructive-Boolean temporary-copy tests.
6/6 new copper vs own FR4 = zero positive-volume overlap.
6/6 new copper vs opposite stalk = zero positive-volume overlap.

Clearance:
rail-to-slot minimum 0.275 mm
A bridge-to-slot-end 0.25143 mm
B bridge-to-slot-end 0.25857 mm

Fresh reopen:
canonical PASS
fixture PASS
fixture ports = 3
result trees = empty

No solver was invoked.

Stop:
HUMAN 3D REVIEW + SEPARATE SOLVE AUTHORIZATION REQUIRED.
