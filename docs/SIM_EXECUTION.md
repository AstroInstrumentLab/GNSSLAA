# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R4_A0_E1_FOOTPRINT_VIA_LOCAL_GROUND_CONTRACT_FREEZE

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

R4-A0 pre-simulation architecture:
PASS_ACTIVE_INTERFACE_PRE_SIM_FREEZE

A0-C0 committed QPL9547 data sanity:
PASS_R4_A0_C0_G0_COMMITTED_DATA_SANITY

A0-E1 landing-zone design seed:
DESIGN_SEED_FROZEN_NO_EXECUTION

Authority:
- docs/R1E1A4A_AR0_B1R_R4_A0_ACTIVE_INTERFACE_PRE_SIM_FREEZE_V01.md
- docs/R1E1A4A_AR0_B1R_R4_A0_E1_LANDING_ZONE_DESIGN_SEED_V01.md
- circuit/qpl9547/QPL9547_G0_MODEL_AUTHORITY_V01.md
- circuit/qpl9547/analysis/R4_A0_C0_G0_DATA_SANITY.json
- execution/R1E1A4A_AR0_B1R_R4_A0_ACTIVE_INTERFACE_MANIFEST_V01.json
- execution/R1E1A4A_AR0_B1R_R4_A0_E1_LANDING_ZONE_SEED_V01.json

Mainline decisions:
- D2-M2 passive return-path fixture mechanism probe = DEFERRED_CONTINGENCY.
- Passive-fixture S11 = diagnostic only, not product matching authority.
- Architecture B remains twin single-ended first-stage LNAs per polarization.
- QPL9547 active device remains outside CST.
- Co-simulation reference planes are QPL9547 device leads.
- Input and output DC blocks are mandatory.
- Package-local backside-paddle ground vias are mandatory.
- Remote lower-stalk-only LNA ground is prohibited as the baseline.
- Exact half-lap slot geometry may reopen locally if required to provide a valid first-stage RF ground.

Frozen landing-zone seed:
- branch centers u=+/-3 mm
- historical LNA center v~7 mm is a placement seed only
- RF IN faces upstream (-v)
- RF OUT/VDD faces downstream (+v)
- same physical package rotation on both branches; no fictitious mirrored package
- G0 input/output DC block seed = 100 pF
- G0 bias-choke seed = Coilcraft 0402CS-18NXGRW, 18 nH
- ground candidates: branch-local baseline / short local common / remote sentinel

Remaining design-only work before any remote BUILD:
1. machine-transcribe and second-check the Rev-D recommended PCB metal + solder-mask pattern;
2. apply actual PCB-fabricator annular-ring / drill rules and freeze paddle-via count/placement;
3. draw at least one manufacturable short-local-ground solution compatible with the orthogonal stalks;
4. select initial broadband 0402 DC-block model; retain 100 pF only as G0 value seed;
5. freeze E1 component-pad representation and exact EM/circuit port count/coordinates;
6. freeze copper/solder/material assumptions and interference predicates.

No NW/XW/251 call before those items are frozen.
