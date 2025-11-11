# Contributing to ResoCharge

First off, thank you for considering contributing to ResoCharge! 

It's people like you that make ResoCharge such a great project. We welcome contributions from everyone, whether it's:

- Bug reports
- Documentation improvements
- New features
- Code improvements
- Testing and validation
- Ideas and suggestions

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. By participating, you are expected to uphold these values:

- **Be respectful** - Different viewpoints and experiences
- **Be collaborative** - We're all learning together
- **Be patient** - Remember that people have varying levels of expertise
- **Be constructive** - Provide helpful feedback
- **Focus on what's best** - For the community and project

## How Can I Contribute?

### Reporting Bugs 

Before creating bug reports, please check existing issues to avoid duplicates.

**Great bug reports include:**
- Clear, descriptive title
- Exact steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details (OS, Python version, etc.)

**Template:**
```markdown
**Description:**
Brief description of the bug

**Steps to Reproduce:**
1. Go to '...'
2. Run command '...'
3. See error

**Expected Behavior:**
What you expected to happen

**Actual Behavior:**
What actually happened

**Environment:**
- OS: [e.g., macOS 14.0]
- Python: [e.g., 3.11.0]
- Dependencies: [list relevant packages]

**Additional Context:**
Any other relevant information
```

### Suggesting Enhancements 

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear, descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

**Types of enhancements we're interested in:**
- New frequency bands to harvest
- Improved rectifier designs
- Better efficiency algorithms
- Real-world testing data
- Alternative antenna designs
- Integration with IoT platforms

### Documentation Improvements 

Documentation is crucial! We welcome:

- Fixing typos or grammar
- Adding examples and tutorials
- Improving clarity of explanations
- Translating documentation
- Adding diagrams and visualizations

### Code Contributions 

We love pull requests! Areas where we need help:

**Simulation & Modeling:**
- Improve power calculation accuracy
- Add new scenario simulations
- Visualization improvements
- Performance optimization

**Hardware Design:**
- Antenna design files (KiCad, Altium)
- PCB layouts
- 3D printable enclosures
- Bill of Materials optimization

**Testing:**
- Real-world measurement data
- Validation of theoretical models
- Different environment testing
- Long-term performance data

**Applications:**
- IoT sensor implementations
- Integration with existing platforms
- Example projects
- Use case demonstrations

## Getting Started

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Clone the repository
git clone https://github.com/bhim-shrestha/resocha.git
cd resocha

# Install dependencies
pip install -r requirements.txt # (when available)
```

### Running the Simulator

```bash
python resocharge_simulator.py
```

### Project Structure

```
resocha/
 01-06_*.md # Core research documentation
 EXECUTIVE_SUMMARY.md # Project overview
 MARKET_ANALYSIS.md # Competitor research
 QUICK_REFERENCE.md # Technical reference
 resocharge_simulator.py # Power calculator
 hardware/ # (Future) Hardware designs
 examples/ # (Future) Example projects
 tests/ # (Future) Test suite
```

## Development Workflow

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your own copy.

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `test/` - Testing additions
- `refactor/` - Code refactoring

### 3. Make Your Changes

- Write clear, concise commit messages
- Follow the style guidelines (below)
- Add tests if applicable
- Update documentation if needed

### 4. Test Your Changes

```bash
# Run the simulator to ensure it still works
python resocharge_simulator.py

# If you add tests (future):
# pytest tests/
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add multi-frequency optimization

- Implement adaptive frequency selection
- Add power density weighting
- Update simulator with new algorithm

Closes #123"
```

**Commit message format:**
```
<type>: <short description>

<detailed description>

<footer>
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Formatting, no code change
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then go to GitHub and create a Pull Request.

**Good PR descriptions include:**
- What changes were made and why
- Link to related issues
- Screenshots (if UI changes)
- Testing performed
- Any breaking changes

## Style Guidelines

### Python Code Style

