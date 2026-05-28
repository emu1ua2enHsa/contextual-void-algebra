#!/usr/bin/env python3
"""
IPC SYSTEM SUBSYSTEM: WYOMING CAPITALIZATION ENGINE
Models cap table dilution, conversion mechanics, and share distributions
for a Series Seed $6,000,000 aggregate principal convertible note round.
"""
import json

class CapTableSimulator:
    def __init__(self, founding_shares=10000000):
        # Initial corporate structure: Founders hold 100% of issued stock
        self.shares_outstanding = founding_shares
        self.founder_shares = founding_shares
        
        # Note parameters from Series Seed Term Sheet
        self.note_principal = 6000000.0
        self.interest_rate = 0.045
        self.valuation_cap = 25000000.0
        self.discount_rate = 0.20 # 20% conversion discount

    def calculate_conversion(self, series_a_valuation, series_a_new_capital, months_elapsed=12):
        print(f"[CAP SIM] Simulating Series A Conversion after {months_elapsed} months...")
        
        # 1. Calculate accrued interest on the aggregate principal
        accrued_interest = self.note_principal * (self.interest_rate * (months_elapsed / 12.0))
        total_note_debt = self.note_principal + accrued_interest
        
        # 2. Determine Pre-Money Share Price based on Series A parameters
        standard_pre_money_price = series_a_valuation / self.shares_outstanding
        
        # 3. Calculate capped and discounted prices to find the optimal conversion vector
        capped_price = self.valuation_cap / self.shares_outstanding
        discounted_price = standard_pre_money_price * (1.0 - self.discount_rate)
        
        # Note converts at the lowest price variant to maximize investor share count
        conversion_price = min(capped_price, discounted_price)
        note_shares_issued = int(total_note_debt / conversion_price)
        
        # 4. Calculate new cash shares issued to Series A investors
        series_a_shares_issued = int(series_a_new_capital / standard_pre_money_price)
        
        # 5. Compute post-conversion capitalization framework
        post_conversion_total_shares = self.shares_outstanding + note_shares_issued + series_a_shares_issued
        
        report = {
            "pre_conversion_founder_shares": self.founder_shares,
            "total_note_debt_converted": round(total_note_debt, 2),
            "effective_conversion_share_price": round(conversion_price, 4),
            "shares_allocated_to_seed_notes": note_shares_issued,
            "shares_allocated_to_series_a_cash": series_a_shares_issued,
            "post_conversion_total_shares_outstanding": post_conversion_total_shares,
            "ownership_percentages": {
                "founders_equity_pct": round((self.founder_shares / post_conversion_total_shares) * 100, 2),
                "seed_note_investors_pct": round((note_shares_issued / post_conversion_total_shares) * 100, 2),
                "series_a_cash_investors_pct": round((series_a_shares_issued / post_conversion_total_shares) * 100, 2)
            }
        }
        return report

if __name__ == "__main__":
    simulator = CapTableSimulator()
    
    # Model a Series A Round: $35M Pre-Money Valuation, $7M New Venture Capital Cash Injection
    conversion_data = simulator.calculate_conversion(
        series_a_valuation=35000000.0,
        series_a_new_capital=7000000.0,
        months_elapsed=18 # Assuming conversion occurs 1.5 years post-closing
    )
    
    print("\n[CAP SIM] Post-Money Valuation Capitalization Array:")
    print(json.dumps(conversion_data, indent=4))

