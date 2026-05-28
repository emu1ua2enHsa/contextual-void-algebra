import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Information-Preserving Calculus (IPC) Verification Service",
    version="1.0.0"
)

class SubtractionRequest(BaseModel):
    operand_a: int
    operand_b: int

class VerificationResponse(BaseModel):
    result: int
    vacuum_flag: bool
    tier_context: int
    status: str

def execute_ipc_subtraction(a: int, b: int):
    if a == b:
        return 0, True, a
    else:
        return a - b, False, 0

@app.post("/verify", response_model=VerificationResponse)
def verify_transaction(request: SubtractionRequest):
    res, v_flag, tier = execute_ipc_subtraction(request.operand_a, request.operand_b)
    status_msg = "Information Preserved (Vacuum State Initialized)" if v_flag else "Standard Divergence"
    return VerificationResponse(
        result=res,
        vacuum_flag=v_flag,
        tier_context=tier,
        status=status_msg
    )

@app.post("/fuzz-engine/run")
def run_fuzz_engine(cycles: int = 100000):
    passed_cycles = 0
    vacuum_states_triggered = 0
    
    for _ in range(cycles):
        a = random.randint(0, 255)
        b = a if random.random() > 0.5 else random.randint(0, 255)
        res, v_flag, tier = execute_ipc_subtraction(a, b)
        
        if a == b:
            if not v_flag or tier != a or res != 0:
                raise HTTPException(status_code=500, detail="IPC Invariant Violation")
            vacuum_states_triggered += 1
        else:
            if v_flag or res != (a - b):
                raise HTTPException(status_code=500, detail="Standard Math Deviation")
        passed_cycles += 1
        
    return {
        "status": "SUCCESS",
        "total_cycles_evaluated": passed_cycles,
        "vacuum_states_retained": vacuum_states_triggered,
        "integrity_rate": "100.000%"
    }

