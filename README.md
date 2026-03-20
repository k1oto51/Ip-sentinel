IP Sentinel 

A lightweight Python tool to perform rapid IP reputation lookups using the AbuseIPDB API.

Features
- Fetches **Abuse Confidence Score** (0-100%).
- Identifies the **ISP** and **Country** of origin.
- Displays the total number of reports from the last 90 days.
- Simple command-line interface for quick triage.

Installation
1. Ensure you have Python 3 installed on your system (Ubuntu/WSL).
2. Install the `requests` library:
   ```bash
   pip install requests
