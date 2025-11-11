# ResoCharge: Multi-Band RF Energy Harvester
# Power Calculation and System Simulation
# 
# What this does:
# - Simulates collecting energy from WiFi, cellular, radio signals around us
# - Calculates how much power we can get (spoiler: very little!)
# - Shows what devices we could theoretically power
# - Compares different locations (urban, near tower, rural)

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Tuple
import json

@dataclass
class RFSource:
    """
    Represents an RF energy source (WiFi, cellular, radio, etc.)
    
    Think of this as a radio tower or WiFi router sending out signals.
    We can capture tiny amounts of energy from these signals.
    
    Example: WiFi router at 2450 MHz with 30 μW/m² power density
    """
    name: str  # Example: "WiFi 2.4GHz", "Cellular 1900MHz"
    frequency_mhz: float  # What frequency it transmits at (like radio station 100.1 FM)
    power_density_uw_per_m2: float  # How much power per square meter (very small!)
    availability: float  # How often it's on (1.0 = always, 0.5 = half the time)
    
@dataclass
class AntennaConfig:
    """
    Antenna configuration for catching RF signals at specific frequencies
    
    Think of this as a radio antenna, but tiny. Each antenna is tuned
    to one frequency (like tuning your radio to a specific station).
    
    Example: Antenna tuned to 2450 MHz with 0.006 m² area (small!)
    """
    frequency_mhz: float  # What frequency this antenna is tuned to
    effective_area_m2: float  # How big the antenna is (bigger = more power)
    efficiency: float  # How good it is at catching signals (0.0 to 1.0, where 1.0 = perfect)
    
@dataclass
class RectifierConfig:
    """
    Rectifier circuit configuration - converts AC to DC
    
    RF signals are AC (alternating current), but devices need DC (direct current).
    The rectifier converts AC → DC, but loses a lot of power in the process.
    
    Think of it like a water filter - water goes in, filtered water comes out,
    but some water is lost in the filter.
    """
    type: str  # Type of rectifier: 'schottky', 'cmos', 'dickson'
    stages: int  # How many conversion stages (more stages = better but more complex)
    threshold_voltage: float  # Minimum voltage needed to work
    efficiency_at_power: Dict[float, float]  # How efficient at different power levels

