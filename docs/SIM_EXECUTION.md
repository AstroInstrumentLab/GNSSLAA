# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_T1_GROUND_ACQUISITION_BUILD_ONLY_AUTHORIZED

BUILD_AUTHORIZED: true
SOLVE_AUTHORIZED: false

Parent:
PASS_R1E1A4A_AR0_B1R_T0_RF_TENON_BUILD_ONLY
SHA256 f4c51b603fc01e8c3cec095de0ca641a3a671dc1e2449a95a123af6a8b902bb9

T1 nominal geometry:
- L_bal = 1.50 mm no-ground balanced throat;
- L_taper = 3.00 mm linear backside-ground acquisition;
- full local ground begins at v=4.50 mm;
- W_ground = 3.60 mm centered under each 1.90-mm signal;
- stalk thickness remains 1.00 mm.

Static preflight corrected the old 4.00-mm ground rail because it would intersect the orthogonal polarization ground.

No ports.
No solver.
Stop after build qualification and human 3D review.
