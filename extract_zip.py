#!/usr/bin/env python3
"""
Script to extract roulette_v4_clean_for_github.zip and remove the ZIP file.
Run this script from the repository root directory.
"""

import zipfile
import os
import sys

def extract_and_cleanup():
    zip_file = 'roulette_v4_clean_for_github.zip'
    
    if not os.path.exists(zip_file):
        print(f"Error: {zip_file} not found in current directory")
        return False
    
    try:
        # Extract the ZIP file
        print(f"Extracting {zip_file}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall()
        print("✓ Extraction complete")
        
        # Remove the ZIP file
        print(f"Removing {zip_file}...")
        os.remove(zip_file)
        print("✓ ZIP file removed")
        
        print("\nSuccess! The roulette_v4 directory has been extracted.")
        print("Next steps:")
        print("  1. git add roulette_v4/")
        print("  2. git commit -m 'Extract roulette_v4_clean_for_github.zip'")
        print("  3. git push origin main")
        
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    success = extract_and_cleanup()
    sys.exit(0 if success else 1)
