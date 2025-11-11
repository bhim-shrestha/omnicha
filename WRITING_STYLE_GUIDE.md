# Writing Style Guide

## Purpose

This document establishes professional and academic writing standards for all ResoCharge documentation. These guidelines ensure consistency, credibility, and accessibility for researchers, engineers, and industry professionals.

---

## Core Principles

### 1. Professional Tone

**REQUIRED:**
- Formal, objective language
- Third-person or passive voice for technical documentation
- Evidence-based claims with proper citations
- Neutral presentation of findings

**AVOID:**
- Casual language and colloquialisms
- Emojis and emoticons (strictly prohibited)
- Exclamation marks (except in warnings)
- First-person narrative ("I think", "I feel")
- Marketing language or hyperbole

### 2. Academic Rigor

**All documentation must:**
- Cite sources for technical claims
- Define acronyms on first use
- Include units in all measurements
- Show derivations for calculations
- Acknowledge limitations and uncertainties

---

## Language Standards

### Formal vs. Informal

| Avoid (Informal) | Use (Formal) |
|------------------|--------------|
| can't, won't, doesn't | cannot, will not, does not |
| tons of, lots of | numerous, substantial, significant |
| We think / We feel | We recommend / Analysis suggests |
| pretty good | satisfactory, adequate |
| huge, massive | substantial, significant |
| Let's build it! | Implementation recommended |
| Check this out | Consider the following |
| Cool, awesome | Notable, significant, effective |

### Technical Writing

**Acronyms and abbreviations:**
```
FIRST USE: Radio Frequency (RF)
SUBSEQUENT: RF

FIRST USE: Internet of Things (IoT)
SUBSEQUENT: IoT
```

**Units and measurements:**
```
CORRECT: 5 W, 100 μW/m², 2.4 GHz
INCORRECT: 5W (missing space), 100 microwatts (use μW)

CORRECT: The power density was measured at 127 μW/m².
INCORRECT: The power density was 127 (missing units)
```

**Numbers and values:**
```
CORRECT: Values ranged from 10 μW to 100 μW.
INCORRECT: Values ranged from 10-100 μW. (ambiguous)

CORRECT: The efficiency is approximately 45%.
INCORRECT: The efficiency is ~45%. (use words)
```

---

## Document Structure

### Headers and Sections

```markdown
# Main Title (H1 - once per document)

## Major Section (H2)

### Subsection (H3)

#### Minor Subsection (H4)
```

**Header guidelines:**
- Use title case for H1
- Use sentence case for H2-H4
- Be specific and descriptive
- Avoid questions in headers (use statements)

### Paragraphs

- Topic sentence states main idea
- Supporting sentences provide evidence
- Concluding sentence summarizes or transitions
- Maximum 5-7 sentences per paragraph
- Blank line between paragraphs

---

## Citations and References

### In-Text Citations

**Numbered format (preferred for ResoCharge):**
```markdown
RF energy harvesting has demonstrated 40-84% efficiency [1, 2].

Multiple studies have measured urban power densities [3, 4, 5].
```

**Inline format (alternative):**
```markdown
Valenta and Durgin (2014) surveyed rectenna efficiency across multiple systems.

According to Piñuela et al. (2013), urban environments provide 50-150 μW/m².
```

### Adding References

**All new technical claims require citations:**

1. Add source to REFERENCES.md:
```markdown
## Academic Papers & Research

42. **Author, A. B., & Author, C. D. (Year).** "Title of Paper." 
    *Journal Name*, Volume(Issue), Pages.
    - DOI: 10.xxxx/xxxxx
    - Note: Brief description of relevance
```

2. Reference in documentation:
```markdown
The Dickson charge pump architecture [6] provides efficient voltage multiplication.
```

### What Requires Citation

**ALWAYS cite:**
- Technical specifications and performance data
- Research findings and experimental results
- Market data and industry statistics
- Historical information
- Theoretical equations and formulas (first use)
- Component specifications (manufacturer datasheets)

