#!/bin/bash
echo "=================================================================="
echo "IPC ENVIRONMENTAL SECURITY: INITIALIZING LOCAL FIREWALL LOCKS"
echo "=================================================================="

# Set restrictive permissions for local configuration files and databases
echo "[SECURE] Restricting write parameters on database storage elements..."
chmod 600 ipc_ledger.db

# Lock legal agreements to read-only for absolute historical integrity protection
echo "[SECURE] Locking legal and operating frameworks to read-only status..."
chmod 444 wyoming_operating_agreement.md

echo "[SUCCESS] Environment hardening protocol applied to active workspace."

