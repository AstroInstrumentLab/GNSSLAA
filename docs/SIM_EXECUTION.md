# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R4_A0_E1_DIMENSIONED_PLACEMENT_AND_MATERIAL_CONTRACT

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

Completed without NW/XW/251:
- QPL9547 Rev-D footprint contract
- G0 3-paddle-via EM/fabrication seed
- G-L0 branch-local-ground baseline
- half-lap exact local slot released if later active-ground evidence requires revision
- QPL9547 FDD bias/DC-block topology contract
- G0 Murata 100-pF C0G model family selection
- G0 Coilcraft 18-nH choke model selection
- five-node one-LNA passive EM port topology
- A0-E1 prebuild review checklist

Five E1 nodes:
E_UP
P_IN
P_OUT
E_DN
B_VDD

All are single-ended to finite local branch ground.
No differential port.

Remaining before first remote build:
1. freeze exact dimensioned E1 component/port placement
2. freeze FR4/copper/solder-mask/solder material contract
3. freeze deterministic interference/clearance predicates
4. freeze build-only artifact/evidence contract

No remote call before those are complete.
