# iPhone Wireless Charging: Deep Technical Analysis

## 1. How iPhone Wireless Charging Works

### Core Technology: Qi Standard (Wireless Power Consortium)
iPhone uses the **Qi (pronounced "chee") standard** for wireless charging, based on **electromagnetic induction**.

### Physical Principles

#### Electromagnetic Induction (Faraday's Law)
```
ε = -N × dΦ/dt

Where:
- ε = Induced EMF (voltage)
- N = Number of coil turns
- Φ = Magnetic flux
- t = Time
```

**Process:**
1. **Transmitter Coil (Charging Pad)**: AC current flows through copper coil
2. **Magnetic Field Generation**: Creates oscillating magnetic field
3. **Receiver Coil (iPhone)**: Magnetic field induces AC current
4. **Rectification**: AC → DC conversion
5. **Voltage Regulation**: Charges battery at correct voltage

### Technical Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Frequency** | 110-205 kHz | Qi baseline standard |
| **iPhone Specific** | ~127.7 kHz | Typical operating frequency |
| **Power Output** | 5W, 7.5W, 15W | Depends on charger |
| **Efficiency** | 70-80% | Energy loss as heat |
| **Distance** | 5-7mm max | Very short range |
| **Coil Type** | Copper wire | Multiple turns |

### Energy Transfer Mechanism

**Near-Field Inductive Coupling:**
- **NOT** far-field radiation
- **Requires close proximity** (magnetic coupling coefficient k > 0.1)
- Energy confined to near-field region
- Falls off rapidly with distance (1/r³)

### Power Formula
```
P = η × V × I

Where:
- P = Power transferred (Watts)
- η = Efficiency (0.7-0.8)
- V = Voltage
- I = Current
```

### Why This Works at Short Range
1. **Strong magnetic coupling** between coils
2. **High mutual inductance** (M)
3. **Resonant frequency matching** optimizes power transfer
4. **Quality factor (Q)** determines efficiency

### Key Components in iPhone
1. **Receiver Coil**: Multi-turn copper coil
2. **Rectifier Circuit**: AC to DC conversion (diode bridge)
3. **Power Management IC**: Voltage regulation
4. **Shielding**: Ferrite sheet (directs magnetic field)
5. **NFC Coil**: Often integrated with charging coil

## 2. Critical Limitations for Distance Charging

### Inverse Cube Law Problem
```
B ∝ 1/r³ (for near-field)

Magnetic field strength drops extremely fast with distance
```

**Example:**
- At 5mm: 100% field strength
- At 10mm: 12.5% field strength
- At 20mm: 1.56% field strength
- At 1 meter: Essentially zero

### Why Long-Range Inductive Charging Doesn't Work
1. **Magnetic field decay**: Too rapid
2. **Efficiency plummets**: Below 1% beyond 10cm
3. **Power requirement**: Would need megawatts for meter-range
4. **Safety concerns**: Dangerous magnetic field levels
5. **Interference**: Disrupts other electronics

## 3. The Frequency Question

**Does the 127.7 kHz frequency carry energy?**

**YES** - but only in the near-field through magnetic induction, not as propagating waves.

### Energy in Electromagnetic Fields
```
Energy Density (u) = (ε₀E²)/2 + (B²)/(2μ₀)

Where:
- E = Electric field
- B = Magnetic field
- ε₀ = Permittivity of free space
- μ₀ = Permeability of free space
```

### Important Distinction
- **Near-field** (kHz range): Energy stored in reactive field, not radiated
- **Far-field** (MHz-GHz range): Energy propagates as electromagnetic waves

## 4. Why Qi Frequency Can't Be "Harvested" Remotely

### Wavelength Analysis
```
λ = c/f

Where:
- λ = Wavelength
- c = Speed of light (3×10⁸ m/s)
- f = Frequency

For 127.7 kHz:
λ = 300,000,000 / 127,700 = 2,349 meters (2.3 km)
```

### Near-Field vs Far-Field Boundary
```
r_boundary ≈ λ/(2π)

For 127.7 kHz:
r_boundary ≈ 2,349 / 6.28 ≈ 374 meters
```

**Below 374m**: Near-field (reactive, non-radiating)
**Above 374m**: Far-field (radiating)

**In practice:** Qi chargers operate at millimeters - firmly in non-radiating near-field.

## 5. Power Levels

### iPhone Wireless Charging Power
- **Input to pad**: 10-20W (from wall)
- **Magnetic coupling**: 7.5-15W
- **Delivered to battery**: 5-10W
- **Loss as heat**: 3-5W

### Energy Per Charge
```
iPhone 14 Pro battery: 3,200 mAh × 3.8V = 12.16 Wh

At 7.5W charging:
Time = 12.16 Wh / 7.5 W ≈ 1.6 hours
```

## Summary

**Key Findings:**
1. iPhone wireless charging uses **electromagnetic induction** at ~127.7 kHz
2. Frequency does carry energy in the **magnetic field**
3. This energy is **NOT radiating** - it's confined to near-field
4. Cannot be harvested beyond ~10mm distance efficiently
5. **Different frequencies** (MHz-GHz) DO radiate and can be harvested
6. **Next Step**: Study ambient RF energy from WiFi, cellular, radio broadcasts

---

**Conclusion for Ambient Charging Project:**
We need to look at **far-field electromagnetic radiation** (radio frequencies) rather than near-field inductive coupling for distance energy harvesting.

**Promising Frequency Ranges:**
- FM Radio: 88-108 MHz
- WiFi: 2.4 GHz, 5 GHz
- Cellular: 700 MHz - 2.6 GHz
- TV Broadcasts: 470-806 MHz

These frequencies **DO propagate through space** and can be captured with antennas (rectennas).