class RFEnergyHarvester:
    """
    The main RF Energy Harvester system
    
    This simulates a device that:
    1. Has multiple antennas to catch RF signals
    2. Converts those signals to usable power
    3. Calculates how much power we actually get
    
    Think of it as a super-advanced "energy collector" that tries to power
    devices from WiFi, cellular, and radio signals in the air.
    """
    
    def __init__(self, name: str = "ResoCharge", enable_resonance: bool = False):
        self.name = name
        self.rf_sources: List[RFSource] = []  # List of all RF sources around us
        self.antennas: List[AntennaConfig] = []  # List of antennas we have
        self.rectifier: RectifierConfig = None  # The AC→DC converter
        self.matching_efficiency: float = 0.90  # How well antenna connects to rectifier (90%)
        self.filter_efficiency: float = 0.95  # How well we filter the signal (95%)
        self.enable_resonance: bool = enable_resonance  # Multi-band resonance boost
        self.resonance_boost: float = 1.5 if enable_resonance else 1.0  # 50% boost when enabled
        
    def add_rf_source(self, source: RFSource):
        """Add an RF energy source to the environment"""
        self.rf_sources.append(source)
        
    def add_antenna(self, antenna: AntennaConfig):
        """Add an antenna to the harvester"""
        self.antennas.append(antenna)
        
    def set_rectifier(self, rectifier: RectifierConfig):
        """Configure the rectifier"""
        self.rectifier = rectifier
        
    def calculate_received_power(self, source: RFSource, antenna: AntennaConfig) -> float:
        """
        Calculate power received by antenna from RF source (in microwatts)
        
        This is like calculating how much rain water a bucket catches:
        - Rain density (power_density) × Bucket size (antenna_area) × 
          Bucket efficiency (holes in bucket?) × Time it rains (availability)
        """
        # Check if antenna frequency matches the source (like tuning a radio)
        if not self._frequency_match(source.frequency_mhz, antenna.frequency_mhz):
            return 0.0  # Wrong frequency = no power received
            
        # Calculate received power using physics formula
        # Power = power_density × effective_area × antenna_efficiency × availability
        power_uw = (source.power_density_uw_per_m2 *  # How strong the signal is
                   antenna.effective_area_m2 *  # How big our antenna is
                   antenna.efficiency *  # How good our antenna is
                   source.availability)  # How often the source is on
        
        # Apply resonance boost if enabled (simulates multi-band resonance improvements)
        power_uw *= self.resonance_boost
        
        return power_uw
        
    def _frequency_match(self, source_freq: float, antenna_freq: float, tolerance: float = 0.15) -> bool:
        """
        Check if source frequency matches antenna (within tolerance)
        
        Antennas are like tuning forks - they only respond to specific frequencies.
        This checks if the source frequency is close enough to the antenna frequency.
        
        tolerance = 0.15 means we allow ±15% difference
        Example: Antenna at 2450 MHz works for 2082-2817 MHz
        """
        return abs(source_freq - antenna_freq) / antenna_freq < tolerance
        
    def get_rectifier_efficiency(self, input_power_uw: float) -> float:
        """
        Get rectifier efficiency based on input power level
        
        Rectifiers work differently at different power levels:
        - Very low power (0.1 μW): Only 10% efficient (loses 90%!)
        - Low power (1 μW): 25% efficient
        - Moderate power (10 μW): 40% efficient
        - Good power (100 μW): 55% efficient
        
        This function interpolates between these levels.
        """
        if not self.rectifier:
            return 0.5  # Default 50% if no rectifier configured
            
        # Get the predefined power levels and their efficiencies
        power_levels = sorted(self.rectifier.efficiency_at_power.keys())
        
        # If power is below lowest level, use lowest efficiency
        if input_power_uw <= power_levels[0]:
            return self.rectifier.efficiency_at_power[power_levels[0]]
        # If power is above highest level, use highest efficiency
        if input_power_uw >= power_levels[-1]:
            return self.rectifier.efficiency_at_power[power_levels[-1]]
            
        # Otherwise, interpolate between two closest power levels
        for i in range(len(power_levels) - 1):
            if power_levels[i] <= input_power_uw <= power_levels[i+1]:
                p1, p2 = power_levels[i], power_levels[i+1]
                e1 = self.rectifier.efficiency_at_power[p1]
                e2 = self.rectifier.efficiency_at_power[p2]
                # Linear interpolation formula
                return e1 + (e2 - e1) * (input_power_uw - p1) / (p2 - p1)
                
        return 0.5  # Fallback
        
    def calculate_total_harvested_power(self) -> Dict:
        """Calculate total harvested power from all sources"""
        results = {
            'sources': [],
            'total_received_uw': 0.0,
            'total_harvested_uw': 0.0,
            'total_harvested_mw': 0.0,
            'system_efficiency': 0.0
        }
        
        total_received = 0.0
        
        # Calculate power from each source through each antenna
        for source in self.rf_sources:
            for antenna in self.antennas:
                received_power = self.calculate_received_power(source, antenna)
                if received_power > 0:
                    total_received += received_power
                    
                    # Calculate conversion efficiency
                    rectifier_eff = self.get_rectifier_efficiency(received_power)
                    
                    # Total efficiency chain
                    total_eff = (antenna.efficiency * 
                               self.matching_efficiency * 
                               rectifier_eff * 
                               self.filter_efficiency)
                    
                    harvested_power = received_power * total_eff
                    
                    results['sources'].append({
                        'source': source.name,
                        'frequency_mhz': source.frequency_mhz,
                        'received_uw': received_power,
                        'harvested_uw': harvested_power,
                        'efficiency': total_eff
                    })
                    
        results['total_received_uw'] = total_received
        results['total_harvested_uw'] = sum(s['harvested_uw'] for s in results['sources'])
        results['total_harvested_mw'] = results['total_harvested_uw'] / 1000.0
        
        if total_received > 0:
            results['system_efficiency'] = results['total_harvested_uw'] / total_received
        
        return results
        
    def calculate_energy_per_day(self, harvested_power_uw: float) -> Dict:
        """Calculate energy harvested per day"""
        power_mw = harvested_power_uw / 1000.0
        
        # Energy in various units
        energy_mwh = power_mw * 24  # milliwatt-hours
        energy_wh = energy_mwh / 1000.0  # watt-hours
        energy_j = power_mw * 24 * 3600 / 1000.0  # joules
        
        return {
            'power_uw': harvested_power_uw,
            'power_mw': power_mw,
            'energy_per_day_mwh': energy_mwh,
            'energy_per_day_wh': energy_wh,
            'energy_per_day_j': energy_j
        }
        
    def estimate_charging_capability(self, harvested_power_uw: float) -> Dict:
        """Estimate what can be powered or charged"""
        power_mw = harvested_power_uw / 1000.0
        
        # Device power requirements (approximate)
        devices = {
            'Temperature sensor': 0.01,  # 10 μW
            'E-ink display (static)': 0.05,  # 50 μW
            'Low-power MCU (sleep)': 0.001,  # 1 μW
            'Low-power MCU (active)': 1.0,  # 1 mW
            'LED (dimmed)': 5.0,  # 5 mW
            'Bluetooth LE transmit': 10.0,  # 10 mW
            'WiFi transmit': 100.0,  # 100 mW
            'iPhone charging': 5000.0  # 5W
        }
        
        capabilities = {}
        for device, required_mw in devices.items():
            if power_mw >= required_mw:
                capabilities[device] = 'Yes - Continuous'
            elif power_mw >= required_mw * 0.1:
                duty_cycle = (power_mw / required_mw) * 100
                capabilities[device] = f'Partial - {duty_cycle:.1f}% duty cycle'
            else:
                capabilities[device] = 'No'
                
        # iPhone charging time
        iphone_battery_wh = 12.16  # iPhone 14 Pro
        energy_per_day = self.calculate_energy_per_day(harvested_power_uw)
        days_to_charge = iphone_battery_wh / energy_per_day['energy_per_day_wh'] if energy_per_day['energy_per_day_wh'] > 0 else float('inf')
        
        return {
            'capabilities': capabilities,
            'iphone_charge_time_days': days_to_charge,
            'iphone_charge_time_years': days_to_charge / 365.25
        }
        
    def generate_report(self) -> str:
        """Generate a comprehensive report"""
        results = self.calculate_total_harvested_power()
        energy = self.calculate_energy_per_day(results['total_harvested_uw'])
        capabilities = self.estimate_charging_capability(results['total_harvested_uw'])
        
        report = f"""
{'='*70}
{self.name} - RF Energy Harvesting Analysis Report
{'='*70}

SYSTEM CONFIGURATION
{'-'*70}
RF Sources: {len(self.rf_sources)}
Antennas: {len(self.antennas)}
Matching Efficiency: {self.matching_efficiency*100:.1f}%
Filter Efficiency: {self.filter_efficiency*100:.1f}%
Multi-Band Resonance: {'ENABLED (1.5x boost)' if self.enable_resonance else 'DISABLED'}

POWER ANALYSIS
{'-'*70}
Total Received Power:    {results['total_received_uw']:.2f} μW
Total Harvested Power:   {results['total_harvested_uw']:.2f} μW ({results['total_harvested_mw']:.4f} mW)
Overall System Efficiency: {results['system_efficiency']*100:.1f}%

POWER BREAKDOWN BY SOURCE
{'-'*70}
"""
        for source in results['sources']:
            report += f"{source['source']:20s} @ {source['frequency_mhz']:8.1f} MHz: "
            report += f"{source['harvested_uw']:8.2f} μW (eff: {source['efficiency']*100:5.1f}%)\n"
            
        report += f"""
ENERGY PER DAY
{'-'*70}
Energy per day:  {energy['energy_per_day_mwh']:.3f} mWh
                 {energy['energy_per_day_wh']:.6f} Wh
                 {energy['energy_per_day_j']:.2f} Joules

DEVICE CAPABILITIES
{'-'*70}
"""
        for device, capability in capabilities['capabilities'].items():
            report += f"{device:30s}: {capability}\n"
            
        report += f"""
iPhone Charging Estimate:
  Time to full charge: {capabilities['iphone_charge_time_days']:.0f} days ({capabilities['iphone_charge_time_years']:.1f} years)
  Daily contribution:  {(1/capabilities['iphone_charge_time_days']*100):.4f}% of battery

{'='*70}
"""
        return report

