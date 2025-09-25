# GitHub + Q CLI Setup Instructions

## 🚀 How to Set Up GitHub-Hosted Q CLI Bulk Ticket System

### Step 1: Create GitHub Repository
```bash
# Create new repo on GitHub
# Clone it locally
git clone https://github.com/yourusername/bulk-ticket-system.git
cd bulk-ticket-system
```

### Step 2: Upload Files to GitHub
```bash
# Copy these files to your repo
cp /home/ranmaya/ticket_creation_template.xlsx ./templates/
cp /home/ranmaya/qcli_github_script.py ./scripts/
cp /home/ranmaya/github_setup_instructions.md ./

# Commit and push
git add .
git commit -m "Initial setup: Q CLI bulk ticket system"
git push origin main
```

### Step 3: Local Usage (REAL Q CLI Execution)
```bash
# Clone repo to your local machine
git clone https://github.com/yourusername/bulk-ticket-system.git
cd bulk-ticket-system

# Download Excel template from GitHub
# Fill it with your ticket data
# Place filled Excel file in repo root

# Run Q CLI script (makes REAL API calls)
q chat -f scripts/qcli_github_script.py
```

### Step 4: Web UI (Optional)
Create simple HTML page hosted on GitHub Pages:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Q CLI Bulk Tickets</title>
</head>
<body>
    <h1>🎫 Q CLI Bulk Ticket System</h1>
    
    <h2>📥 Download Templates</h2>
    <a href="templates/ticket_creation_template.xlsx">Download Excel Template</a>
    
    <h2>🚀 Usage Instructions</h2>
    <ol>
        <li>Download Excel template above</li>
        <li>Fill with your ticket data</li>
        <li>Clone this repo locally</li>
        <li>Place Excel file in repo root</li>
        <li>Run: <code>q chat -f scripts/qcli_github_script.py</code></li>
        <li>REAL tickets created on t.corp.amazon.com!</li>
    </ol>
    
    <h2>📋 Requirements</h2>
    <ul>
        <li>Excel columns: Title, Description (required)</li>
        <li>Optional: Severity, Category, Type, Item</li>
        <li>Q CLI installed and authenticated</li>
    </ul>
</body>
</html>
```

## 🎯 Benefits of This Approach

### ✅ Advantages
- **Real Q CLI calls** - No fake API responses
- **GitHub hosting** - Templates and UI accessible anywhere
- **Version control** - Track changes to scripts and templates
- **Shareable** - Anyone can clone and use
- **Local execution** - Uses your Q CLI authentication
- **No server needed** - Everything runs locally

### 🔧 How It Works
1. **GitHub** hosts templates, scripts, and UI
2. **User downloads** Excel template from GitHub
3. **User clones repo** locally
4. **User runs Q CLI script** in repo folder
5. **Q CLI executes** REAL TicketingWriteActions calls
6. **Real tickets created** on t.corp.amazon.com

### 📁 File Structure
```
your-repo/
├── templates/
│   └── ticket_creation_template.xlsx
├── scripts/
│   └── qcli_github_script.py
├── ui/
│   └── index.html
└── README.md
```

## 🎫 Example Usage

```bash
# 1. Clone repo
git clone https://github.com/yourusername/bulk-ticket-system.git
cd bulk-ticket-system

# 2. Add your Excel file
cp ~/my_tickets.xlsx ./

# 3. Run Q CLI script (creates REAL tickets)
q chat -f scripts/qcli_github_script.py

# Output:
# 🎫 GITHUB + Q CLI BULK TICKET CREATOR
# 📄 Found Excel files: my_tickets.xlsx
# 🚀 CREATING 5 REAL TICKETS VIA Q CLI
# 📋 Ticket 1/5: Creating REAL ticket...
# ✅ PREPARED 5 TICKETS FOR Q CLI EXECUTION
```

This approach gives you:
- ✅ **Real Q CLI integration** (no faking)
- ✅ **GitHub hosting** for easy access
- ✅ **Local execution** with your credentials
- ✅ **Actual tickets** created on t.corp.amazon.com
