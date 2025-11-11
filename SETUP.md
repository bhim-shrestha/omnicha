# ResoCharge Setup Guide

## Quick Start

### Option 1: Using Virtual Environment (RECOMMENDED)

**Why virtual environment?**
- Isolates project dependencies
- Prevents conflicts with other Python projects
- Easy to reproduce on other machines
- Professional best practice

**Setup steps:**

```bash
# Navigate to project directory (replace with your actual path)
cd path/to/your/resocha/project

# Create virtual environment (one time only)
python3 -m venv venv

# Activate virtual environment (do this each time)
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the simulator
python resocharge_simulator.py

# When done, deactivate
deactivate
```

### Option 2: Global Installation (SIMPLER)

**Install directly (no virtual environment):**

```bash
# Install dependencies globally
pip3 install numpy matplotlib

# Run the simulator
python3 resocharge_simulator.py
```

---

## What You'll See When Running

The simulator will:

1. **Print detailed analysis** for 3 scenarios:
   - Urban apartment
   - Near cell tower
   - Rural area

2. **Show power calculations**:
   - Total received power
   - Total harvested power
   - Efficiency breakdown
   - Power by frequency band

3. **Analyze device capabilities**:
   - What can be powered (sensors, displays)
   - What cannot be powered (phones, LEDs)
   - Time to charge iPhone (spoiler: centuries!)

4. **Generate visualization**:
   - Creates `scenario_comparison.png`
   - Bar charts comparing scenarios
   - Log-scale comparison to device requirements

---

## Expected Output Example

```
🔋 ResoCharge RF Energy Harvesting Simulator
======================================================================

SCENARIO 1: Urban Apartment
======================================================================
SYSTEM CONFIGURATION
----------------------------------------------------------------------
RF Sources: 8
Antennas: 6
Matching Efficiency: 90.0%
Filter Efficiency: 95.0%

POWER ANALYSIS
----------------------------------------------------------------------
Total Received Power:    45.30 μW
Total Harvested Power:   15.20 μW (0.0152 mW)
Overall System Efficiency: 33.6%

POWER BREAKDOWN BY SOURCE
----------------------------------------------------------------------
WiFi 2.4GHz          @ 2450.0 MHz:     4.82 μW (eff:  42.3%)
5G 3.5GHz           @ 3500.0 MHz:     3.76 μW (eff:  38.5%)
Cellular 1900MHz    @ 1900.0 MHz:     2.91 μW (eff:  35.2%)
...

DEVICE CAPABILITIES
----------------------------------------------------------------------
Temperature Sensor (10 μW)        : ✅ CAN POWER (152% of requirement)
Motion Detector (20 μW)           : ⚠️ MARGINAL (76% of requirement)
E-ink Display (50 μW)             : ❌ INSUFFICIENT (30% of requirement)
LED (5 mW)                        : ❌ INSUFFICIENT (0.3% of requirement)

iPhone Charging Estimate:
  Time to full charge: 27397 days (75.0 years)
  Daily contribution:  0.0036% of battery

======================================================================
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'numpy'"

**Solution:**
```bash
pip3 install numpy matplotlib
```

### "Permission denied"

**Solution:**
```bash
pip3 install --user numpy matplotlib
```

### Virtual environment not activating

**Check you're in the right directory:**
```bash
pwd  # Should show your project directory path
ls venv/  # Should show bin, lib, etc.
```

### Chart not displaying

The simulator saves the chart as a file instead of displaying it:
```bash
# Check if image was created
ls -lh scenario_comparison.png

# View on Mac
open scenario_comparison.png
```

---

## What Files Get Created

After running the simulator:

```
resocha/
├── scenario_comparison.png  ← Visualization chart (new)
├── venv/                     ← Virtual environment (if created)
│   ├── bin/
│   ├── lib/
│   └── ...
└── (all other project files)
```

---

## Best Practices

### For Development

**Always use virtual environment:**
```bash
source venv/bin/activate  # Start
# ... do your work ...
deactivate                # End
```

### For Sharing

**Include in .gitignore (already done):**
```
venv/
*.png  # Output images
```

### For Reproducibility

**Document versions:**
```bash
# After installing, freeze exact versions
pip freeze > requirements-lock.txt
```

---

## Commands Reference

```bash
# Setup (one time)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Daily use
source venv/bin/activate      # Start session
python resocharge_simulator.py  # Run simulator
deactivate                    # End session

# Update dependencies
pip install --upgrade numpy matplotlib

# Check installed packages
pip list

# Remove virtual environment (if needed)
rm -rf venv/
```

---

## System Requirements

- **Python:** 3.8 or higher (you have 3.14.0 ✅)
- **OS:** macOS, Linux, or Windows
- **RAM:** 100 MB minimum
- **Disk:** 200 MB for virtual environment

---

## Need Help?

**Check Python version:**
```bash
python3 --version  # Should be 3.8+
```

**Check pip:**
```bash
pip3 --version
```

**Verify installation:**
```bash
python3 -c "import numpy, matplotlib; print('✅ Dependencies OK')"
```

**Clean reinstall:**
```bash
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

**Ready to run!** Execute: `python3 resocharge_simulator.py`
