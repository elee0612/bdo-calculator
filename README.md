# BDO Calculator

A command-line tool for calculating silver profit from **Black Desert Online** in-game activities.

## Features

- **Fishing Events** — calculates total silver profit from Bountiful, Mystical, and Precious clams
- **Trade Crates** — calculates silver profit for the Valencia → Nampo trade route (Steel, Bronze, Snowfield, Calpheon, Serendia, Thorn, and Palm crates), including the travel distance and bargain bonus multipliers
- Simple menu-driven interface with input validation (won't crash on invalid input — it just re-prompts)

## Requirements

- Python 3.10+ (uses `match` statements)
- No external dependencies

## Usage

### Running from source

```
python main.py
```

You'll be shown a menu:

```
Select an option:
1. Fishing Events
2. Trade Crates
3. Exit

Enter your choice (1-3):
```

Follow the prompts to enter your crate or clam counts, and the program will print a formatted profit breakdown.

### Running the standalone executable

If you don't have Python installed, download the latest `.exe` from the [Releases](../../releases) page and run it directly — no setup required.

> **Note:** Windows may show a SmartScreen warning ("Windows protected your PC") since the executable isn't code-signed. Click **More info** → **Run anyway** to proceed. This is expected for small open-source tools distributed without a paid signing certificate.

## Example Output

**Fishing Events**
```
Clams    :         Profit
--------------------------------
Bountiful:    121,000,000 silver
Mystical :    580,000,000 silver
Precious :    240,000,000 silver
--------------------------------
Total    :    941,000,000 silver
```

**Trade Crates**
```
Crates     :         Profit
----------------------------------
Steel      :    416,966,016 silver
Bronze     :     34,117,200 silver
Snowfield  :     18,000,000 silver
Calpheon   :     26,435,520 silver
Serendia   :     94,095,000 silver
Thorn      :    110,230,200 silver
Palm       :      9,377,220 silver
----------------------------------
Total w/o b:    709,220,856 silver
Total w/ b :  1,063,831,284 silver
```

## Project Structure

```
.
├── main.py             # Entry point — launches the menu
├── basic_ui.py          # Menu system and input handling
├── fishing_events.py    # Clam fishing profit calculations
└── trade_crates.py      # Trade crate profit calculations
```

## Notes & Assumptions

- Currently supports the **Valencia → Nampo** trade route only.
- Profit values are formatted assuming totals up to ~10 billion silver.
- Base crate/clam prices are hardcoded and reflect values at the time of writing — update the constants in `fishing_events.py` and `trade_crates.py` if in-game prices change.

## Building the Executable

This project can be packaged into a standalone `.exe` using [PyInstaller](https://pyinstaller.org/):

```
pip install pyinstaller
pyinstaller --onefile --console --name BDOProfitCalc main.py
```

The built executable will be in `dist/BDOProfitCalc.exe`.

## License

[MIT](LICENSE)