**NO citation needed:**
- Well-established physical laws (after initial definition)
- Mathematical derivations shown in the document
- Original calculations performed for this project
- General knowledge in the field

---

## Technical Elements

### Equations and Formulas

**Format:**
```markdown
The Friis transmission equation relates received power to transmitted power:

P_r = P_t × G_t × G_r × (λ / 4πd)²

Where:
- P_r = received power (W)
- P_t = transmitted power (W)
- G_t = transmitter antenna gain (dimensionless)
- G_r = receiver antenna gain (dimensionless)
- λ = wavelength (m)
- d = distance between antennas (m)
```

**Guidelines:**
- Define all variables immediately after the equation
- Include units for each variable
- Use consistent notation throughout document
- Show derivation steps for complex calculations

### Tables

**Professional table format:**

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| Frequency | 2.45 | GHz | [1] |
| Power density | 127 | μW/m² | [3] |
| Efficiency | 45 | % | Measured |

**Table guidelines:**
- Descriptive caption above table
- All columns labeled with units
- Consistent decimal places (align on decimal)
- Source cited in caption or column

### Code Examples

**Python:**
```python
def calculate_power(density: float, area: float, efficiency: float) -> float:
    """
    Calculate harvested power from ambient RF energy.
    
    Parameters:
        density: Power density in μW/m²
        area: Effective antenna area in m²
        efficiency: System efficiency (0.0 to 1.0)
    
    Returns:
        Harvested power in μW
    """
    return density * area * efficiency
```

**Guidelines:**
- Include type hints
- Write docstrings for all functions
- Use descriptive variable names
- Comment complex logic
- Follow PEP 8 conventions

---

## Specific Documentation Types

### Research Documents (01-06 series)

**Structure:**
1. Introduction with clear objective
2. Background and related work (with citations)
3. Methodology or approach
4. Results and analysis
5. Discussion of implications
6. Conclusion and recommendations

**Tone:** Objective, analytical, evidence-based

### Technical Specifications

**Include:**
- Precise numerical values with units
- Operating ranges and tolerances
- Performance characteristics
- Limitations and constraints
- Test conditions

**Format:**
```markdown
## Specifications

### Electrical Characteristics
- Operating frequency: 2.4 GHz ± 50 MHz
- Input power range: 1-100 μW
- Conversion efficiency: 35-45% (typical)
- Output voltage: 1.8 V ± 0.1 V
```

### Market Analysis

**Requirements:**
- Cite all market data sources
- Specify date of data collection
- Distinguish facts from projections
- Acknowledge competitor information sources
- Present neutral comparisons

---

## Common Mistakes to Avoid

### Language Errors

**INCORRECT:**
```markdown
This is really important for IoT devices!
We think RF harvesting is awesome.
The results are pretty good.
```

**CORRECT:**
```markdown
This consideration is critical for IoT device applications.
Analysis indicates RF harvesting provides significant benefits.
The results demonstrate satisfactory performance characteristics.
```

### Technical Errors

**INCORRECT:**
```markdown
Power = 100 (missing units)
Efficiency: ~40% (use words, not symbols)
The device works well (vague, not quantitative)
```

**CORRECT:**
```markdown
Power = 100 μW
Efficiency: approximately 40%
The device achieves 85% uptime under standard operating conditions.
```

### Citation Errors

**INCORRECT:**
```markdown
Studies show this works well.
According to research, efficiency is high.
It's well known that Tesla invented wireless power.
```

**CORRECT:**
```markdown
Multiple studies demonstrate 40-60% efficiency [1, 2, 3].
Valenta and Durgin (2014) measured 45% average efficiency across ten systems [2].
Tesla developed resonant inductive coupling in 1891, later refined at Wardenclyffe [8, 9].
```

---

## Review Checklist

Before submitting documentation, verify:

