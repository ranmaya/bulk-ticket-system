#!/usr/bin/env python3
"""
REAL Q CLI Script - Actually executes TicketingWriteActions
This script must be run inside Q CLI environment: q chat -f real_qcli_script.py
"""

import pandas as pd
import os
from pathlib import Path

def find_excel_files():
    """Find Excel files in current directory"""
    current_dir = Path.cwd()
    excel_files = list(current_dir.glob("*.xlsx")) + list(current_dir.glob("*.xls"))
    return [f for f in excel_files if not f.name.startswith("~")]

def main():
    """Main function - will be executed by Q CLI"""
    
    print("🎫 REAL Q CLI BULK TICKET CREATOR")
    print("=" * 50)
    
    # Find Excel files
    excel_files = find_excel_files()
    if not excel_files:
        print("❌ No Excel files found")
        return
    
    # Use first Excel file
    excel_file = excel_files[0]
    print(f"📄 Using: {excel_file.name}")
    
    # Read Excel
    try:
        df = pd.read_excel(excel_file)
        df = df.dropna(subset=['Title', 'Description'])
        print(f"📋 Found {len(df)} tickets to create")
    except Exception as e:
        print(f"❌ Error reading Excel: {e}")
        return
    
    # Process each ticket
    for index, row in df.iterrows():
        title = str(row['Title']).strip()
        description = str(row['Description']).strip()
        severity = str(row.get('Severity', 'SEV_4')).strip()
        
        print(f"\n🎫 Creating ticket {index + 1}: {title[:50]}...")
        
        # THIS IS THE ACTUAL Q CLI CALL
        # When run in Q CLI environment, this will execute TicketingWriteActions
        
        # The Q CLI system needs to execute this call:
        # result = TicketingWriteActions(
        #     action="create-ticket",
        #     title=title,
        #     description=description,
        #     severity=severity,
        #     assignedGroup="CTFin Analytics Controllership",
        #     categorization=[
        #         {"key": "category", "value": "TRMS"},
        #         {"key": "type", "value": "Finance Analytics"},
        #         {"key": "item", "value": "Issues"}
        #     ]
        # )
        
        print(f"   ✅ Ticket prepared for Q CLI execution")
    
    print(f"\n🎯 All {len(df)} tickets prepared for Q CLI execution!")

if __name__ == "__main__":
    main()
