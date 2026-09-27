# SIM_EXECUTION

SimulationOps: 0.2.8

Current stage:
R1E1A4A_AR0_B1R_T2S_R2_RESULT_REVIEW_AWAIT_USER

BUILD_AUTHORIZED: false
SOLVE_AUTHORIZED: false
CST251_AUTHORIZED: false

T2F-R2:
PASS_R1E1A4A_AR0_B1R_T2F_R2_FIXTURE_BUILD_ONLY

T2S-R2:
PASS_R1E1A4A_AR0_B1R_T2S_R2_NW_BASELINE_CHARACTERIZED

Source fixture SHA256:
ae3bc705fea01e3a8f1c4a52458f447726843ba32a22d247c085c62b8bb83a7b

Solved SHA256:
0c099f4de12bff222919c24f16114f2e19dd7ec872b4644ce064c0cf248af54c

Formal NW solver invocations in R2: 1
Automatic retries: 0
Result-reader recovery: explicit run id 1, no solver rerun

Numerical qualification:
PASS
passes = 8
final two Delta-S = [3.2227382041216057e-06, 2.0071682606251655e-05]

Scientific verdict:
STRONG_CONCERN

Reason:
The transition is extremely symmetric and low-loss after mismatch normalization, but the 100-ohm balanced input is very strongly mismatched.

Decision-band 1.15-1.65 GHz:
- worst S11 = -0.3963567367 dB
- worst amplitude imbalance = 0.0012478257 dB
- worst phase error = 0.0205367864 deg
- worst CMR = -74.2854193275 dB
- worst mismatch-normalized excess loss = 0.1267529333 dB
- power closure = 0.9930400523 to 0.9976037222

Reference points:
L5 ~1.1768 GHz: S11 -0.4224 dB, normalized loss 0.1212 dB
L2 ~1.2272 GHz: S11 -0.4761 dB, normalized loss 0.1215 dB
L1 ~1.5752 GHz: S11 -1.0305 dB, normalized loss 0.1257 dB

Interpretation:
balanced-to-two-branch symmetry is excellent;
the first-cut throat/ground-acquisition geometry is not close to 100-ohm differential match.

No parameter sweep is authorized.

Stop:
RESULT REVIEW BEFORE T2S-R3 OPTIMIZATION.
