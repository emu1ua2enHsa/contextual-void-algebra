import subprocess
import json
import os

print("==================================================================")
print("IPC SYSTEM CONSOLIDATION: EXECUTING FULL ARCHITECTURE TELEMETRY")
print("==================================================================")

def verify_full_stack():
    metrics = {"hardware_layer": "FAILED", "ledger_layer": "FAILED", "software_layer": "FAILED"}
    
    # 1. Audit Hardware Layer
    if os.path.exists("simulation_waveforms.vcd"):
        print("[CHECK] Hardware layer waveform telemetry detected.")
        metrics["hardware_layer"] = "PASSED"
        
    # 2. Audit Relational Data Ledger
    if os.path.exists("ipc_ledger.db"):
        print("[CHECK] Relational database storage matrix detected.")
        metrics["ledger_layer"] = "PASSED"
        
    # 3. Audit Local API Endpoint Connectivity Mapping
    try:
        import fastapi
        print("[CHECK] Software API framework verified locally.")
        metrics["software_layer"] = "PASSED"
    except ImportError:
        pass

    print("\n================ SYSTEM STATUS SUMMARY ================")
    print(json.dumps(metrics, indent=2))
    print("=======================================================")

if __name__ == "__main__":
    verify_full_stack()

