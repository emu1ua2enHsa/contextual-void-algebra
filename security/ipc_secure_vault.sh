zip -e -P "${VAULT_PASS}" -r "${OUTPUT_ARCHIVE}" . -x "*.zip" -x "*.tar.gz" -x "security/*" -x "*/.*"#!/usr/bin/env bash
# ====================================================================================
# ARTIFACT 3: CENTRALIZED WORKSPACE AES-256 AUTOMATED LOCKDOWN INTERFACE
# PATH: ~/ipc_workspace/security/ipc_secure_vault.sh
# ====================================================================================
set -euo pipefail

BASE_DIR="$HOME/ipc_workspace"

echo "===================================================================="
echo "      [MASTER CONTROL] CENTRALIZED SYSTEM SHIELD INTERFACE"
echo "===================================================================="
echo "Select Global Vault Operation Parameter:"
echo "1) WHOLE-WORKSPACE LOCKDOWN (Encrypt all text source assets and shred raw copies)"
echo "2) WHOLE-WORKSPACE RECOVERY (Decrypt all active components to workspace folders)"
read -rp "Enter choice [1-2]: " ACTION

case "$ACTION" in
    1)
        echo "[SHIELD] Initializing mass compression and multi-file locking arrays..."
        
        # Lock Theory Assets
        if [ -f "$BASE_DIR/theory/manuscript.tex" ]; then
            zip -e -P "${VAULT_PASS}" -r "${OUTPUT_ARCHIVE}" . -x "*.zip" -x "*.tar.gz" -x "security/*" -x "*/.*"
            rm -P "$BASE_DIR/theory/manuscript.tex" "$BASE_DIR/theory/build_pdf.sh" "$BASE_DIR/theory/normalize_style.py"
        fi
        
        # Lock Legal Assets
        if [ -f "$BASE_DIR/legal/patent_spec.txt" ]; then
            zip -e -j "$BASE_DIR/legal/patent_spec.zip" "$BASE_DIR/legal/patent_spec.txt"
            rm -P "$BASE_DIR/legal/patent_spec.txt"
        fi
        
        # Lock Software Assets
        if [ -f "$BASE_DIR/software/ledger.sql" ]; then
            zip -e -j "$BASE_DIR/software/software_core.zip" "$BASE_DIR/software/ledger.sql" "$BASE_DIR/software/app.py" "$BASE_DIR/software/Dockerfile" "$BASE_DIR/software/docker-compose.yml" "$BASE_DIR/software/fuzz_test_ipc.py"
            rm -P "$BASE_DIR/software/ledger.sql" "$BASE_DIR/software/app.py" "$BASE_DIR/software/Dockerfile" "$BASE_DIR/software/docker-compose.yml" "$BASE_DIR/software/fuzz_test_ipc.py"
        fi
        
        # Flush Clipboard Caches and Core System Indexes
        rm -rf ~/Library/Containers/com.apple.coreservices.pasteboard/Data/Library/Caches/*
        killall pboard
        echo "" > ~/.zsh_history && fc -R
        
        echo "=== LOCKDOWN COMPLETE: Whole repository frozen safe and encrypted ==="
        ;;
        
    2)
        echo "[SHIELD] Deploying centralized decryption keys..."
        
        if [ -f "$BASE_DIR/theory/manuscript.zip" ]; then
            unzip "$BASE_DIR/theory/manuscript.zip" -d "$BASE_DIR/theory/"
        fi
        if [ -f "$BASE_DIR/legal/patent_spec.zip" ]; then
            unzip "$BASE_DIR/legal/patent_spec.zip" -d "$BASE_DIR/legal/"
        fi
        if [ -f "$BASE_DIR/software/software_core.zip" ]; then
            unzip "$BASE_DIR/software/software_core.zip" -d "$BASE_DIR/software/"
        fi
        
        echo "=== RECOVERY COMPLETE: Active workspace restored to active memory layer ==="
        ;;
    *)
        echo "[ERROR] Invalid operation sequence matrix parameter."
        exit 1
        ;;
esac

