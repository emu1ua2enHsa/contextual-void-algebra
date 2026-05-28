#!/usr/bin/env bash
set -euo pipefail

TARGET_FILE="../theory/manuscript.tex"
ENCRYPTED_FILE="../theory/manuscript.zip"

echo "=== [IPC ENGINE] Core Asset Protection Interface ==="
echo "Select Operation Mode:"
echo "1) LOCK (Encrypt and shred raw source file)"
echo "2) UNLOCK (Decrypt to active memory layer)"
read -rp "Enter choice [1-2]: " CHOICE

case "$CHOICE" in
    1)
        if [ ! -f "$TARGET_FILE" ]; then
            echo "[ERROR] Source file '$TARGET_FILE' not found in this register."
            exit 1
        fi
        echo "[IPC] Executing symmetric AES-256 encryption sequence..."
        zip -e "$ENCRYPTED_FILE" "$TARGET_FILE"

        echo "[IPC] Shredding raw text file from hard drive sectors..."
        rm -P "$TARGET_FILE"
        echo "=== SUCCESS: File locked securely inside $ENCRYPTED_FILE ==="
        ;;
    2)
        if [ ! -f "$ENCRYPTED_FILE" ]; then
            echo "[ERROR] Target file '$ENCRYPTED_FILE' is not present."
            exit 1
        fi
        echo "[IPC] Initiating decryption pipeline..."
        unzip "$ENCRYPTED_FILE"
        echo "=== SUCCESS: File decrypted to $TARGET_FILE ==="
        ;;
    *)
        echo "[ERROR] Invalid operation parameter."
        exit 1
        ;;
esac

