from __future__ import print_function
import argparse, hashlib, json, os, subprocess, sys
from pathlib import Path

PARENT_SHA="fbf375c605acff4f53e46fedefba7acf24ef871b427a579091144b7833dd149e"
MODEL="R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_BUILD_ONLY_V01"

def sha256(path):
    h=hashlib.sha256()
    with open(str(path),"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def git_head(repo):
    return subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()

def write_json(path,obj):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["qualification","build"],required=True)
    ap.add_argument("--project-root",required=True)
    ap.add_argument("--output-packet",required=True)
    ap.add_argument("--state-root",required=True)
    ap.add_argument("--result-packet",required=True)
    ap.add_argument("--qualification-output")
    ap.add_argument("--target-root")
    ap.add_argument("--parent-cst")
    ap.add_argument("--cst-python")
    a=ap.parse_args()

    root=Path(a.project_root).resolve()
    head=git_head(root)
    runner="scripts/run_r1e1a4a_ar0_b1r_r4_a0_e2c_dualpol_build_only_v01.py"
    bridge="scripts/simops_cst_python_bridge_v01.py"
    audit="scripts/audit_e2c_build_entrypoint_contract_v01.py"
    generator="scripts/make_e2c_build_recovery_runner_packet_v01.py"
    macro="source/cst/R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_BUILD_ONLY_V01.mcr"
    inv="execution/R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_BUILD_INVENTORY_V01.json"
    kernel="source/cst/R1E1A4A_AR0_B1R_R4_A0_E2C_16VIA_DRILL_KERNEL_REFERENCE_V01.mcr"

    hashes={p:sha256(root/p) for p in [runner,bridge,audit,generator,macro,inv,kernel]}

    common={
      "schema_version":"runner-task-v0.1",
      "project":{"name":"GNSS_Lband_Active_Array","repository":"Dingo-infinity2020/GNSS_Lband_Active_Array","source_commit":head,"model_identity":MODEL},
      "transport":{"type":"local","ssh_alias":"","remote_shell":""},
      "authorization":{"BUILD_AUTHORIZED":False,"SOLVE_AUTHORIZED":False},
      "preflight":{"fail_closed":True,"checks":[
        {"id":"git_clean","type":"git_clean","path":"."},
        {"id":"git_head","type":"git_head_equals","path":".","commit":head},
        {"id":"runner_hash","type":"file_sha256_equals","path":runner,"sha256":hashes[runner]},
        {"id":"bridge_hash","type":"file_sha256_equals","path":bridge,"sha256":hashes[bridge]},
        {"id":"audit_hash","type":"file_sha256_equals","path":audit,"sha256":hashes[audit]},
        {"id":"generator_hash","type":"file_sha256_equals","path":generator,"sha256":hashes[generator]},
        {"id":"result_absent","type":"result_path_absent"}
      ]},
      "dc_call_budget":{"target_calls":1,"polling_policy":"no_polling"}
    }

    if a.mode=="qualification":
        if not a.qualification_output or not a.cst_python:
            raise SystemExit("qualification requires --qualification-output and --cst-python")
        qout=str(Path(a.qualification_output).resolve())
        bridge_evidence=str(Path(qout).with_name("e2c_bridge_qualification.json"))
        packet=dict(common)
        packet.update({
          "packet_id":"GNSS-E2C-RECOVERY-ENTRYPOINT-QUAL-20260930-01",
          "stage":{"name":"E2C_BUILD_RECOVERY_ENTRYPOINT_QUALIFICATION","kind":"READ_ONLY","control_host_alias":"NW","working_directory":str(root),"stop_boundary":"RETURN_AFTER_AST_AND_CST_RUNTIME_QUALIFICATION"},
          "entrypoint":{"argv":[
              "python","-c",
              ("import subprocess,sys; "
               "rc1=subprocess.call([sys.executable,'"+audit+"','--runner','"+runner+"','--out',r'"+qout+"']); "
               "rc2=subprocess.call([sys.executable,'"+bridge+"','--bridge-evidence',r'"+bridge_evidence+"','--','"+runner+"','--help']); "
               "sys.exit(rc1 or rc2)")
            ],
            "environment":{"CST_PYTHON_EXECUTABLE":str(Path(a.cst_python).resolve())},
            "timeout_seconds":120},
          "expected_outputs":[
            {"path":qout,"required":True,"sha256":True},
            {"path":bridge_evidence,"required":True,"sha256":True}
          ],
          "result":{"state_root":str(Path(a.state_root).resolve()),"result_packet_path":str(Path(a.result_packet).resolve())}
        })
        write_json(a.output_packet,packet)
        return 0

    # build mode
    if not a.target_root or not a.parent_cst or not a.cst_python:
        raise SystemExit("build requires --target-root --parent-cst --cst-python")
    target=Path(a.target_root).resolve()
    parent=Path(a.parent_cst).resolve()
    parent_comp=parent.with_suffix("")
    out=target/"R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_COEXISTENCE_BUILD_ONLY_V01.cst"
    review=target/"R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_HUMAN_REVIEW_COPY.cst"
    evidence=target/"evidence"
    bridge_evidence=Path(a.result_packet).resolve().with_name("build_bridge_provenance.json")

    packet=dict(common)
    packet["packet_id"]="GNSS-E2C-DUALPOL-BUILD-RECOVERY-20260930-02"
    packet["stage"]={"name":"R1E1A4A_AR0_B1R_R4_A0_E2C_DUALPOL_BUILD_RECOVERY","kind":"BUILD_ONLY","control_host_alias":"NW","working_directory":str(root),"stop_boundary":"STOP_AFTER_177_24_16_29_AUDIT_AND_COMPLETE_HUMAN_REVIEW_COPY_NO_SOLVER"}
    packet["authorization"]={"BUILD_AUTHORIZED":True,"SOLVE_AUTHORIZED":False}
    packet["entrypoint"]={
      "argv":["python",bridge,"--bridge-evidence",str(bridge_evidence),"--",runner,
        "--parent-cst",str(parent),
        "--macro",str(root/macro),
        "--kernel-reference-macro",str(root/kernel),
        "--inventory-contract",str(root/inv),
        "--out",str(out),
        "--review-copy",str(review),
        "--evidence",str(evidence)],
      "environment":{"CST_PYTHON_EXECUTABLE":str(Path(a.cst_python).resolve())},
      "timeout_seconds":7200
    }
    packet["preflight"]["checks"].extend([
      {"id":"parent_exists","type":"path_exists","path":str(parent)},
      {"id":"parent_companion_exists","type":"path_exists","path":str(parent_comp)},
      {"id":"parent_hash","type":"file_sha256_equals","path":str(parent),"sha256":PARENT_SHA},
      {"id":"macro_hash","type":"file_sha256_equals","path":macro,"sha256":hashes[macro]},
      {"id":"inventory_hash","type":"file_sha256_equals","path":inv,"sha256":hashes[inv]},
      {"id":"kernel_hash","type":"file_sha256_equals","path":kernel,"sha256":hashes[kernel]},
      {"id":"target_root_absent","type":"path_absent","path":str(target)}
    ])
    packet["expected_outputs"]=[
      {"path":str(out),"required":True,"sha256":True},
      {"path":str(review),"required":True,"sha256":True},
      {"path":str(evidence/"FINAL_STATUS.txt"),"required":True,"sha256":True},
      {"path":str(evidence/"summary.json"),"required":True,"sha256":True},
      {"path":str(evidence/"HUMAN_3D_REVIEW.md"),"required":True,"sha256":True},
      {"path":str(bridge_evidence),"required":True,"sha256":True}
    ]
    packet["result"]={"state_root":str(Path(a.state_root).resolve()),"result_packet_path":str(Path(a.result_packet).resolve())}
    write_json(a.output_packet,packet)
    return 0

if __name__=="__main__":
    sys.exit(main())
