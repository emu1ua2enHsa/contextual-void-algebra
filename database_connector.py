import sqlite3
import os

DB_FILE = "ipc_ledger.db"

def initialize_local_database():
    """Initializes a local database file with structural tracking triggers."""
    print("==================================================================")
    print("IPC DATABASE SYSTEM: INITIALIZING STORAGE LEDGERS & DATA TRIGGERS")
    print("==================================================================")
    
    # Connect to local SQLite file
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 1. Create standard ledger table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ledger_states (
        entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
        operand_a INTEGER NOT NULL,
        operand_b INTEGER NOT NULL,
        computed_result INTEGER NOT NULL,
        recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    # 2. Create specialized vacuum tracking table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacuum_origin_ledger (
        vacuum_id INTEGER PRIMARY KEY AUTOINCREMENT,
        entry_id INTEGER,
        preserved_tier_context INTEGER NOT NULL,
        initialized_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    # 3. Create the programmatic trigger equivalent for zero-loss conservation
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS process_ipc_conservation
    AFTER INSERT ON ledger_states
    FOR EACH ROW
    WHEN NEW.operand_a = NEW.operand_b
    BEGIN
        INSERT INTO vacuum_origin_ledger (entry_id, preserved_tier_context)
        VALUES (NEW.entry_id, NEW.operand_a);
    END;
    """)
    
    conn.commit()
    conn.close()
    print("[SUCCESS] Local SQLite database and relational tables generated.")
    print("[SUCCESS] Information-Preserving Trigger initialized successfully.")

def log_transaction_to_db(a: int, b: int, result: int):
    """Inserts a transactional record into the state engine."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO ledger_states (operand_a, operand_b, computed_result)
    VALUES (?, ?, ?)
    """, (a, b, result))
    
    conn.commit()
    conn.close()

def fetch_database_audit_report():
    """Queries the database to confirm data preservation metrics."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    print("\n--- DATABASE AUDIT LOG ---")
    cursor.execute("SELECT * FROM ledger_states")
    print("Standard Ledger Entries:")
    for row in cursor.fetchall():
        print(f"  ID {row[0]}: {row[1]} ⊖ {row[2]} = {row[3]} ({row[4]})")
        
    cursor.execute("SELECT * FROM vacuum_origin_ledger")
    print("\nPreserved Vacuum Matrices:")
    for row in cursor.fetchall():
        print(f"  Vacuum ID {row[0]}: Connected to entry ID {row[1]} | Preserved Origin Tier Context: [{row[2]}]")
    print("--------------------------")
    
    conn.close()

if __name__ == "__main__":
    # If run directly, test the entire relational data layer pipeline
    initialize_local_database()
    print("\n[TEST] Logging standard operation (10 - 4)...")
    log_transaction_to_db(10, 4, 6)
    
    print("[TEST] Logging zero-loss identity divergence (214 ⊖ 214)...")
    log_transaction_to_db(214, 214, 0)
    
    # Pull the real-time report to visually confirm the trigger intercepted the data
    fetch_database_audit_report()

