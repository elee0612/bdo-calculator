# Clam Fishing Event
def clams(precious_clam, mystical_clam, bountiful_clam):
    """Print silver profit from a clam fishing event.

    Args:
        precious_clam (int): number of Precious clams caught.
        mystical_clam (int): number of Mystical clams caught.
        bountiful_clam (int): number of Bountiful clams caught.
    """
    
    # Calculate Clam Profits(_p)
    precious_clam_p = precious_clam * 30000000 # Precious (30,000,000 silver)
    mystical_clam_p = mystical_clam * 10000000 # Mystical (10,000,000 silver)
    bountiful_clam_p = bountiful_clam * 1000000 # Bountiful (1,000,000 silver)
    
    total_p = precious_clam_p + mystical_clam_p + bountiful_clam_p
    
    # Dictionary to store profits
    clam_p = {
        "Precious": precious_clam_p,
        "Mystical": mystical_clam_p,
        "Bountiful": bountiful_clam_p,
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