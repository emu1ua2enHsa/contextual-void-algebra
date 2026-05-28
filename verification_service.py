import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="Information-Preserving Calculus (IPC) Unified Gateway",
    description="Day 2 Integrated System: Core Logic, Venture Metrics, and Biochemical Frameworks",
    version="2.0.0"
)

# ==========================================
# 1. CORE IPC LOGIC LAYER
# ==========================================
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

@app.post("/core/verify", response_model=VerificationResponse, tags=["Core Logic"])
def verify_transaction(request: SubtractionRequest):
    res, v_flag, tier = execute_ipc_subtraction(request.operand_a, request.operand_b)
    status_msg = "Information Preserved (Vacuum State Initialized)" if v_flag else "Standard Divergence"
    return VerificationResponse(
        result=res, vacuum_flag=v_flag, tier_context=tier, status=status_msg
    )

@app.post("/core/fuzz-engine", tags=["Core Logic"])
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
        "status": "SUCCESS", "total_cycles_evaluated": passed_cycles,
        "vacuum_states_retained": vacuum_states_triggered, "integrity_rate": "100.000%"
    }

# ==========================================
# 2. VENTURE METRICS LAYER (cap_table_simulator.py)
# ==========================================
class CapTableSimulationRequest(BaseModel):
    total_shares: int
    founder_percentage: float
    investor_funding_round_usd: float
    target_valuation_usd: float

@app.post("/venture/cap-table", tags=["Venture Metrics"])
def simulate_cap_table(req: CapTableSimulationRequest):
    if req.founder_percentage > 100.0 or req.founder_percentage < 0:
        raise HTTPException(status_code=400, detail="Invalid percentage range")
    
    founder_shares = int(req.total_shares * (req.founder_percentage / 100.0))
    equity_issued_to_investors = (req.investor_funding_round_usd / req.target_valuation_usd) * 100.0
    investor_shares = int(req.total_shares * (equity_issued_to_investors / 100.0))
    pool_shares = req.total_shares - founder_shares - investor_shares
    
    return {
        "summary": "IPC Quantum Technologies Capital Distribution Matrix",
        "founder_allocation": {"shares": founder_shares, "percentage": f"{req.founder_percentage}%"},
        "investor_allocation": {"shares": investor_shares, "percentage": f"{round(equity_issued_to_investors, 2)}%"},
        "unallocated_treasury_pool": {"shares": max(0, pool_shares)}
    }

# ==========================================
# 3. BIOCHEMICAL FRAMEWORK LAYER (ipc_biochem_sim.py)
# ==========================================
class ProteinSequenceRequest(BaseModel):
    sequence: str  # e.g., "MGCVKSKPMK"

@app.post("/biochem/simulate", tags=["Biochemical Sim"])
def simulate_molecular_conservation(req: ProteinSequenceRequest):
    simulated_entropy = 0
    vacuum_nodes_stored = []
    
    for index, amino_acid in enumerate(req.sequence.upper()):
        tier_weight = ord(amino_acid)
        if tier_weight % 2 == 0:
            simulated_entropy += 1
        else:
            vacuum_nodes_stored.append({"position": index, "residual_tier": tier_weight})
            
    return {
        "status": "Simulation Stabilized",
        "sequence_length": len(req.sequence),
        "entropy_index": simulated_entropy,
        "ipc_preserved_bonds": len(vacuum_nodes_stored),
        "vacuum_matrices": vacuum_nodes_stored
    }
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(
    title="Information-Preserving Calculus (IPC) Unified Gateway",
    description="Day 2 Integrated System: Core Logic, Venture Metrics, and Biochemical Frameworks",
    version="2.0.0"
)

# ==========================================
# 1. CORE IPC LOGIC LAYER
# ==========================================
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

@app.post("/core/verify", response_model=VerificationResponse, tags=["Core Logic"])
def verify_transaction(request: SubtractionRequest):
    res, v_flag, tier = execute_ipc_subtraction(request.operand_a, request.operand_b)
    status_msg = "Information Preserved (Vacuum State Initialized)" if v_flag else "Standard Divergence"
    return VerificationResponse(
        result=res, vacuum_flag=v_flag, tier_context=tier, status=status_msg
    )

@app.post("/core/fuzz-engine", tags=["Core Logic"])
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
        "status": "SUCCESS", "total_cycles_evaluated": passed_cycles,
        "vacuum_states_retained": vacuum_states_triggered, "integrity_rate": "100.000%"
    }

# ==========================================
# 2. VENTURE METRICS LAYER (cap_table_simulator.py)
# ==========================================
class CapTableSimulationRequest(BaseModel):
    total_shares: int
    founder_percentage: float
    investor_funding_round_usd: float
    target_valuation_usd: float

@app.post("/venture/cap-table", tags=["Venture Metrics"])
def simulate_cap_table(req: CapTableSimulationRequest):
    if req.founder_percentage > 100.0 or req.founder_percentage < 0:
        raise HTTPException(status_code=400, detail="Invalid percentage range")
    
    founder_shares = int(req.total_shares * (req.founder_percentage / 100.0))
    equity_issued_to_investors = (req.investor_funding_round_usd / req.target_valuation_usd) * 100.0
    investor_shares = int(req.total_shares * (equity_issued_to_investors / 100.0))
    pool_shares = req.total_shares - founder_shares - investor_shares
    
    return {
        "summary": "IPC Quantum Technologies Capital Distribution Matrix",
        "founder_allocation": {"shares": founder_shares, "percentage": f"{req.founder_percentage}%"},
        "investor_allocation": {"shares": investor_shares, "percentage": f"{round(equity_issued_to_investors, 2)}%"},
        "unallocated_treasury_pool": {"shares": max(0, pool_shares)}
    }

# ==========================================
# 3. BIOCHEMICAL FRAMEWORK LAYER (ipc_biochem_sim.py)
# ==========================================
class ProteinSequenceRequest(BaseModel):
    sequence: str  # e.g., "MGCVKSKPMK"

@app.post("/biochem/simulate", tags=["Biochemical Sim"])
def simulate_molecular_conservation(req: ProteinSequenceRequest):
    simulated_entropy = 0
    vacuum_nodes_stored = []
    
    for index, amino_acid in enumerate(req.sequence.upper()):
        tier_weight = ord(amino_acid)
        if tier_weight % 2 == 0:
            simulated_entropy += 1
        else:
            vacuum_nodes_stored.append({"position": index, "residual_tier": tier_weight})
            
    return {
        "status": "Simulation Stabilized",
        "sequence_length": len(req.sequence),
        "entropy_index": simulated_entropy,
        "ipc_preserved_bonds": len(vacuum_nodes_stored),
        "vacuum_matrices": vacuum_nodes_stored
    }
