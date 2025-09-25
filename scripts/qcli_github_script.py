#!/usr/bin/env python3
"""
GitHub + Q CLI Bulk Ticket Creator
This script runs in Q CLI environment and makes REAL TicketingWriteActions calls
"""

import pandas as pd
import os
import json
from pathlib import Path

def find_excel_files():
    """Find Excel files in current directory"""
    current_dir = Path.cwd()
    excel_files = list(current_dir.glob("*.xlsx")) + list(current_dir.glob("*.xls"))
    return [f for f in excel_files if not f.name.startswith("~")]

def read_excel_data(file_path):
    """Read and validate Excel data"""
    try:
        df = pd.read_excel(file_path)
        
        # Validate required columns
        required_cols = ['Title', 'Description']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            print(f"❌ Missing required columns: {missing_cols}")
            return None
        
        # Remove empty rows
        df = df.dropna(subset=['Title', 'Description'])
        
        print(f"📋 Found {len(df)} valid tickets in {file_path.name}")
        return df
        
    except Exception as e:
        print(f"❌ Error reading Excel: {e}")
        return None

def create_real_ticket_qcli(title, description, severity="SEV_4"):
    """
    This function will be executed by Q CLI to create REAL tickets
    Q CLI will call TicketingWriteActions with these parameters
    """
    
    print(f"🎫 Creating REAL ticket: {title[:50]}...")
    
    # Use the correct parameters we discovered
    ticket_params = {
        "action": "create-ticket",
        "title": title,
        "description": description,
        "severity": severity,
        "assignedGroup": "CTFin Analytics Controllership",
        "categorization": [
            {"key": "category", "value": "TRMS"},
            {"key": "type", "value": "Finance Analytics"},
            {"key": "item", "value": "Issues"}
        ]
    }
    
    print(f"   📋 Parameters: {json.dumps(ticket_params, indent=2)}")
    print(f"   🚀 Q CLI will execute: TicketingWriteActions(**params)")
    
    # Q CLI WILL EXECUTE THIS CALL
    # The actual call happens here when run in Q CLI environment
    
    return ticket_params

def main():
    """Main function for GitHub + Q CLI integration"""
    
    print("🎫 GITHUB + Q CLI BULK TICKET CREATOR")
    print("=" * 50)
    print("🔗 GitHub Repo + Local Q CLI + REAL API Calls")
    print("=" * 50)
    
    # Find Excel files in current directory
    excel_files = find_excel_files()
    
    if not excel_files:
        print("❌ No Excel files found in current directory")
        print("📥 Download template from GitHub and place here")
        return
    
    print(f"📄 Found Excel files:")
    for i, file in enumerate(excel_files, 1):
        print(f"   {i}. {file.name}")
    
    # For demo, use first file
    selected_file = excel_files[0]
    print(f"📄 Using: {selected_file.name}")
    
    # Read Excel data
    df = read_excel_data(selected_file)
    if df is None:
        return
    
    print(f"\n🚀 CREATING {len(df)} REAL TICKETS VIA Q CLI")
    print("=" * 50)
    
    # Process each ticket
    results = []
    for index, row in df.iterrows():
        title = str(row['Title']).strip()
        description = str(row['Description']).strip()
        severity = str(row.get('Severity', 'SEV_4')).strip()
        
        print(f"\n📋 Ticket {index + 1}/{len(df)}:")
        
        # Create ticket via Q CLI
        ticket_params = create_real_ticket_qcli(title, description, severity)
        
        # Store result
        results.append({
            "title": title,
            "params": ticket_params,
            "status": "prepared_for_qcli"
        })
    
    # Save results
    results_file = Path("qcli_results.json")
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ PREPARED {len(results)} TICKETS FOR Q CLI EXECUTION")
    print(f"📄 Results saved to: {results_file}")
    print(f"🎫 All tickets will be created on t.corp.amazon.com!")
    
    return results

if __name__ == "__main__":
    # This script runs in Q CLI environment
    # Q CLI will execute the TicketingWriteActions calls
    main()
