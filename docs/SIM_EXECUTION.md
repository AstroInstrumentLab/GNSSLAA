# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R4_A0_C0_CIRCUIT_REFERENCE_AND_A0_E1_LANDING_ZONE_FREEZE

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
LNA_INTEGRATION_AUTHORIZED: false

R4-A0 pre-simulation freeze:
PASS_ACTIVE_INTERFACE_PRE_SIM_FREEZE

Authority:
- docs/R1E1A4A_AR0_B1R_R4_A0_ACTIVE_INTERFACE_PRE_SIM_FREEZE_V01.md
- circuit/qpl9547/QPL9547_G0_MODEL_AUTHORITY_V01.md
- execution/R1E1A4A_AR0_B1R_R4_A0_ACTIVE_INTERFACE_MANIFEST_V01.json

Mainline decision:
D2-M2 passive return-path fixture mechanism probe is DEFERRED_CONTINGENCY.
Passive-fixture S11 is diagnostic evidence only and is not product matching authority.

Architecture B:
- 2 single-ended first-stage LNAs per polarization
- 4 per dual-pol element
- no pre-LNA balun
- active QPL9547 stays outside CST
- device-lead EM/circuit reference planes
- mandatory input/output DC blocks
- package-local backside-paddle ground vias
- remote lower-stalk-only LNA ground is prohibited as baseline

Reference G0 device:
QPL9547
5 V / 65 mA
device-lead S/noise reference
existing external S2P SHA256:
fad334a226acb9fbe1e4bd769f474afa14e2c23c18f31f4750c091f3d5d0424f

Next design-only work:
1. A0-C0 circuit/import sanity using existing S/noise authority
2. machine-transcribe/audit Rev-D package land pattern
3. freeze package orientation
4. freeze local-ground island and paddle-via seed
5. freeze DC-block/bias component-model seeds
6. freeze A0-E1 landing-zone geometry + device-lead ports + interference predicates

No NW/XW/251 call before the A0-E1 contract is frozen.