# Predefined environment scenarios
def create_urban_apartment_scenario() -> RFEnergyHarvester:
    """Create typical urban apartment scenario"""
    harvester = RFEnergyHarvester("Urban Apartment")
    
    # RF Sources in urban apartment
    harvester.add_rf_source(RFSource("FM Radio", 100, 2, 1.0))
    harvester.add_rf_source(RFSource("TV Broadcast", 600, 5, 1.0))
    harvester.add_rf_source(RFSource("Cellular 700MHz", 750, 15, 0.9))
    harvester.add_rf_source(RFSource("Cellular 1900MHz", 1900, 15, 0.9))
    harvester.add_rf_source(RFSource("WiFi 2.4GHz", 2450, 30, 0.95))
    harvester.add_rf_source(RFSource("Cellular 2600MHz", 2600, 10, 0.9))
    harvester.add_rf_source(RFSource("5G 3.5GHz", 3500, 20, 0.8))
    harvester.add_rf_source(RFSource("WiFi 5GHz", 5500, 15, 0.8))
    
    # Antennas (compact array - 10cm x 10cm footprint)
    harvester.add_antenna(AntennaConfig(600, 0.015, 0.75))   # TV
    harvester.add_antenna(AntennaConfig(750, 0.01, 0.80))    # Cell 700
    harvester.add_antenna(AntennaConfig(1900, 0.008, 0.80))  # Cell 1900
    harvester.add_antenna(AntennaConfig(2450, 0.006, 0.85))  # WiFi 2.4
    harvester.add_antenna(AntennaConfig(3500, 0.005, 0.80))  # 5G
    harvester.add_antenna(AntennaConfig(5500, 0.003, 0.75))  # WiFi 5
    
    # Rectifier configuration (Dickson 6-stage with Schottky diodes)
    rectifier = RectifierConfig(
        type='dickson',
        stages=6,
        threshold_voltage=0.3,
        efficiency_at_power={
            0.1: 0.10,   # Very low power - poor efficiency
            1.0: 0.25,   # Low power
            10.0: 0.40,  # Moderate power
            100.0: 0.55, # Good power
            1000.0: 0.65 # High power
        }
    )
    harvester.set_rectifier(rectifier)
    
    return harvester

