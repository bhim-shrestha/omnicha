# Project Rename: OmniCharge to ResoCharge

**Date:** November 10, 2025  
**Version:** 1.0.0

---

## Summary

This project has been renamed from **OmniCharge** to **ResoCharge** to avoid trademark conflicts with an existing commercial entity (Omnicharge Inc., omnicharge.co).

---

## Reason for Change

### Trademark Conflict Identified

**Existing Company:** Omnicharge Inc.
- **Website:** omnicharge.co
- **Products:** Portable power banks, power stations, enterprise charging solutions
- **Location:** California, USA
- **Industry:** Power/charging solutions (directly related to our research area)
- **Status:** Active commercial entity with established brand

**Risk Assessment:**
- High potential for trademark infringement
- Confusion in the power/energy space
- Legal complications for future commercialization
- SEO/branding conflicts

### Decision

To maintain academic integrity and avoid legal issues, the project was renamed to **ResoCharge** before gaining significant public visibility.

---

## New Name: ResoCharge

### Name Breakdown

**Reso** = Resonance
- References Tesla's resonant inductive coupling
- Core principle of RF energy harvesting
- Implies frequency matching and harmonic capture

**Charge** = Energy/Power
- Clear connection to energy harvesting
- Maintains the original "charge" concept
- Professional and technical

### Technical Accuracy

The name **ResoCharge** accurately reflects the technology:
- Resonant frequency matching is fundamental to rectenna operation
- Multi-band harvesting relies on resonant antenna design
- Tesla's resonant coupling principles are core to this research
- Impedance matching (resonance-based) is critical for efficiency

### Advantages

**Legal:**
- No trademark conflicts identified
- Available for use in research and potential commercialization
- Clean slate for branding

**Technical:**
- Accurately describes the resonant RF harvesting approach
- Honors Tesla's resonant coupling work
- Professional and academic tone

**Branding:**
- Unique and memorable
- Easy to spell and pronounce
- Good SEO potential (distinctive name)
- Works well as hashtag: #ResoCharge

---

## Changes Made

### Documentation Files Updated (14 files)

1. README.md
2. 04_TESLA_WIRELESS_POWER_RESEARCH.md
3. 06_FEASIBILITY_ANALYSIS_AND_RECOMMENDATIONS.md
4. EXECUTIVE_SUMMARY.md
5. INDEX.md
6. MARKET_ANALYSIS.md
7. CONTRIBUTING.md
8. SECURITY.md
9. REFERENCES.md
10. CITATION.cff
11. WRITING_STYLE_GUIDE.md
12. PROFESSIONALIZATION_CHECKLIST.md
13. .github/pull_request_template.md
14. resocharge_simulator.py (renamed from omnicharge_simulator.py)

### Total Instances Changed

- **42 instances** of "OmniCharge" replaced with "ResoCharge"
- **All case variations** updated (omnicharge, OMNICHARGE, etc.)
- **Repository references** updated (omnicha -> resocha)

### File Renames

```bash
# Python simulator renamed
omnicharge_simulator.py -> resocharge_simulator.py
```

### Still Requires (Manual Steps)

**GitHub Repository:**
1. Repository name: `omnicha` -> `resocha`
2. Update URL in badges and links
3. Update remote URL locally:
   ```bash
   git remote set-url origin https://github.com/bhim-shrestha/resocha.git
   ```

**Optional:**
- Domain registration (resocharge.com, resocharge.io)
- Social media handles (@resocharge)

---

## Migration Guide for Contributors

### For Existing Clones

If you have already cloned the repository:

```bash
# Update remote URL (after GitHub repo is renamed)
cd omnicha
git remote set-url origin https://github.com/bhim-shrestha/resocha.git

# Optional: Rename local directory
cd ..
mv omnicha resocha
cd resocha

# Pull latest changes
git pull origin main
```

### For New Clones

```bash
git clone https://github.com/bhim-shrestha/resocha.git
cd resocha
```

### Code References

Update any scripts or code that referenced:
- `omnicharge_simulator.py` -> `resocharge_simulator.py`
- "OmniCharge" class/variable names -> "ResoCharge"
- Repository URLs

---

## Citation Updates

### Old Citation

```bibtex
@misc{shrestha2025omnicharge,
  author = {Shrestha, Bhim},
  title = {OmniCharge: Ambient RF Energy Harvesting Research},
  year = {2025},
  url = {https://github.com/bhim-shrestha/omnicha}
}
```

### New Citation

```bibtex
@misc{shrestha2025resocharge,
  author = {Shrestha, Bhim},
  title = {ResoCharge: Ambient RF Energy Harvesting Research and Feasibility Analysis},
  year = {2025},
  url = {https://github.com/bhim-shrestha/resocha}
}
```

**See CITATION.cff for complete citation information.**

---

## Communication Plan

### Announcement (if needed)

For any existing followers or contributors:

**Subject:** Project Renamed: OmniCharge → ResoCharge

**Message:**
> We have renamed the RF energy harvesting research project from "OmniCharge" 
> to "ResoCharge" to avoid trademark conflicts with an existing commercial 
> entity. The new name better reflects our focus on resonant frequency matching 
> in ambient RF energy harvesting. All documentation has been updated. Please 
> update your local repositories accordingly.

### Social Media

```
Renamed our RF energy harvesting research project to ResoCharge (from OmniCharge) 
to honor Tesla's resonant coupling principles while avoiding trademark conflicts. 
Same great research, clearer name! #ResoCharge #RFHarvesting #IoT
```

---

## Technical Continuity

### What Stayed the Same

- All research findings and data
- Technical approach and methodology
- Documentation structure and content
- Code functionality
- MIT License
- Project goals and scope
- Repository history and commit log

### What Changed

- Project name only
- File references in documentation
- Python simulator filename
- Repository name (pending)
- URLs and links (pending)

---

## Future Considerations

### Brand Protection

Consider:
- Trademark search for "ResoCharge" before commercialization
- Domain registration
- Logo design (if project grows)
- Social media presence

### Academic Publications

Use **ResoCharge** in:
- Research papers
- Conference presentations
- Grant applications
- Academic citations

### Commercial Path

If pursuing commercialization:
- File trademark application for "ResoCharge"
- Verify no conflicts in target markets
- Establish brand guidelines
- Protect intellectual property

---

## Questions?

For questions about the name change:
- Open a GitHub Discussion
- Reference this document: PROJECT_RENAME.md
- See updated documentation in README.md

---

## Acknowledgment

Thank you to the community for understanding this necessary change. ResoCharge 
maintains the spirit of the original project while establishing a unique identity 
in the RF energy harvesting research space.

---

**Document Version:** 1.0  
**Last Updated:** November 10, 2025  
**Author:** Bhim Shrestha
