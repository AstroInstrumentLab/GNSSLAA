# SIM_EXECUTION

SimulationOps: 0.2.10

Current stage:
R1E1A4A_AR0_B1R_R4_A0_E2_INTEGRATED_ANTENNA_EM_CONTRACT_FREEZE

BUILD_AUTHORIZED: false
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


## V03 formal recovery build result

Automated status:
PASS_R1E1A4A_AR0_B1R_R4_A0_E1_V03_BUILD_ONLY

Artifact SHA256:
a0e4bda5c64ea712564db76441721ca6dc147c97c061360a16a7d21f272f787a

PASS:
- persistent model history
- exact 36 solids/materials
- six persistent 50-ohm ports with frozen coordinates
- four plated vias / drill tools consumed
- CDCheckModelIntersections returned
- 10/10 forbidden pairwise positive-volume overlaps = 0
- empty result tree
- fresh-reopen hash stable
- solver invocations = 0

BUILD authorization consumed and closed.
SOLVE_AUTHORIZED remains false.
Next gate: human 3D review using docs/R1E1A4A_AR0_B1R_R4_A0_E1_V03_HUMAN_3D_REVIEW_20260928.md.


## V03 human geometry review result

Status:
PASS_R4_A0_E1_V03_HUMAN_3D_REVIEW

Scope:
visual geometry / assembly sanity only.

Reviewer noted limited RF-layout expertise, therefore this PASS does not qualify RF performance, impedance, passive loss, local-ground RF quality, coupling, or stability.

A0-E1 build/human-geometry stage is closed PASS.

Next stage:
R1E1A4A_AR0_B1R_R4_A0_E1_PASSIVE_EM_SOLVE_CONTRACT_FREEZE

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
No solver invocation follows automatically.


## E1-S0 passive EM solve contract freeze

Status:
PASS_R4_A0_E1_PASSIVE_EM_PRESOLVE_FREEZE_READY_AWAIT_SOLVE_AUTH

Freeze:
docs/R1E1A4A_AR0_B1R_R4_A0_E1_PASSIVE_EM_SOLVE_FREEZE_V01.md

Protected V03 source SHA256:
a0e4bda5c64ea712564db76441721ca6dc147c97c061360a16a7d21f272f787a

Solver config:
source/cst/R1E1A4A_AR0_B1R_R4_A0_E1_PASSIVE_EM_SOLVER_CONFIG_V01.mcr
blob 14554ad16fb7cb982ed7d9c03d0dc662bb4dec88

Runner:
scripts/run_r1e1a4a_ar0_b1r_r4_a0_e1_passive_em_solve.py
blob 81379f68d79d229b713edd2ee2d06b3cec1853f4

Route:
NW only for this stage.
Complete-project copy of protected V03 source.
One formal solver invocation.
Zero automatic retries.

Hard gates:
- final two DeltaS <= 0.02
- complete common-run 6x6 S matrix
- max |Sij-Sji| <= 0.02
- max sum_i |Sij|^2 <= 1.02
- no fatal solver error
- no mesh corruption

Interpretation:
S11 is diagnostic only.
E_UP-to-E_DN transmission is not final insertion loss because C_IN/QPL9547/C_OUT/L1 remain circuit-domain gaps.
Unintended coupling > -20 dB is a review sentinel, not a hard physics FAIL.

If hard gates PASS with no coupling review:
next = A0-E2 integrated antenna EM contract freeze.

If hard gates PASS with coupling review:
next = narrow E1-M1 field/current/loss mechanism probe.

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

No remote calls were used for this contract freeze.


## E1-S0 solve authorization — 2026-09-28

SOLVE_AUTHORIZED: true
BUILD_AUTHORIZED: false
Formal solver budget: 1
Automatic retry budget: 0
Solve host: NW
Stop after read-only six-port qualification; no retry.


## E1-S0 post-human provenance rebaseline

Pre-solve source hash drift was detected before any solver invocation.
Dedicated identity audit PASSed: exact 36 solids/materials, exact six ports/coordinates, persistent V03 History, empty result tree, stable current hash.

Build-pass SHA256:
a0e4bda5c64ea712564db76441721ca6dc147c97c061360a16a7d21f272f787a

Canonical post-human source SHA256:
aee6bc30085c002b6063de80f110096f6b62911bf897007d133b309e5a962b36

Classification: provenance-only rebaseline; no scientific model or solve-gate change.
Formal solver budget remains 0/1 consumed.
SOLVE_AUTHORIZED remains true for exactly one E1-S0 solve.


## E1-S0 passive EM solve result

Status:
PASS_R1E1A4A_AR0_B1R_R4_A0_E1_PASSIVE_EM_CHARACTERIZED

Disposition:
PASS_CHARACTERIZED_NETWORK_CLEAN_SENTINELS

Formal solver invocations: 1
Automatic retries: 0

Solved artifact SHA256:
bd487a52e342284fe7cdf4b6a35c0a7fc23296e97560f9603451bbf6f0b6349c

Native CST mesh-adaptation authority:
- pass 3 DeltaS = 0.00772936
- pass 4 DeltaS = 0.00465735
- CST terminated adaptation because desired accuracy was reached

Network integrity:
- complete 6x6 network: PASS
- native frequency grid: 1001 points, 1.0–1.8 GHz
- max |Sij-Sji| = 4.233e-7: PASS
- max sum_i |Sij|^2 = 0.999045: PASS
- fatal solver error: false
- mesh corruption: false

Coupling:
- strongest P_IN/P_OUT bypass = -68.99 dB
- E_UP/E_DN bypass = -49.44 dB
- no unintended coupling exceeded -20 dB
- no E1-M1 mechanism probe required

Native warning:
large input reflection at 1.8 GHz.
This is interpretation-only because the passive EM coupon intentionally leaves C_IN/QPL9547/C_OUT/L1 in the circuit domain. It is not product input-match authority.

The cst.results convergence series is retained as secondary evidence; native output.txt is the primary mesh-adaptation authority because the two representations are numerically different though both independently pass the 0.02 threshold.

SOLVE_AUTHORIZED: false
BUILD_AUTHORIZED: false

Next:
R1E1A4A_AR0_B1R_R4_A0_E2_INTEGRATED_ANTENNA_EM_CONTRACT_FREEZE


## SimulationOps sync after E1-S0

Next-stage minimum: SimulationOps 0.2.11.
New global rules captured from E1-S0: post-human/GUI CST source-hash integrity and native-vs-result-tree convergence authority.
