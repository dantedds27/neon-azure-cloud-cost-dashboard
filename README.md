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
