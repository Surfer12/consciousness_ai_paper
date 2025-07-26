#!/bin/bash
# Temporal Forensics Automation Script
# Based on the comprehensive forensics plan provided
# Usage: ./forensic_automation.sh [file_path]

echo "=========================================="
echo "TEMPORAL FORENSICS AUTOMATION SCRIPT"
echo "Date: $(date)"
echo "=========================================="

# Check if file path provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_path>"
    echo "Example: $0 ../Documents/Papers/bour-eval-v1.txt.rtf"
    exit 1
fi

FILE_PATH="$1"
EVIDENCE_DIR="forensic_evidence_$(date +%Y%m%d_%H%M%S)"

# Create evidence directory
mkdir -p "$EVIDENCE_DIR"

echo "Analyzing file: $FILE_PATH"
echo "Evidence directory: $EVIDENCE_DIR"
echo ""

# 1. CRYPTOGRAPHIC HASHES
echo "===== CRYPTOGRAPHIC INTEGRITY ====="
echo "Generating SHA-256 hash..."
shasum -a 256 "$FILE_PATH" | tee "$EVIDENCE_DIR/sha256_hash.txt"
echo "Generating SHA-512 hash..."
shasum -a 512 "$FILE_PATH" | tee "$EVIDENCE_DIR/sha512_hash.txt"
echo ""

# 2. FILESYSTEM METADATA
echo "===== FILESYSTEM METADATA ====="
echo "File: $FILE_PATH"
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    stat -f "Birth: %SB | Modified: %Sm | Access: %Sa | Size: %z bytes" "$FILE_PATH" | tee "$EVIDENCE_DIR/filesystem_metadata.txt"
else
    # Linux
    stat -c "Modified: %y | Access: %x | Size: %s bytes" "$FILE_PATH" | tee "$EVIDENCE_DIR/filesystem_metadata.txt"
fi
echo ""

# 3. FILE TYPE ANALYSIS
echo "===== FILE TYPE ANALYSIS ====="
file "$FILE_PATH" | tee "$EVIDENCE_DIR/file_type.txt"
echo ""

# 4. METADATA EXTRACTION (if exiftool available)
echo "===== EMBEDDED METADATA ====="
if command -v exiftool &> /dev/null; then
    echo "Using exiftool for metadata extraction..."
    exiftool -time:all -a -G0:1 "$FILE_PATH" | grep -i date | tee "$EVIDENCE_DIR/exif_metadata.txt"
else
    echo "exiftool not available - using alternative methods..."
    # For RTF files, check header
    if [[ "$FILE_PATH" == *.rtf ]]; then
        echo "RTF Header Analysis:"
        head -20 "$FILE_PATH" | grep -i "creat\|modif\|date\|time" | tee "$EVIDENCE_DIR/rtf_header_analysis.txt"
    fi
fi
echo ""

# 5. BACKUP ARTIFACT SEARCH
echo "===== BACKUP ARTIFACT SEARCH ====="
BASENAME=$(basename "$FILE_PATH" .rtf)
DIRNAME=$(dirname "$FILE_PATH")
echo "Searching for backup artifacts related to: $BASENAME"

# Look for common backup patterns
find "$DIRNAME" -name "*$BASENAME*" -type f 2>/dev/null | grep -E "\.(bak|tmp|~|asd|wbk)$" | tee "$EVIDENCE_DIR/backup_artifacts.txt"
echo ""

# 6. VERSION CONTROL CHECK
echo "===== VERSION CONTROL ANALYSIS ====="
if [ -d ".git" ]; then
    echo "Git repository detected. Checking for file in version history..."
    git log --follow --name-only -- "$FILE_PATH" 2>/dev/null | tee "$EVIDENCE_DIR/git_history.txt"
    if [ ! -s "$EVIDENCE_DIR/git_history.txt" ]; then
        echo "File not found in git history" | tee "$EVIDENCE_DIR/git_history.txt"
    fi
else
    echo "No git repository found in current directory" | tee "$EVIDENCE_DIR/git_history.txt"
fi
echo ""

# 7. DUPLICATE DETECTION
echo "===== DUPLICATE FILE DETECTION ====="
FILE_HASH=$(shasum -a 256 "$FILE_PATH" | cut -d' ' -f1)
echo "Searching for files with identical hash: $FILE_HASH"
find ~ -type f -exec shasum -a 256 {} \; 2>/dev/null | grep "^$FILE_HASH" | tee "$EVIDENCE_DIR/duplicate_files.txt"
echo ""

# 8. EVIDENCE SUMMARY
echo "===== EVIDENCE SUMMARY ====="
echo "Analysis completed: $(date)" | tee "$EVIDENCE_DIR/analysis_summary.txt"
echo "File analyzed: $FILE_PATH" | tee -a "$EVIDENCE_DIR/analysis_summary.txt"
echo "Evidence preserved in: $EVIDENCE_DIR" | tee -a "$EVIDENCE_DIR/analysis_summary.txt"
echo ""
echo "All evidence files created:"
ls -la "$EVIDENCE_DIR/"

echo ""
echo "=========================================="
echo "FORENSIC ANALYSIS COMPLETE"
echo "Evidence directory: $EVIDENCE_DIR"
echo "==========================================" 