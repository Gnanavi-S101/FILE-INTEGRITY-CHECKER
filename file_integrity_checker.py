"""
File Integrity Checker
Author: Sky
Description: Monitors file changes by calculating and comparing SHA-256 hash values.
"""

import hashlib
import os
import json
from datetime import datetime

BASELINE_FILE = "baseline.json"


def calculate_hash(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        return None
    except PermissionError:
        print(f"[ERROR] Permission denied: {filepath}")
        return None


def save_baseline(filepath, hash_value):
    """Save the baseline hash of a file to a JSON file."""
    baseline = {}
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            baseline = json.load(f)

    baseline[filepath] = {
        "hash": hash_value,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print(f"[INFO] Baseline saved for: {filepath}")
    print(f"[INFO] SHA-256: {hash_value}")


def load_baseline(filepath):
    """Load the stored baseline hash for a file."""
    if not os.path.exists(BASELINE_FILE):
        print("[WARNING] No baseline file found. Please create a baseline first.")
        return None

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    if filepath not in baseline:
        print(f"[WARNING] No baseline found for: {filepath}")
        return None

    return baseline[filepath]["hash"]


def create_baseline(filepath):
    """Create a baseline hash for the given file."""
    print(f"\n[*] Creating baseline for: {filepath}")
    hash_value = calculate_hash(filepath)
    if hash_value:
        save_baseline(filepath, hash_value)


def check_integrity(filepath):
    """Compare current file hash against the stored baseline."""
    print(f"\n[*] Checking integrity of: {filepath}")

    current_hash = calculate_hash(filepath)
    if not current_hash:
        return

    baseline_hash = load_baseline(filepath)
    if not baseline_hash:
        return

    print(f"[INFO] Baseline Hash : {baseline_hash}")
    print(f"[INFO] Current Hash  : {current_hash}")

    if current_hash == baseline_hash:
        print("[OK] File integrity VERIFIED. No changes detected.")
    else:
        print("[ALERT] File integrity COMPROMISED! The file has been modified.")


def main():
    print("=" * 50)
    print("       FILE INTEGRITY CHECKER - SHA-256")
    print("=" * 50)

    print("\nOptions:")
    print("  1. Create baseline for a file")
    print("  2. Check file integrity")
    print("  3. Exit")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice == "1":
        filepath = input("Enter file path: ").strip()
        create_baseline(filepath)

    elif choice == "2":
        filepath = input("Enter file path: ").strip()
        check_integrity(filepath)

    elif choice == "3":
        print("Exiting. Goodbye!")

    else:
        print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()