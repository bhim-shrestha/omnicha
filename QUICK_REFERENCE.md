# Quick Reference: RF Energy Harvesting

## Key Formulas

### Energy-Frequency Relationship
```
E = h × f
Where:
 E = Energy per photon (Joules)
 h = Planck's constant (6.626 × 10⁻³⁴ J·s)
 f = Frequency (Hz)
```

### Wavelength
```
λ = c / f
Where:
 λ = Wavelength (meters)
 c = Speed of light (3 × 10⁸ m/s)
 f = Frequency (Hz)
```

### Antenna Length (Dipole)
```
L = λ / 2 = c / (2f)

Examples:
 FM 100 MHz: L = 1.5 m
 WiFi 2.4 GHz: L = 6.25 cm
 5G 3.5 GHz: L = 4.29 cm
```

### Power Density
```
S = P / (4πr²)
Where:
 S = Power density (W/m²)
 P = Transmitter power (W)
 r = Distance (m)
```

### Harvested Power
```
P_harvested = S × A × η_total
Where:
 S = Power density (W/m²)
 A = Antenna effective area (m²)
 η_total = Total system efficiency
```

### System Efficiency
```
η_total = η_antenna × η_matching × η_rectifier × η_filter

Typical values:
 η_antenna = 0.75-0.85
 η_matching = 0.85-0.95
 η_rectifier = 0.30-0.70 (depends on power level)
 η_filter = 0.90-0.95
 η_total ≈ 0.25-0.45 (25-45%)
```

### Rectifier Efficiency vs Power
```
Low power (<10 μW): 10-25%
Moderate (10-100 μW): 30-45%
Good (100-1000 μW): 45-60%
High (>1000 μW): 60-75%
```

## Frequency Bands

| Band | Frequency | Wavelength | Antenna Size | Power Density |
|------|-----------|------------|--------------|---------------|
| **FM Radio** | 88-108 MHz | 2.8-3.4 m | 75 cm | 0.5-10 μW/m² |
| **TV VHF** | 174-216 MHz | 1.4-1.7 m | 35-42 cm | 0.5-5 μW/m² |
| **TV UHF** | 470-806 MHz | 37-64 cm | 9-16 cm | 1-10 μW/m² |
| **Cell 700** | 700-800 MHz | 37-43 cm | 9-11 cm | 5-50 μW/m² |
| **Cell 850** | 850 MHz | 35 cm | 8.8 cm | 5-30 μW/m² |
| **Cell 1900** | 1.9 GHz | 16 cm | 4 cm | 5-40 μW/m² |
| **WiFi 2.4** | 2.4 GHz | 12.5 cm | 3.1 cm | 10-100 μW/m² |
| **Cell 2600** | 2.6 GHz | 11.5 cm | 2.9 cm | 5-50 μW/m² |
| **5G** | 3.5 GHz | 8.6 cm | 2.1 cm | 10-100 μW/m² |
| **WiFi 5** | 5.0 GHz | 6 cm | 1.5 cm | 5-50 μW/m² |

## Typical Power Densities by Location

| Location | Combined RF | Notes |
|----------|-------------|-------|
| **Rural home** | 5-20 μW/m² | Weak cellular, own WiFi |
| **Suburban** | 20-50 μW/m² | Moderate cellular, WiFi |
| **Urban apt** | 50-150 μW/m² | Multiple WiFi, good cellular |
| **Near cell tower** | 200-1000 μW/m² | Strong cellular dominant |
| **Shopping mall** | 200-500 μW/m² | Dense WiFi, many devices |
| **Airport** | 300-800 μW/m² | Excellent coverage |

## Device Power Requirements

| Device | Power | Duty Cycle | Average |
|--------|-------|------------|---------|
| **Temp sensor** | 10 μW | 100% | 10 μW |
| **Motion detector** | 50 μW | 10% | 5 μW |
| **E-ink update** | 1 mW | 0.1% | 1 μW avg |
| **MCU sleep** | 1 μW | 90% | 0.9 μW |
| **MCU active** | 10 mW | 10% | 1 mW avg |
| **BLE transmit** | 15 mW | 1% | 150 μW avg |
| **LED (dim)** | 5 mW | 10% | 500 μW avg |
| **WiFi transmit** | 200 mW | 1% | 2 mW avg |
| **iPhone charge** | 5 W | 100% | 5 W |

## Component Selection

### Schottky Diodes
- **HSMS-285x Series** (Avago/Broadcom)
 - V_forward: 0.15-0.35V
 - Frequency: DC-6 GHz
 - Best for: Low-power rectification
- **SMS7630 Series** (Skyworks)
 - V_forward: 0.25-0.40V
 - Frequency: DC-6 GHz
 - Good balance

### Power Management ICs
- **BQ25570** (Texas Instruments)
 - Cold-start: 330 mV
 - Input: 100 mV - 5.5V
 - MPPT: Yes
 - Best for: Energy harvesting

- **AEM10941** (e-peas)
 - Cold-start: 380 mV
 - Input: 10-500 mV
 - MPPT: Yes
 - Best for: Multi-source

### Supercapacitors
- **5.5V, 1-10F** (various brands)
 - Low ESR (< 50 mΩ)
 - Temperature: -40°C to +85°C
 - Purpose: Energy buffer

## Quick Calculations

### Urban Apartment (Typical)
```
Power density: 100 μW/m²
Antenna array: 0.1 m² (10cm × 10cm)
System efficiency: 30%

Harvested = 100 × 0.1 × 0.30 = 3 μW

 Can power: Temperature sensor
 Cannot power: iPhone
```

