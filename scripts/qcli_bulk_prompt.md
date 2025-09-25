# Q CLI Bulk Ticket Creation Prompt

Please read the Excel file in the current directory and create REAL tickets using TicketingWriteActions with these parameters:

- assignedGroup: "CTFin Analytics Controllership"
- categorization: [{"key": "category", "value": "TRMS"}, {"key": "type", "value": "Finance Analytics"}, {"key": "item", "value": "Issues"}]
- severity: Use SEV_4 as default, or read from Excel Severity column

For each row in the Excel file:
1. Read Title and Description columns
2. Call TicketingWriteActions to create REAL ticket
3. Report the ticket ID returned

This will create actual tickets on t.corp.amazon.com.