def create_near_cell_tower_scenario() -> RFEnergyHarvester:
    """Create scenario near cellular tower (100m distance)"""
    harvester = RFEnergyHarvester("Near Cell Tower")
    
    # RF Sources - much stronger cellular signals
    harvester.add_rf_source(RFSource("FM Radio", 100, 3, 1.0))
    harvester.add_rf_source(RFSource("TV Broadcast", 600, 10, 1.0))
    harvester.add_rf_source(RFSource("Cellular 700MHz", 750, 200, 0.95))  # Strong!
    harvester.add_rf_source(RFSource("Cellular 1900MHz", 1900, 150, 0.95))  # Strong!
    harvester.add_rf_source(RFSource("WiFi 2.4GHz", 2450, 50, 0.9))
    harvester.add_rf_source(RFSource("Cellular 2600MHz", 2600, 100, 0.95))  # Strong!
    harvester.add_rf_source(RFSource("5G 3.5GHz", 3500, 150, 0.9))  # Strong!
    harvester.add_rf_source(RFSource("WiFi 5GHz", 5500, 30, 0.8))
    
    # Larger antenna array - 25cm x 25cm
    harvester.add_antenna(AntennaConfig(600, 0.04, 0.78))
    harvester.add_antenna(AntennaConfig(750, 0.035, 0.82))
    harvester.add_antenna(AntennaConfig(1900, 0.025, 0.82))
    harvester.add_antenna(AntennaConfig(2450, 0.020, 0.85))
    harvester.add_antenna(AntennaConfig(3500, 0.015, 0.82))
    harvester.add_antenna(AntennaConfig(5500, 0.010, 0.78))
    
    # Better rectifier efficiency due to higher power
    rectifier = RectifierConfig(
        type='dickson',
        stages=6,
        threshold_voltage=0.3,
        efficiency_at_power={
            0.1: 0.10,
            1.0: 0.25,
            10.0: 0.45,   # Better at moderate power
            100.0: 0.60,  # Better at good power
            1000.0: 0.70  # Better at high power
        }
    )
    harvester.set_rectifier(rectifier)
    
    return harvester

