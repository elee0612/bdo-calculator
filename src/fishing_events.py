# Clam Fishing Event
def clams(bountiful, mystical, precious):
    """
    Print silver profit from a clam fishing event.

    Args:
        bountiful (int): number of Bountiful clams.
        mystical (int): number of Mystical clams.
        precious (int): number of Precious clams.
    """
    
    # Calculate Clam Profits(_p)
    bountiful_profit = bountiful * 1000000 # Bountiful (1,000,000 silver) each
    mystical_profit = mystical * 10000000 # Mystical (10,000,000 silver) each
    precious_profit = precious * 30000000 # Precious (30,000,000 silver) each
    
    total_profit = bountiful_profit + mystical_profit + precious_profit
    
    # Dictionary to store profits
    clam_profits = {
        "Bountiful": bountiful_profit,
        "Mystical": mystical_profit,
        "Precious": precious_profit,
    }
    
    # Print All Clam & Total Profits
    # '<9' left-aligns the crate name in a 9-character wide field
    # '>14,' right-aligns the profit with comma formatting in a 14-character field
    print(f"{'Clams':<9}: {'Profit':>14}")
    print("-" * 32)
    
    # Print each clam's profit with formatting
    for clam, profit in clam_profits.items():
            print(f"{clam:<9}: {profit:>14,} silver")
            
    print("-" * 32)
    print(f"{'Total':<9}: {total_profit:>14,} silver")
    print("")