### Language
- [ ] No emojis or emoticons present
- [ ] Formal language throughout (no contractions)
- [ ] Third-person or passive voice used
- [ ] No exclamation marks (except warnings)
- [ ] No casual expressions or colloquialisms

### Technical Content
- [ ] All acronyms defined on first use
- [ ] Units included in all measurements
- [ ] Equations clearly formatted with variable definitions
- [ ] Tables include headers with units
- [ ] Calculations shown step-by-step

### Citations
- [ ] Technical claims supported by references
- [ ] Sources added to REFERENCES.md
- [ ] In-text citations properly formatted
- [ ] Data sources specified with dates
- [ ] Manufacturer specifications cited

### Structure
- [ ] Clear hierarchical organization
- [ ] Descriptive section headers
- [ ] Logical flow of information
- [ ] Consistent formatting throughout
- [ ] Professional appearance

---

## Examples

### Example 1: Before and After

**BEFORE (Casual, unprofessional):**
```markdown
# Cool RF Harvesting Stuff!

WiFi is everywhere nowadays! We can totally harvest it to power things. 
It's super cool how Tesla did this like 100 years ago. We should build 
some awesome devices that use this tech. The results are pretty good!

Here's what you can do:
- Build IoT sensors 
- They work great!  
- Save the planet 
```

**AFTER (Professional, academic):**
```markdown
# Radio Frequency Energy Harvesting for Autonomous Systems

Ambient Radio Frequency (RF) energy from commercial wireless infrastructure 
presents opportunities for powering ultra-low-power devices. This approach, 
conceptually demonstrated by Tesla in the early 20th century [8, 9], has been 
validated through modern rectenna technology [1, 2].

## Applications

Analysis indicates the following applications achieve technical feasibility:

### Internet of Things Sensors
- Power requirement: 10-100 μW
- Feasibility: High (ambient RF provides 50-150 μW/m² in urban environments [3])
- Implementation status: Commercially proven [16, 17]
```

### Example 2: Technical Description

**BEFORE:**
```markdown
The circuit works by catching RF waves with an antenna and then turning 
them into DC power. It's pretty efficient - like 40% or so. You need 
a good antenna and a fast diode to make it work right.
```

**AFTER:**
```markdown
## System Architecture

The rectenna system operates through four primary stages:

1. **RF Reception**: A tuned antenna (2.4 GHz resonance) captures 
   electromagnetic energy with 80% efficiency [1]
   
2. **Impedance Matching**: A Pi-network matches antenna impedance 
   (50 Ω) to rectifier input, achieving 90% power transfer [21]
   
3. **Rectification**: A Schottky diode bridge (HSMS-285C) converts 
   RF to DC with 40-50% efficiency at 10-100 μW input [22]
   
4. **Output Filtering**: A low-pass filter (f_c = 100 Hz) provides 
   95% ripple attenuation

Total system efficiency: 25-35% under typical operating conditions 
(P_in = 50 μW, f = 2.4 GHz).
```

---

## Enforcement

### For Contributors

All pull requests will be reviewed for compliance with this style guide. 
Non-compliant submissions will be requested to revise before merge.

### For Maintainers

Maintainers should:
- Reference this guide when requesting changes
- Provide specific examples of violations
- Be supportive and educational in feedback
- Recognize that English proficiency varies

### For AI Assistants

When generating content for this project:
- Follow all guidelines in this document
- Never include emojis or casual language
- Always provide citations for technical claims
- Use formal academic tone throughout
- Verify units and technical accuracy

---

## Questions?

If you are unsure about style guidance:
1. Check examples in existing documentation
2. Consult REFERENCES.md for citation format
3. Open a GitHub Discussion for clarification
4. Reference academic papers in your field

---

## Document History

- **Version 1.0** (2025-11-10): Initial style guide created
- Professional standards established
- No-emoji policy implemented
- Academic citation requirements defined

---

**Note:** This guide evolves based on community feedback. Suggestions for 
improvements should be submitted as GitHub issues with the label "documentation".