def create_rural_scenario() -> RFEnergyHarvester:
    """Create rural/remote scenario"""
    harvester = RFEnergyHarvester("Rural Area")
    
    # RF Sources - weaker signals
    harvester.add_rf_source(RFSource("FM Radio", 100, 1, 1.0))
    harvester.add_rf_source(RFSource("TV Broadcast", 600, 2, 1.0))
    harvester.add_rf_source(RFSource("Cellular 700MHz", 750, 3, 0.7))
    harvester.add_rf_source(RFSource("Cellular 1900MHz", 1900, 2, 0.7))
    harvester.add_rf_source(RFSource("WiFi 2.4GHz (own)", 2450, 10, 1.0))
    harvester.add_rf_source(RFSource("5G 3.5GHz", 3500, 1, 0.5))
    
    # Medium antenna array - 15cm x 15cm
    harvester.add_antenna(AntennaConfig(600, 0.020, 0.75))
    harvester.add_antenna(AntennaConfig(750, 0.015, 0.78))
    harvester.add_antenna(AntennaConfig(1900, 0.012, 0.80))
    harvester.add_antenna(AntennaConfig(2450, 0.010, 0.82))
    harvester.add_antenna(AntennaConfig(3500, 0.008, 0.78))
    
    rectifier = RectifierConfig(
        type='dickson',
        stages=8,  # More stages for lower power
        threshold_voltage=0.3,
        efficiency_at_power={
            0.1: 0.08,
            1.0: 0.20,
            10.0: 0.35,
            100.0: 0.50,
            1000.0: 0.60
        }
    )
    harvester.set_rectifier(rectifier)
    
    return harvester

