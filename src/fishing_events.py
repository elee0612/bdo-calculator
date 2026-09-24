# Clam Fishing Event
def clams(bountiful, mystical, precious):
    """
    Print silver profit from a clam fishing event.

    Args:
        bountiful (int): number of Bountiful clams.
        mystical (int): number of Mystical clams.
        precious (int): number of Precious clamsc.
    """
    
    # Calculate Clam Profits(_p)
    bountiful_p = bountiful * 1000000 # Bountiful (1,000,000 silver)
    mystical_p = mystical * 10000000 # Mystical (10,000,000 silver)
    precious_p = precious * 30000000 # Precious (30,000,000 silver)
    
    total_p = bountiful_p + mystical_p + precious_p
    
    # Dictionary to store profits
    clam_p = {
        "Bountiful": bountiful_p,
        "Mystical": mystical_p,
        "Precious": precious_p,
    }
    
    # Print All Clam & Total Profits
    # '<9' left-aligns the crate name in a 9-character wide field
    # '>14,' right-aligns the profit with comma formatting in a 14-character field
    print(f"{'Clams':<9}: {'Profit':>14}")
    print("-" * 32)
    
    for clam, profit in clam_p.items():
            print(f"{clam:<9}: {profit:>14,} silver")
            
    print("-" * 32)
    print(f"{'Total':<9}: {total_p:>14,} silver")
    print("")