-- Create the core state table for standard ledger entries
CREATE TABLE IF NOT EXISTS ledger_states (
    entry_id SERIAL PRIMARY KEY,
    operand_a INT NOT NULL,
    operand_b INT NOT NULL,
    computed_result INT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the specialized vacuum origin tracking table
CREATE TABLE IF NOT EXISTS vacuum_origin_ledger (
    vacuum_id SERIAL PRIMARY KEY,
    entry_id INT,
    preserved_tier_context INT NOT NULL,
    initialized_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Function to intercept rows and route them based on IPC logic
CREATE OR REPLACE FUNCTION process_ipc_conservation()
RETURNS TRIGGER AS $$
BEGIN
    -- Check if standard arithmetic reduction equals absolute nullity
    IF NEW.operand_a = NEW.operand_b THEN
        NEW.computed_result := 0;
        -- Insert state record
        INSERT INTO ledger_states (operand_a, operand_b, computed_result)
        VALUES (NEW.operand_a, NEW.operand_b, NEW.computed_result)
        RETURNING entry_id INTO NEW.entry_id;

        -- Divert and isolate historical context to preserve information
        INSERT INTO vacuum_origin_ledger (entry_id, preserved_tier_context)
        VALUES (NEW.entry_id, NEW.operand_a);

        RETURN NEW;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