def compare_scenarios(enable_resonance: bool = False):
    """Compare all scenarios"""
    scenarios = [
        create_urban_apartment_scenario(),
        create_near_cell_tower_scenario(),
        create_rural_scenario()
    ]
    
    # Apply resonance if enabled
    if enable_resonance:
        for scenario in scenarios:
            scenario.enable_resonance = True
            scenario.resonance_boost = 1.5
    
    print("\n" + "="*70)
    print("RESOCHARGE - RF ENERGY HARVESTING SCENARIO COMPARISON")
    if enable_resonance:
        print("🔊 MULTI-BAND RESONANCE: ENABLED (1.5x boost)")
    else:
        print("🔇 MULTI-BAND RESONANCE: DISABLED (standard mode)")
    print("="*70)
    
    comparison_data = []
    
    for harvester in scenarios:
        print(harvester.generate_report())
        results = harvester.calculate_total_harvested_power()
        comparison_data.append({
            'name': harvester.name,
            'power_uw': results['total_harvested_uw'],
            'power_mw': results['total_harvested_mw']
        })
    
    # Create comparison chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    names = [d['name'] for d in comparison_data]
    powers_uw = [d['power_uw'] for d in comparison_data]
    powers_mw = [d['power_mw'] for d in comparison_data]
    
    # Bar chart - μW
    ax1.bar(names, powers_uw, color=['#3498db', '#2ecc71', '#e74c3c'])
    ax1.set_ylabel('Harvested Power (μW)', fontsize=12)
    ax1.set_title('Harvested Power by Scenario', fontsize=14, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Add value labels on bars
    for i, v in enumerate(powers_uw):
        ax1.text(i, v + max(powers_uw)*0.02, f'{v:.1f} μW', 
                ha='center', va='bottom', fontweight='bold')
    
    # Comparison to requirements
    requirements = {
        'Temp Sensor\n(10 μW)': 10,
        'E-ink Display\n(50 μW)': 50,
        'LED\n(5000 μW)': 5000,
        'iPhone\n(5M μW)': 5000000
    }
    
    req_names = list(requirements.keys())
    req_values = list(requirements.values())
    
    ax2.barh(req_names, req_values, color='#95a5a6', alpha=0.6, label='Required')
    
    # Add harvested power lines
    colors = ['#3498db', '#2ecc71', '#e74c3c']
    for i, d in enumerate(comparison_data):
        ax2.axvline(x=d['power_uw'], color=colors[i], linestyle='--', 
                   linewidth=2, label=d['name'])
    
    ax2.set_xlabel('Power (μW, log scale)', fontsize=12)
    ax2.set_xscale('log')
    ax2.set_title('Harvested vs Required Power', fontsize=14, fontweight='bold')
    ax2.legend(loc='lower right')
    ax2.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('scenario_comparison.png', dpi=300, bbox_inches='tight')
    print("\n📊 Comparison chart saved as 'scenario_comparison.png'")
    
    return comparison_data

if __name__ == "__main__":
    print("🔋 ResoCharge RF Energy Harvesting Simulator")
    print("="*70)
    print("\n📖 WHAT THIS SIMULATOR DOES:")
    print("   1. Simulates RF energy collection from WiFi, cellular, radio signals")
    print("   2. Calculates how much power we can harvest (spoiler: very little!)")
    print("   3. Tests 3 scenarios: Urban apartment, Near cell tower, Rural area")
    print("   4. Shows what devices could theoretically run on this power")
    print("   5. Tests with and WITHOUT multi-band resonance technology")
    print("\n⚠️  IMPORTANT: This uses THEORETICAL data, not real measurements!")
    print("   - RF signal strengths are hard-coded estimates")
    print("   - Real-world results would vary based on your location")
    print("   - Physics limits how much power we can harvest (inverse square law)")
    
    # Ask user if they want to test resonance
    print("\n" + "="*70)
    print("RESONANCE MODE SELECTION")
    print("="*70)
    print("\n🔊 Multi-Band Resonance Technology:")
    print("   - Simulates improved antenna design that resonates at multiple frequencies")
    print("   - Captures more energy by optimizing frequency matching")
    print("   - Provides 1.5x power boost (50% improvement)")
    print("   - Represents cutting-edge research (not yet commercial)")
    
    choice = input("\n▶️  Test with resonance enabled? (y/n): ").lower().strip()
    enable_resonance = choice == 'y' or choice == 'yes'
    
    print("\n▶️  Running simulations...\n")
    
    comparison_data = compare_scenarios(enable_resonance=enable_resonance)
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print("\n✅ FEASIBLE APPLICATIONS:")
    print("  • Temperature/humidity sensors (10-50 μW)")
    print("  • Motion detectors (5-20 μW)")
    print("  • E-ink displays (static, 20-50 μW)")
    print("  • Battery-free IoT nodes")
    
    print("\n⚠️  CHALLENGING APPLICATIONS:")
    print("  • Active displays (>100 μW)")
    print("  • Wireless communication (burst mode only)")
    print("  • LEDs (supplemental power only)")
    
    print("\n❌ NOT FEASIBLE (Current Technology):")
    print("  • Smartphone charging")
    print("  • Laptop charging")
    print("  • Any device requiring >1 mW continuous")
    
    print("\n💡 RECOMMENDATIONS:")
    print("  1. Target ultra-low-power IoT sensors (BEST MATCH)")
    print("  2. Use supercapacitor for burst operations")
    print("  3. Position near cellular towers for optimal performance")
    print("  4. Implement multi-band harvesting (6+ frequency bands)")
    print("  5. Consider hybrid RF+Solar for higher power needs")
    
    print("\n🚀 Next step: Build prototype and validate with real measurements!")
    print("="*70 + "\n")
