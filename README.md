# ResoCharge: Ambient RF Energy Harvesting System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/bhim-shrestha/resocha?style=social)](https://github.com/bhim-shrestha/resocha/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/bhim-shrestha/resocha?style=social)](https://github.com/bhim-shrestha/resocha/network/members)
[![Status](https://img.shields.io/badge/Status-Research%20Phase-yellow)](https://github.com/bhim-shrestha/resocha)
[![Technology](https://img.shields.io/badge/Technology-RF%20Harvesting-blue)](https://github.com/bhim-shrestha/resocha)
[![Inspired By](https://img.shields.io/badge/Inspired%20By-Nikola%20Tesla-purple)](https://github.com/bhim-shrestha/resocha)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/bhim-shrestha/resocha/blob/main/CONTRIBUTING.md)

> *"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."* — Nikola Tesla

## About the Name

**ResoCharge** combines "Resonance" and "Charge" - reflecting the core principle of resonant frequency matching in Radio Frequency (RF) energy harvesting. The name honors Nikola Tesla's pioneering work in resonant inductive coupling while emphasizing our focus on ambient energy capture through multi-band resonant rectenna systems.

## Project Vision

Harvest omnipresent electromagnetic energy from ambient RF sources (WiFi, cellular networks, radio broadcasts, TV signals) to create perpetual power sources for ultra-low-power devices. This project explores the feasibility of Tesla's wireless power transmission vision, adapted for the modern wireless world.

## Documentation

This repository contains comprehensive research and technical documentation:

1. **[01_WIRELESS_CHARGING_DEEP_DIVE.md](01_WIRELESS_CHARGING_DEEP_DIVE.md)**
 - How iPhone Qi wireless charging works
 - Electromagnetic induction principles
 - Frequency and power characteristics
 - Why it doesn't work at distance

2. **[02_FREQUENCY_AND_ENERGY_PHYSICS.md](02_FREQUENCY_AND_ENERGY_PHYSICS.md)**
 - Planck-Einstein relation (E = h × f)
 - Electromagnetic spectrum analysis
 - Power density calculations
 - Energy conversion mechanisms

3. **[03_AMBIENT_RF_SOURCES_CATALOG.md](03_AMBIENT_RF_SOURCES_CATALOG.md)**
 - Complete catalog of RF sources in common environments
 - Power density measurements by location
 - Frequency bands and availability
 - Best locations for harvesting

4. **[04_TESLA_WIRELESS_POWER_RESEARCH.md](04_TESLA_WIRELESS_POWER_RESEARCH.md)**
 - Tesla's resonant inductive coupling
 - Wardenclyffe Tower project
 - Modern validation (MIT WiTricity)
 - Relevant principles for our project

5. **[05_RECTENNA_TECHNOLOGY_DEEP_DIVE.md](05_RECTENNA_TECHNOLOGY_DEEP_DIVE.md)**
 - Rectifying antenna (rectenna) principles
 - Multi-band harvesting architectures
 - State-of-the-art performance
 - Practical design considerations

6. **[06_FEASIBILITY_ANALYSIS_AND_RECOMMENDATIONS.md](06_FEASIBILITY_ANALYSIS_AND_RECOMMENDATIONS.md)**
 - Complete feasibility study
 - Economic analysis
 - Recommendations and roadmap
 - Realistic applications

7. **[REFERENCES.md](REFERENCES.md)** 
 - 45+ academic papers and sources
 - Technical standards & specifications
 - Industry reports & market data
 - Proper citations and bibliography

8. **[WRITING_STYLE_GUIDE.md](WRITING_STYLE_GUIDE.md)**
 - Professional and academic writing standards
 - Citation requirements and formats
 - Technical documentation guidelines
 - Style enforcement for all contributors

## Key Findings

### What Works (Proven)

- **Physics is sound**: RF energy can be harvested from ambient sources
- **Technology exists**: Rectenna technology is mature (since 1960s)
- **Multi-band helps**: Harvesting multiple frequencies increases power
- **Perfect for IoT**: Ultra-low-power sensors can run indefinitely

### The Challenge

**Power Density Gap:**
- iPhone needs: 5-15 W for charging
- Typical ambient RF: 10-100 μW/m² available
- Best case harvest: 1-130 μW realistic
- **Gap: ~100,000× too low for smartphone charging**

### Realistic Applications

| Application | Power Need | Feasibility | Status |
|-------------|------------|-------------|--------|
| **Temperature sensor** | 10 μW | Excellent | Proven |
| **Motion detector** | 20 μW | Excellent | Proven |
| **E-ink display** | 50 μW | Good | Proven |
| **Battery-free IoT** | 10-100 μW | Excellent | **Best Target** |
| **LED lighting** | 5 mW | Supplemental | Challenging |
| **Smartphone charging** | 5000 mW | Not feasible | Requires breakthrough |

## Technical Design

### Multi-Band Rectenna Architecture

```
RF Sources (Ambient) Harvester System Output
 FM Radio 
 88-108 MHz 6-Band Super- 
 Antenna Dickson cap 
 > Array >Voltage> Buffer 
 Multiplier 
 TV Broadcast Impedance Charge 
 470-806 MHz Matching Power Control 
 Combiner 
 Multi-Stage Battery 
 Rectifiers / Load 
 Cellular 
 700-2600 MHz 30-40% 3.3-5V 
 Efficiency Output 
 WiFi 2.4/5 GHz 
 2.4-5.8 GHz 
 5G 
 3.5 GHz 

```

### Expected Performance

| Scenario | Power Harvested | Applications |
|----------|-----------------|--------------|
| **Urban Apartment** | 3-10 μW | Temp sensor, low-power MCU |
| **Near Cell Tower** | 60-130 μW | E-ink display, IoT node |
| **Rural Area** | 0.5-3 μW | Ultra-low-power sensor only |

## Simulation Tool

**File:** `resocharge_simulator.py`

Python simulator for calculating harvested power based on:
- RF source power densities
- Antenna configurations
- Rectifier efficiency curves
- System losses

**Run the simulator:**
```bash
python resocharge_simulator.py
```

**Output:**
- Power analysis for 3 scenarios
- Energy per day calculations
- Device capability assessment
- Comparison charts

## Bill of Materials (Prototype)

| Component | Quantity | Est. Cost | Notes |
|-----------|----------|-----------|-------|
| PCB antennas (6 types) | 1 set | $50-100 | FM, TV, Cell, WiFi, 5G |
| Schottky diodes (HSMS-285C) | 50 pcs | $20 | Low threshold voltage |
| Capacitors (assorted) | 1 set | $15 | 100pF - 10μF |
| 4-layer PCB | 1 | $30-50 | Custom design |
| BQ25570 power IC | 1 | $5-10 | Energy harvesting PMIC |
| 10F supercapacitor | 1 | $10-20 | Energy buffer |
| Enclosure | 1 | $20 | Weather-proof |
| Misc. components | - | $30 | Wire, connectors, etc. |
| **TOTAL** | | **$180-265** | First prototype |

## Development Roadmap

### Phase 1: Research & Simulation COMPLETE
- [x] Study wireless charging technology
- [x] Analyze frequency and energy physics
- [x] Catalog ambient RF sources
- [x] Research Tesla's wireless power work
- [x] Deep dive into rectenna technology
- [x] Create feasibility analysis
- [x] Build Python simulator

### Phase 2: Design & Prototyping (3-6 months)
- [ ] Design antenna array (HFSS/CST simulation)
- [ ] Design rectifier circuit (LTSpice simulation)
- [ ] Create PCB layout (KiCad/Altium)
- [ ] Order components
- [ ] Fabricate PCB
- [ ] Assemble prototype
- [ ] Initial testing

### Phase 3: Testing & Optimization (6-12 months)
- [ ] Measure real-world RF power in various locations
- [ ] Test harvester performance
- [ ] Optimize impedance matching
- [ ] Refine antenna designs
- [ ] Improve rectifier efficiency
- [ ] Document results

### Phase 4: Application Development (12-18 months)
- [ ] Design IoT sensor node
- [ ] Integrate harvester with application
- [ ] Field testing (multiple locations)
- [ ] Reliability testing
- [ ] Prepare for production

### Phase 5: Commercialization (18+ months)
- [ ] Finalize design for manufacturing
- [ ] Seek partnerships
- [ ] Consider patent applications
- [ ] Launch product (IoT sensors)
- [ ] Explore hybrid approaches (RF+Solar)

## Educational Value

This project demonstrates:
- **Electromagnetic theory** in practice
- **RF engineering** principles
- **Power electronics** design
- **Energy harvesting** techniques
- **System optimization** strategies
- **Physics-to-product** development

Perfect for:
- Engineering students
- Makers and hobbyists
- RF engineers
- Sustainability enthusiasts
- Tesla fans 

## Key Insights

### What Tesla Taught Us
1. **Resonance is key** - Matching frequencies maximizes efficiency
2. **Multiple frequencies** can coexist and be harvested
3. **Environment contains energy** - It's everywhere, just tap it
4. **Persistence pays** - Breakthrough takes time

### What Modern Physics Adds
1. **Quantum mechanics** - Photon energy E = h × f
2. **Efficiency matters** - Every stage of conversion has losses
3. **Power density** - Fundamental limitation of ambient harvesting
4. **Multi-band approach** - Additive power from multiple sources

## Future Possibilities

### Near-Term (2-5 years)
- Battery-free IoT sensor networks
- Self-powered smart home devices
- Maintenance-free building sensors
- Hybrid RF+Solar chargers (5-20% boost)

### Mid-Term (5-10 years)
- Dense 5G increases ambient power 5-10×
- Advanced metamaterials concentrate RF 10-100×
- Improved rectifier efficiency (>70% at low power)
- Practical trickle charging for wearables

### Long-Term (10+ years)
- Breakthrough: Room-scale resonant cavities (Disney research path)
- Quantum rectification for ultra-high efficiency
- Smartphone cases with meaningful charging contribution
- Wireless power as ubiquitous as wireless data

## Contributing

**We welcome contributions from everyone!** Whether you're an RF engineer, student, maker, or just curious about wireless power, there's a place for you here.

**Ways to contribute:**
- Report bugs or issues
- Suggest new features or improvements
- Improve documentation (including citations!)
- Share real-world testing data
- Submit hardware designs
- Improve the simulator
- Translate documentation
- Add references to REFERENCES.md

**See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.**

**High-priority contributions:**
- Real-world RF power measurements from different locations
- PCB designs and hardware prototypes
- IoT sensor implementations
- Testing data validation
- Academic paper citations and verification

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- Use it for any purpose (personal, commercial, research)
- Modify and distribute freely
- Private use allowed
- Must include copyright and license notice
- No warranty provided

**If you use this in your work:**
- Please give credit (link back to this repo)
- Share your improvements (but not required)
- Let us know what you built! We'd love to hear about it

## Acknowledgments

- **Nikola Tesla** - The original wireless power visionary
- **William C. Brown** - Invented the rectenna (1960s)
- **MIT WiTricity Team** - Modern resonant wireless power
- **University of Washington** - Ambient backscatter research
- **Powercast** - Commercial RF harvesting products

## Contact & Community

**Project:** ResoCharge 
**Status:** Research & Development Phase 
**Started:** November 2025

**Get Involved:**
- [GitHub Discussions](https://github.com/bhim-shrestha/resocha/discussions) - Ask questions, share ideas
- [Issues](https://github.com/bhim-shrestha/resocha/issues) - Report bugs, request features
- [Pull Requests](https://github.com/bhim-shrestha/resocha/pulls) - Contribute code or docs
- [Star this repo](https://github.com/bhim-shrestha/resocha) - Show your support!

**Stay Updated:**
- Watch this repo for updates
- Check the [Releases](https://github.com/bhim-shrestha/resocha/releases) page
- Follow project milestones

---

## Star History

If you find this project useful, please consider giving it a star! 

[![Star History Chart](https://api.star-history.com/svg?repos=bhim-shrestha/resocha&type=Date)](https://star-history.com/#bhim-shrestha/resocha&Date)

---

## Support This Project

If this project helps your research or inspires your work:
- Star the repository
- Report bugs and help improve it
- Share it with others who might be interested
- Contribute code or documentation
- Sponsor development (GitHub Sponsors - coming soon)

---

*"The present is theirs; the future, for which I really worked, is mine."* — Nikola Tesla

 **Let's harvest the invisible energy sea together!** 

---

**Made with by [Bhim Shrestha](https://github.com/bhim-shrestha)**