We follow [PEP 8](https://pep8.org/) with some exceptions:

```python
# Good
def calculate_harvested_power(power_density: float, area: float, efficiency: float) -> float:
 """
 Calculate harvested power from ambient RF.
 Args:
 power_density: Available power density in μW/m²
 area: Effective antenna area in m²
 efficiency: System efficiency (0.0 to 1.0)
 Returns:
 Harvested power in μW
 """
 return power_density * area * efficiency

# Use type hints
# Docstrings for all functions
# Clear variable names
# Comments for complex logic
```

**Tools we use:**
- `black` for formatting (when available)
- `pylint` for linting
- `mypy` for type checking

### Documentation Style

**IMPORTANT: All documentation must follow professional/academic standards.**

See **[WRITING_STYLE_GUIDE.md](WRITING_STYLE_GUIDE.md)** for complete guidelines.

**Quick summary:**
- NO emojis or emoticons (strictly enforced)
- Formal, professional language only
- All technical claims must be cited
- Define acronyms on first use
- Include units in all measurements

**Markdown guidelines:**
- Use clear headers (# ## ###)
- Include code examples
- Add visual elements (tables, diagrams)
- Keep line length reasonable (~80-100 chars)
- **NO EMOJIS** - Maintain professional/academic tone

**Technical writing standards:**
- Use formal, professional language
- Avoid casual expressions and colloquialisms
- Define acronyms on first use (e.g., "Radio Frequency (RF)")
- Include units in all measurements (μW, MHz, m², etc.)
- Show calculations step-by-step with clear notation
- **Always cite sources** - Add references to REFERENCES.md
- Use third person or passive voice for formal documentation
- Prefer "we recommend" over "we think" or "we feel"
- Use "cannot" instead of "can't", "does not" instead of "doesn't"

**Academic writing principles:**
- Present findings objectively without hyperbole
- Use hedging language appropriately ("may", "suggests", "indicates")
- Support all claims with data or citations
- Maintain consistent terminology throughout
- Use proper scientific notation and symbols

### Hardware Design

**File formats:**
- **Schematics:** KiCad (preferred), Altium, Eagle
- **PCB:** Gerber files + source files
- **3D Models:** STL, STEP
- **Documentation:** PDF exports + source

**Naming:**
```
resocharge_v1.0_schematic.kicad_sch
resocharge_v1.0_pcb.kicad_pcb
resocharge_v1.0_bom.csv
```

## Testing Guidelines

### Simulation Testing

If you modify the simulator:

```python
# Example test (future)
def test_power_calculation():
 """Test basic power calculation"""
 power_density = 100 # μW/m²
 area = 0.1 # m²
 efficiency = 0.3
 expected = 3.0 # μW
 actual = calculate_power(power_density, area, efficiency)
 assert abs(actual - expected) < 0.1
```

### Hardware Testing

If you build hardware:

**Required measurements:**
- Power density at antenna (before rectifier)
- DC output power (after rectifier)
- Efficiency calculation
- Temperature monitoring
- Time-series data (1 hour minimum)

**Please document:**
- Location and environment
- Equipment used (spectrum analyzer, etc.)
- Date and time of testing
- Weather/RF conditions

## Areas Seeking Contributions

### High Priority 

- [ ] Real-world testing data from different locations
- [ ] Improved rectifier circuit designs
- [ ] Antenna optimization for specific bands
- [ ] PCB design for prototype
- [ ] Bill of Materials with sourcing

### Medium Priority 

- [ ] Additional simulation scenarios
- [ ] Data visualization improvements
- [ ] Documentation translations
- [ ] Example IoT sensor implementations
- [ ] Cost optimization analysis

### Future Features 

- [ ] Machine learning power prediction
- [ ] Mobile app for power monitoring
- [ ] Cloud database of RF measurements
- [ ] Integration with Home Assistant
- [ ] Automatic frequency selection

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in academic papers (if applicable)
- Given credit in any commercialization (if significant contribution)

## Questions?

- **Discussions:** Use GitHub Discussions for questions
- **Issues:** Use GitHub Issues for bugs/features
- **Email:** [Your contact - optional]
- **Twitter:** [@your_handle - optional]

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Thank You! 

Your contributions make this project better for everyone. Whether you're fixing a typo or adding a major feature, every contribution is valued!

**Let's harvest some energy together!** 

---

**Special Thanks To:**
- Nikola Tesla - For the inspiration
- Open source community - For the tools and knowledge
- All contributors - For making this possible

*"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."* — Nikola Tesla
