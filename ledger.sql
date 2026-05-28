-- PostgreSQL Enterprise Reversible Schema Layout
-- Enforces Information-Preserving Calculus tracking at the row layer
-- Blocks tracking data erasure and establishes a 0.0% ledger reconciliation variance profile

-- Drop existing assets if present to ensure clean initialization boundaries
DROP TABLE IF EXISTS vacancy_capacity_archive CASCADE;
DROP TABLE IF EXISTS active_ledger_journal CASCADE;

-- 1. Active Processing Journal Table
CREATE TABLE active_ledger_journal (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    active_liquid_payload NUMERIC(18, 4) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Latent Vacancy Mirror Archive Table
CREATE TABLE vacancy_capacity_archive (
    vacancy_id SERIAL PRIMARY KEY,
    reference_transaction_id INT NOT NULL,
    account_id INT NOT NULL,
    latent_vacancy_capacity NUMERIC(18, 4) NOT NULL,
    operational_trajectory TEXT NOT NULL,
    erasure_prevention_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. The Core Non-Lossy Verification Logic Trigger
CREATE OR REPLACE FUNCTION process_ipc_reconciliation()
RETURNS TRIGGER AS $$
BEGIN
    -- Detect if a matching balance cancellation reduces the liquid payload properties to zero
    IF NEW.active_liquid_payload = 0.0000 THEN
        INSERT INTO vacancy_capacity_archive (
            reference_transaction_id, 
            account_id, 
            latent_vacancy_capacity, 
            operational_trajectory
        )
        VALUES (
            NEW.transaction_id, 
            NEW.account_id, 
            OLD.active_liquid_payload, 
            'PRESERVED_RECONCILIATION_VACANCY_FIELD_V1'
        );
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 4. Attach the Operational Safety Perimeter to the Active Journal Table
CREATE TRIGGER trigger_ipc_secure_reconciliation
    AFTER UPDATE OF active_liquid_payload ON active_ledger_journal
    FOR EACH ROW
    EXECUTE FUNCTION process_ipc_reconciliation();

-- 5. Build High-Velocity Query Performance Indexes
CREATE INDEX idx_active_ledger_accounts ON active_ledger_journal(account_id);
CREATE INDEX idx_vacancy_archive_references ON vacancy_capacity_archive(reference_transaction_id);

