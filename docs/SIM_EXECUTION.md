# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_R3_D2_M1B_BUILD_ONLY_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false
CONDITIONAL_AB_SOLVE_AFTER_POLB_BUILD_PASS: true

Canonical D2-M0R1:
4ec39ab9965dd9ec6b416d801ded0ee6e56d910d2ffc2ba405cb9dec978cd91e

Existing Pol-A fixture:
33294aa6200264135582ec0c0742a1b4e6ca7b2148e1adece2f64388d81d3dd6

Build:
fresh Pol-B 3-port fixture with rotated port coordinates.

If Pol-B build PASS:
one NW solve Pol-A
one NW solve Pol-B
same 1.0..1.8 GHz adaptive HF-FD solver
no retry
no sweep

Scientific target:
measure RF impact of the mechanically required 1.05-mm A/B common-ground merge-height offset.
