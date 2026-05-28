def calculate_token_issuance(total_supply: int, public_allocation: float):
    print("==================================================================")
    print("IPC VENTURE SYSTEM: SIMULATING TOKENIZED ASSET DISTRIBUTION")
    print("==================================================================")
    
    public_tokens = int(total_supply * (public_allocation / 100.0))
    reserve_tokens = total_supply - public_tokens
    
    print(f"Total Ecosystem Supply:   {total_supply:,} IPC")
    print(f"Public Market Liquidity:  {public_tokens:,} IPC ({public_allocation}%)")
    print(f"Treasury Reserve Custody: {reserve_tokens:,} IPC ({100.0 - public_allocation}%)")
    print("==================================================================")

if __name__ == "__main__":
    calculate_token_issuance(1000000000, 40.0)

