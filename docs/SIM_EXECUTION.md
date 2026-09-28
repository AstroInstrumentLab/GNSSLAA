# SIM_EXECUTION

SimulationOps: 0.2.10

Current stage:
R1E1A4A_AR0_B1R_R4_A0_E1_V03_RECOVERY_BUILD_ONLY_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

PRE-REMOTE STATUS:
PASS_R4_A0_E1_PREBUILD_READY_AWAIT_BUILD_AUTH

Remote calls in R4-A0 prebuild:
0

Mainline:
- passive D1/M1 fixture S11 = diagnostic only
- Architecture B retained
- two single-ended first-stage LNAs per polarization
- QPL9547 = G0 reference, not final-production device
- active device remains outside CST
- co-simulation reference planes = QPL9547 device leads
- local package ground + vias mandatory
- remote lower-stalk-only LNA ground forbidden as baseline

A0-E1:
one-LNA landing-zone coupon only
no radiator
no second LNA
no full lower stalk
no remote ground merge
no solver

Frozen coupon:
q=-2..+2 mm
v=3..13 mm
FR4 thickness=1.00 mm
finite backside local ground

Frozen package:
Rev-D QPL9547 land pattern
3 paddle vias
5 grounded side-pin spokes to exposed paddle
pin1 Vbias remains isolated EM node
pin2 RF-IN
pin7 RF-OUT/VDD

Frozen circuit seed:
C_IN=100 pF
C_OUT=100 pF
L1=18 nH
C_RF=100 pF
R4=3.32 kOhm circuit-domain in E1

Six EM nodes:
E_UP
P_IN
P_OUT
E_DN
B_VDD
B_VBIAS

All single-ended 50-ohm normalized to finite local backside ground.
No differential port.

Static arithmetic audit:
PASS_R4_A0_E1_STATIC_PREBUILD_ARITHMETIC_AUDIT

Narrowest planned unrelated-copper clearance:
0.20 mm
downstream RF trace vs right-side decoupling lane.
If CST build fails this clearance, widen/rework the active-region stalk; do not shrink vendor/package lands.

Build source:
source/cst/R1E1A4A_AR0_B1R_R4_A0_E1_ONE_LNA_LANDING_ZONE_BUILD_ONLY_V02.mcr

V01 source:
PRE-EXECUTION SUPERSEDED
never authorized/executed.
Reason: plated-via barrel required explicit FR4 drill-hole subtraction first.

V02 plated-via rule:
0.35-mm drill
0.25-mm finished hole
FR4 hole subtracted first
annular copper barrel second

V02 static source audit:
PASS_R4_A0_E1_BUILD_SOURCE_STATIC_AUDIT_RECOVERY

Expected postbuild:
36 solids
6 ports
4 plated vias total
0 via drill-tool solids remaining
0 result tree
0 solver invocations

Deterministic runner:
scripts/run_r1e1a4a_ar0_b1r_r4_a0_e1_build_only.py

Authorized 2026-09-28 for exactly one BUILD-ONLY invocation:
fresh MWS
-> execute V02 macro once
-> save
-> fresh reopen
-> exact inventory/port/material audit
-> critical pairwise Boolean checks
-> human 3D review
-> STOP

No solve follows automatically.
SOLVE_AUTHORIZED remains false.


## 2026-09-28 formal A0-E1 build-only attempt 1

Status:
HOLD_R1E1A4A_AR0_B1R_R4_A0_E1_BUILD_ONLY

Formal build invocations consumed: 1
Solver invocations: 0
Retry authorized: false

PASS:
- 36 solids and exact component counts
- exact material identities
- four via drill tools consumed / four plated vias remain
- empty result tree
- fresh-reopen artifact hash stable

HOLD:
- expected 6 ports, observed 0 after fresh reopen
- ten pairwise Solid.Intersect audits uniformly returned CST automation error -2147418113
- zero reported intersection volumes are not accepted as PASS because the Boolean operation errored

Protected NW artifact SHA256:
f5ee6fceab2c26db5d4d63365e37abec65b87698633c577e1ca87613b86a9745

Next boundary:
R4_A0_E1_BUILD_HOLD_RECOVERY_CONTRACT_FREEZE

No rebuild/retry/solve is authorized.

## V03 recovery source freeze

Recovery freeze:
docs/R1E1A4A_AR0_B1R_R4_A0_E1_BUILD_HOLD_RECOVERY_FREEZE_V01.md

V03 source:
source/cst/R1E1A4A_AR0_B1R_R4_A0_E1_ONE_LNA_LANDING_ZONE_BUILD_ONLY_V03.mcr

Static equivalence:
PASS_R4_A0_E1_V03_STATIC_NO_GEOMETRY_REDESIGN

V03 changes only build persistence semantics: production source must enter the CST 3D History List. Geometry/material/via/pad/port coordinates remain frozen.

Next required action is a non-formal CST 2022 tooling/API probe on temporary copies. BUILD_AUTHORIZED remains false; SOLVE_AUTHORIZED remains false.

## Tooling root-cause closeout

Status:
PASS_R4_A0_E1_V03_RECOVERY_PREBUILD_READY_AWAIT_BUILD_AUTH

Confirmed:
- direct schematic.execute_vba_code Port99 fresh-reopens with PORT_COUNT=0;
- modeler.add_to_history Port99 fresh-reopens with PORT_COUNT=1 and persistent Model.mod history;
- CST 2022.5 current VBA surface does not expose Solid.DoTheseGeometricallyIntersect;
- .cst-only temporary pair copy can lose the required model state for a history-less artifact;
- complete project copy restores the target solid and makes Solid.Intersect return Err.Number=0 for the known zero-overlap test.

Recovery freeze:
docs/R1E1A4A_AR0_B1R_R4_A0_E1_BUILD_HOLD_RECOVERY_FREEZE_V02.md

Recovery runner:
scripts/run_r1e1a4a_ar0_b1r_r4_a0_e1_v03_recovery_build.py

BUILD_AUTHORIZED remains false.
SOLVE_AUTHORIZED remains false.
Next boundary is a new one-shot V03 recovery BUILD-ONLY authorization.


## V03 recovery build authorization — 2026-09-28

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false
Formal build budget: 1
Solver launch budget: 0
Silent retry: forbidden
Stop after persistent-history build + fresh reopen + port/history/intersection audit.
