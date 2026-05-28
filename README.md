## neon-azure-cloud-cost-dashboard

### Description
This Python script connects to **Azure Cost Management** using the **Azure CLI credentials** and retrieves cost data for the last 30 days. It displays a colorful terminal dashboard showing service‑level spending, total cost, and alerts if the total exceeds a defined threshold.

### Key Features
- ⚡ **[Real‑time cost retrieval](ca://s?q=Azure_Cost_Management_API_usage)** using Azure SDK  
- 💰 **[Spending alerts](ca://s?q=Azure_cost_alert_thresholds)** when costs exceed your set limit  
- 📈 **[Service breakdown](ca://s?q=Azure_service_cost_breakdown)** for detailed visibility  
- 💾 **[Automatic report saving](ca://s?q=Azure_cost_report_saving)** to timestamped text files  

### How It Works
1. Authenticates via `AzureCliCredential` — ensure you’ve logged in with:
   ```bash
   az login

## About
Built as part of my Azure cloud engineering portfolio 
while studying for Microsoft Azure certifications.

## Features
- Fetches real Azure cost data via Cost Management API
- Neon hacker-style colour-coded terminal output
- Spending threshold alert system
- Saves a timestamped cost report to a .txt file
- Breakdown by service name

## Certifications
- Microsoft AZ-900 Azure Fundamentals ✅

## Tech Stack
- Python 3
- Azure SDK (azure-identity, azure-mgmt-costmanagement)
- Azure CLI
- python-dotenv for secure credential management

## Setup
pip3 install azure-identity azure-mgmt-costmanagement python-dotenv
az login
Create a .env file with your SUB_ID and LIMIT values
python3 cost_monitor.py

## Author
Dante | Aspiring Azure Cloud Engineer
