# Crate Base Prices(bp)
# Mineral Crates
steel_bp = 67296 # Steel Ingot Crates (67,296 silver)
bronze_bp = 113724 # Bronze Ingot Crates (113,724 silver)
snowfield_bp = 200000 # Snowfield Jade Box (200,000 silver)

# Timber Crates
calpheon_bp = 197280 # Calpheon Timber Crate (197,280 silver)
serendia_bp = 125460 # Serendia Timber Crate (125,460 silver)
thorn_bp = 201150 # Thorn Timber Crate (201,150 silver)
palm_bp = 5490 # Palm Timber Crate (5,490 silver)

def valencia_to_nampo(num_c1, num_c2, num_c3, num_c4, num_c5, num_c6, num_c7):
    """Prints silver profits from my trade crates using the route from Valencia to Nampo.

    Args:
        num_c1 (int): number of Steel Ingot Crates
        num_c2 (int): number of Bronze Ingot Crates
        num_c3 (int): number of Snowfield Jade Box
        num_c4 (int): number of Calpheon Timber Crates
        num_c5 (int): number of Serendia Timber Crates
        num_c6 (int): number of Thorn Timber Crates
        num_c7 (int): number of Palm Timber Crates
        
    Takes into account the travel distance bonus(td) and bargain bonus(b) multipliers for the route from Valencia to Nampo.
    """
    
    # Calculate Crate Profits(_p)
    td = 1.5 # Travel distance bonus multiplier
    b = 1 # Bargain bonus multiplier
    
    steel_p = num_c1 * steel_bp # Number of Crates(_c*) * Base Price(_bp)
    bronze_p = num_c2 * bronze_bp
    snowfield_p = num_c3 * snowfield_bp
    calpheon_p = num_c4 * calpheon_bp
    serendia_p = num_c5 * serendia_bp
    thorn_p = num_c6 * thorn_bp
    palm_p = num_c7 * palm_bp

    total_p = steel_p + bronze_p + snowfield_p + calpheon_p + serendia_p + thorn_p + palm_p
    bonus_total_p = round(total_p * td * b)
    
    # Dictionary to store Crate Profits
    crate_p = {
        "Steel": steel_p,
        "Bronze": bronze_p,
        "Snowfield": snowfield_p,
        "Calpheon": calpheon_p,
        "Serendia": serendia_p,
        "Thorn": thorn_p,
        "Palm": palm_p,
    }
    
    # Print All Crate & Total Profits
    # '<11' left-aligns the crate name in a 11-character wide field
    # '>14,' right-aligns the profit with comma formatting in a 14-character field
    print(f"{'Crates':<11}: {'Profit':>14}")
    print("-" * 34)
    
    for crate, profit in crate_p.items():
        print(f"{crate:<11}: {profit:>14,} silver")
        
    print("-" * 34)
    print(f"{'Total w/o b':<11}: {total_p:>14,} silver")
    print(f"{'Total w/ b':<11}: {bonus_total_p:>14,} silver")
    print("")
    