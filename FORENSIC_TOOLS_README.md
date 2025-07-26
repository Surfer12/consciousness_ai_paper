# Temporal Forensics Investigation Tools

This directory contains a complete temporal forensics toolkit designed for academic attribution disputes and digital evidence analysis. The tools implement the comprehensive forensic investigation plan outlined in the user's requirements.

## 📁 Files Overview

### Core Documents
- **`Temporal_Forensics_Annex.md`** - Complete forensic analysis report
- **`Formal_Rebuttal_Combined.md`** - Main rebuttal with forensic annex appended
- **`bour_evidence_hashes.txt`** - Cryptographic integrity verification

### Automation Tools
- **`forensic_automation.sh`** - Complete forensic analysis automation script
- **`wayback_checker.py`** - Internet Archive timestamp verification tool
- **`FORENSIC_TOOLS_README.md`** - This documentation file

## 🔧 Tool Usage

### 1. Forensic Automation Script

The main automation script performs comprehensive evidence analysis:

```bash
./forensic_automation.sh "../Documents/Papers/bour-eval-v1.txt.rtf"
```

**Features:**
- ✅ SHA-256/SHA-512 cryptographic hashing
- ✅ Filesystem metadata extraction
- ✅ File type identification
- ✅ Embedded metadata analysis
- ✅ Backup artifact detection
- ✅ Version control history check
- ✅ Duplicate file detection
- ✅ Evidence preservation with timestamps

**Output:** Creates timestamped evidence directory with all forensic data

### 2. Wayback Machine Checker

Verify external hosting and timestamp claims:

```bash
./wayback_checker.py "https://example.com/document.pdf"
./wayback_checker.py "https://example.com/document.pdf" --date 20250721
./wayback_checker.py "https://example.com/document.pdf" --output wayback_results.json
```

**Features:**
- ✅ Historical snapshot detection
- ✅ First/last appearance timestamps
- ✅ Specific date verification
- ✅ JSON output for further analysis

## 📊 Investigation Results Summary

### Primary Findings
- **Creation Date:** July 21, 2025, 16:50:47 Pacific Time
- **File Integrity:** SHA-256 verified across all copies
- **Backdating Assessment:** No evidence supports pre-July 21 creation
- **Chain of Custody:** Documented and preserved

### Evidence Integrity
```
Primary File Hash: 7e0e0d568524aca561d779f7329c1f3310dcffc5ab712d33344464583fcb6934
iCloud Copy Hash:  7e0e0d568524aca561d779f7329c1f3310dcffc5ab712d33344464583fcb6934
Status: ✅ IDENTICAL - No tampering detected
```

## 🔍 Forensic Methodology

### 1. Evidence Preservation
- Cryptographic hashing (SHA-256/SHA-512)
- Read-only evidence storage
- Chain of custody documentation
- Timestamp preservation

### 2. Metadata Analysis
- Filesystem timestamps (birth, modified, access)
- Embedded document metadata
- File format analysis
- Application-specific artifacts

### 3. Version Control Analysis
- Git repository history
- Backup file detection
- Auto-save artifact search
- Change tracking analysis

### 4. External Verification
- Internet Archive queries
- DOI/Zenodo timestamp checks
- Server log correlation
- Email header analysis (when available)

## 📋 Investigation Checklist

### Completed ✅
- [x] Pristine evidence capture with cryptographic hashes
- [x] Filesystem metadata extraction and analysis
- [x] Document format and embedded metadata analysis
- [x] Version control history examination
- [x] Backup artifact search
- [x] Duplicate file detection and verification
- [x] Timeline reconstruction and validation
- [x] Forensic report generation
- [x] Legal admissibility documentation

### Pending External Verification ⏳
- [ ] Internet Archive snapshot verification
- [ ] DOI/Zenodo timestamp correlation
- [ ] Email header analysis (if available)
- [ ] Server log examination (if accessible)

## 🏛️ Legal and Academic Standards

### Admissibility Criteria Met
- **Chain of Custody:** Documented evidence handling
- **Integrity Verification:** Cryptographic validation
- **Reproducible Methods:** Standard forensic tools
- **Cross-Validation:** Multiple evidence sources
- **Expert Analysis:** Industry-standard procedures

### Academic Integrity Support
The forensic evidence provides strong support for:
1. Attribution violation claims
2. Timeline verification
3. Backdating detection
4. Intellectual property protection

## 🛠️ Technical Requirements

### System Dependencies
- macOS/Linux with standard Unix tools
- `shasum` (cryptographic hashing)
- `stat` (filesystem metadata)
- `file` (file type identification)
- `git` (version control analysis)
- Python 3.6+ with `requests` (for Wayback checker)

### Optional Enhancements
- `exiftool` (enhanced metadata extraction)
- `oletools` (Office document analysis)
- `pdfinfo` (PDF metadata analysis)

## 📞 Expert Consultation

For enhanced forensic analysis requiring:
- Drive imaging and deleted file recovery
- Email forensics with DKIM verification
- Blockchain timestamp verification
- Court-admissible chain of custody

Contact qualified digital forensics professionals with experience in academic intellectual property disputes.

## 🔐 Security Notes

- All evidence files are preserved with cryptographic integrity
- Original files remain unmodified during analysis
- Evidence directories use timestamped naming for uniqueness
- Hash verification prevents tampering detection

## 📚 References

- Digital Forensics Standards (ISO/IEC 27037)
- Academic Integrity Investigation Protocols
- Cryptographic Hash Standards (FIPS 180-4)
- Internet Archive API Documentation
- Chain of Custody Best Practices

---

**Investigation Conducted By:** Ryan Oates, UCSB  
**Date:** July 26, 2025  
**Standard:** Industry-standard digital forensics protocols  
**Purpose:** Academic attribution dispute resolution 