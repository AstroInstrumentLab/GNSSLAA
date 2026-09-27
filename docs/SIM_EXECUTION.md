# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R4_A0_E1_STATIC_PREBUILD_AUDIT_AND_BUILD_PACKET_FREEZE

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

Pre-remote A0-E1 contracts now frozen:
- Rev-D QPL9547 footprint
- G0 three-via paddle-ground seed
- branch-local G-L0 ground baseline
- bias/DC-block topology
- dimensioned one-LNA coupon placement
- FR4/copper/material baseline
- geometry/interference predicates
- six-node EM/circuit port contract

Six nodes:
E_UP
P_IN
P_OUT
E_DN
B_VDD
B_VBIAS

QPL9547 S2P connects P_IN <-> P_OUT.
No differential port.

Coupon:
q=-2..+2 mm
v=3..13 mm
FR4 thickness 1.00 mm
backside local ground full 4-mm width

Package:
center q=+0.25, v=7.0 mm
RF-IN q=0,v=6.085
RF-OUT q=0,v=7.915

Next, still without remote:
1. repo-local static geometry arithmetic audit
2. exact build-only artifact/evidence/task contract
3. final prebuild PASS/HOLD review

Only after that may BUILD authority be requested.
SOLVE remains separately gated.