### Near Cell Tower (Optimal)
```
Power density: 600 μW/m²
Antenna array: 0.25 m² (50cm × 50cm)
System efficiency: 40%

Harvested = 600 × 0.25 × 0.40 = 60 μW

 Can power: E-ink display, IoT node
 Can power: LED (burst mode with supercap)
 Cannot power: iPhone charging
```

### Energy Storage Calculation
```
Supercap: 10F at 3.3V
Stored energy = ½CV² = 0.5 × 10 × 3.3² = 54.5 J

If harvesting 60 μW:
 Charge time = 54.5 J / (60×10⁻⁶ W) = 908,333 s = 10.5 days

If load needs 10 mW burst for 1 second:
 Energy = 10 mW × 1s = 10 mJ = 0.01 J
 Bursts available = 54.5 / 0.01 = 5,450 bursts
 Recharge time per burst = 0.01 / (60×10⁻⁶) = 167 seconds
 Burst rate = 1 burst per 3 minutes (sustainable)
```

## Success Criteria

### IoT Sensor (FEASIBLE)
- [x] Power requirement: < 100 μW
- [x] Harvested power: 3-130 μW
- [x] Location: Urban/suburban
- [x] Size: < 15cm × 15cm
- [x] Cost: < $100 DIY, < $50 production
- **ACHIEVABLE**

### Smartphone Charging (NOT FEASIBLE)
- [ ] Power requirement: 5,000,000 μW
- [ ] Harvested power: 3-130 μW
- [ ] Gap: 50,000× - 1,000,000×
- **REQUIRES BREAKTHROUGH**

## Decision Matrix

| If you need... | Then... |
|----------------|---------|
| **< 10 μW continuous** | RF harvesting perfect |
| **10-100 μW continuous** | RF harvesting good |
| **100 μW - 1 mW continuous** | RF + Solar hybrid |
| **1-10 mW continuous** | Primarily solar, RF supplemental |
| **> 10 mW continuous** | Use dedicated power source |
| **> 100 mW continuous** | RF harvesting not suitable |

## Best Practices

### Antenna Design
1. Use PCB antennas for compactness
2. Tune each antenna to center frequency
3. Maximize effective aperture within size constraints
4. Consider antenna array for directionality
5. Isolate antennas to prevent coupling

### Rectifier Design
1. Use Dickson multiplier for low power (4-8 stages)
2. Select Schottky diodes with lowest V_threshold
3. Optimize capacitor values (100 pF - 1 nF typical)
4. Match impedance at each stage
5. Minimize PCB parasitics

### Power Management
1. Use cold-start capable IC (< 400 mV)
2. Implement MPPT for maximum efficiency
3. Use supercapacitor for buffering
4. Protect battery from over/under voltage
5. Monitor harvesting performance

### System Optimization
1. Target strongest frequency bands (cellular, WiFi)
2. Position device near RF sources
3. Use large ground plane
4. Minimize losses in connections
5. Test in real environment (lab ≠ real world)

## Common Mistakes to Avoid

 **Expecting too much power** - Ambient RF is weak!
 **Ignoring efficiency** - Every stage has losses
 **Single-band only** - Multi-band is essential
 **Poor impedance matching** - Wastes 50%+ power
 **Undersized supercap** - Cannot handle bursts
 **No MPPT** - Leaves 20-40% on table
 **Lab-only testing** - Real world is different

## Resources

### Simulation Tools
- **HFSS** - Antenna simulation (commercial)
- **CST Studio** - EM simulation (commercial)
- **4NEC2** - Antenna modeling (free)
- **LTSpice** - Circuit simulation (free)
- **KiCad** - PCB design (free)

### Key Papers
1. "Ambient RF Energy Harvesting" - Vullers et al. (2010)
2. "Rectenna Design and Development" - Brown (1984)
3. "Ambient Backscatter" - UW (2013)
4. "Multi-band RF Energy Harvesting" - Various

### Datasheets
- BQ25570: ti.com/product/BQ25570
- HSMS-285x: broadcom.com
- AEM10941: e-peas.com

## Quick Checklist

### Before Starting
- [ ] Understand power requirements
- [ ] Survey RF environment
- [ ] Set realistic expectations
- [ ] Budget for prototype ($200-300)
- [ ] Have simulation tools ready

### Design Phase
- [ ] Simulate antennas (target 75%+ efficiency)
- [ ] Design rectifier circuit (target 40%+ efficiency)
- [ ] Layout PCB (minimize parasitics)
- [ ] Select components (low threshold, low ESR)
- [ ] Plan testing procedure

### Build Phase
- [ ] Order PCB from reputable manufacturer
- [ ] Source quality components
- [ ] Careful soldering (RF sensitive!)
- [ ] Test each stage independently
- [ ] Assemble complete system

### Test Phase
- [ ] Measure antenna resonance (VNA)
- [ ] Test rectifier with signal generator
- [ ] Measure harvested power in various locations
- [ ] Compare to simulations
- [ ] Optimize and iterate

### Deployment
- [ ] Select optimal location
- [ ] Monitor performance over time
- [ ] Document real-world results
- [ ] Share findings with community

---

## The One-Sentence Summary

**RF energy harvesting works perfectly for ultra-low-power IoT devices (<100 μW), but needs 100,000× more power for smartphone charging.**

**Focus on IoT. Perfect the technology. Then push boundaries.** 
