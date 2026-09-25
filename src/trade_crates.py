# Crate Base Prices(_bp)# Mineral Crates
steel_base_price = 67296 # Steel Ingot Crates (67,296 silver)
bronze_base_price = 113724 # Bronze Ingot Crates (113,724 silver)
snowfield_base_price = 200000 # Snowfield Jade Box (200,000 silver)

# Timber Crates
calpheon_base_price = 197280 # Calpheon Timber Crate (197,280 silver)
serendia_base_price = 125460 # Serendia Timber Crate (125,460 silver)
thorn_base_price = 201150 # Thorn Timber Crate (201,150 silver)
palm_base_price = 5490 # Palm Timber Crate (5,490 silver)

# Trade route from Valencia to Nampo
def valencia_to_nampo(steel, bronze, snowfield, calpheon, serendia, thorn, palm, trade_lvl):
    """Prints silver profits from my trade crates using the route from Valencia to Nampo.

    Args:
        steel (int): number of Steel Ingot Crates
        bronze (int): number of Bronze Ingot Crates
        snowfield (int): number of Snowfield Jade Box
        calpheon (int): number of Calpheon Timber Crates
        serendia (int): number of Serendia Timber Crates
        thorn (int): number of Thorn Timber Crates
        palm (int): number of Palm Timber Crates
        trade_lvl (int): the user's trade level

    Takes into account the travel distance bonus(td) and bargain bonus(b) multipliers for the route from Valencia to Nampo.
    """
    
    # Calculate Crate Profits
    travel_distance_bonus = 1.0 + 1.5 # Travel distance bonus multiplier (1.0 + bonus, capped at 2.5)
    bargain_bonus = 1.05 + trade_lvl * 0.005 # Bargain bonus multiplier (1.05 + 0.005 per trade level)
    total_bonus = travel_distance_bonus * bargain_bonus # Total bonus multiplier (travel distance bonus * bargain bonus)

    # Number of Crates * (Base Price * Total Bonus) rounded to nearest integer
    steel_profit = steel * round(steel_base_price * total_bonus)
    bronze_profit = bronze * round(bronze_base_price * total_bonus)
    snowfield_profit = snowfield * round(snowfield_base_price * total_bonus)
    calpheon_profit = calpheon * round(calpheon_base_price * total_bonus)
    serendia_profit = serendia * round(serendia_base_price * total_bonus)
    thorn_profit = thorn * round(thorn_base_price * total_bonus)
    palm_profit = palm * round(palm_base_price * total_bonus)

    total_profit = round(steel_profit + bronze_profit + snowfield_profit + calpheon_profit + serendia_profit + thorn_profit + palm_profit)
    
    # Dictionary to store crate profits
    crate_profits = {
        "Steel": steel_profit,
        "Bronze": bronze_profit,
        "Snowfield": snowfield_profit,
        "Calpheon": calpheon_profit,
        "Serendia": serendia_profit,
        "Thorn": thorn_profit,
        "Palm": palm_profit,
    }
    
    # Print All Crate & Total Profits
    # '<12' left-aligns the crate name in a 12-character wide field
    # '>14,' right-aligns the profit with comma formatting in a 14-character field
    print(f"{'Crates':<12}: {'Profit':>14}")
    print("-" * 35)
    
    # Print each crate's profit with formatting
    for crate, profit in crate_profits.items():
        print(f"{crate:<12}: {profit:>14,} silver")
    
    print()
    print(f"{'TD bonus':<12}: {travel_distance_bonus*100:>14.2f}%") # Total travel distance bonus multiplier
    print(f"{'B bonus':<12}: {bargain_bonus*100:>14.2f}%") # Total bargain bonus multiplier
    print("-" * 35)
    print(f"{'Total profit':<12}: {total_profit:>14,} silver") # Total profit with bonuses applied
    print(f"{'Total bonus':<12}: {total_bonus*100:>14.2f} %") # Total bonus multiplier
    print("")
    