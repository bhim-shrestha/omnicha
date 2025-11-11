# Security Policy

## Supported Versions

As this is a research and educational project, we continuously update the main branch with improvements and fixes.

| Version | Supported |
| ------- | ------------------ |
| main | :white_check_mark: |
| < 1.0 | :x: |

## Reporting a Vulnerability

We take the security of ResoCharge seriously. If you discover a security vulnerability, please follow these steps:

### For Code/Software Vulnerabilities:

1. **DO NOT** open a public GitHub issue
2. Email the maintainer directly (or use GitHub's private vulnerability reporting)
3. Include:
 - Description of the vulnerability
 - Steps to reproduce
 - Potential impact
 - Suggested fix (if available)

### For Hardware/Safety Concerns:

If you discover a potential safety issue with hardware designs:

1. Open a GitHub issue with the label "safety"
2. Clearly describe the concern
3. Provide technical details
4. Suggest mitigation steps

### Response Timeline:

- **Acknowledgment:** Within 48 hours
- **Initial Assessment:** Within 7 days
- **Fix/Mitigation:** As soon as possible (depends on severity)
- **Public Disclosure:** After fix is deployed or mitigation is available

## Security Considerations for Users

### Electrical Safety:

**When building hardware from this project:**

 **WARNING: Working with RF circuits and power systems can be dangerous**

- Always follow proper ESD (Electrostatic Discharge) procedures
- Use appropriate test equipment
- Never exceed component voltage/current ratings
- Use proper fusing and overcurrent protection
- Follow local electrical codes and regulations
- Be aware of RF exposure limits (FCC/ICNIRP guidelines)

### RF Exposure:

- This project harvests ambient RF energy (very low power)
- All designs should comply with FCC/CE regulations
- Do not create high-power RF transmitters without proper licensing
- Follow SAR (Specific Absorption Rate) guidelines

### Battery Safety:

- Use appropriate battery protection circuits
- Follow battery manufacturer guidelines
- Never short-circuit batteries
- Properly dispose of damaged batteries
- Monitor temperature during charging

### Chemical Safety:

- PCB fabrication involves chemicals
- Follow MSDS (Material Safety Data Sheets)
- Use proper protective equipment
- Work in ventilated areas

## Privacy & Data

This project:
- Does NOT collect personal data
- Does NOT transmit data externally
- Simulator runs entirely locally
- No telemetry or tracking

If you contribute testing data:
- Only share data you're comfortable making public
- Remove any personally identifiable information
- Be aware that GitHub is public

## Third-Party Dependencies

When available, we will:
- Maintain a list of dependencies
- Monitor for security advisories
- Update dependencies regularly
- Use tools like Dependabot

## Responsible Disclosure

We appreciate security researchers who:
- Follow responsible disclosure practices
- Give us reasonable time to fix issues
- Don't exploit vulnerabilities maliciously

We will:
- Acknowledge your contribution
- Credit you in release notes (if desired)
- Keep you informed of progress

## Legal Considerations

### Regulatory Compliance:

**United States:**
- FCC Part 15 regulations apply to RF devices
- Power limits: Unlicensed devices typically <1W EIRP
- Interference: Must not cause harmful interference

**European Union:**
- CE marking required for commercial products
- RED (Radio Equipment Directive) compliance
- RoHS compliance for hazardous substances

**Other Regions:**
- Check local regulations before building/deploying
- Some frequencies may be restricted
- Commercial use may require certification

### Intellectual Property:

- This project is MIT Licensed
- Patents may exist on specific techniques
- Do your own patent search before commercialization
- We make no warranty regarding patent infringement

## Contact

For security issues: Use GitHub's private vulnerability reporting or create a security advisory

For general questions: Use GitHub Discussions or Issues

---

**Remember: Safety first! If you're unsure about anything, ask for help.** 
