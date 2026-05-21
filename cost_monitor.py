from azure.identity import AzureCliCredential
from azure.mgmt.costmanagement import CostManagementClient
from datetime import datetime, timedelta
import sys

if sys.version_info[0] < 3:
    print("This script requires Python 3. Please upgrade your Python version.")
    sys.exit(1)

CYAN      = "\033[96m"
NEON      = "\033[92m"
WHITE     = "\033[97m"
DIM       = "\033[2m"
RED       = "\033[91m"
YELLOW    = "\033[93m"
RESET     = "\033[0m"
BOLD      = "\033[1m"
UNDERLINE = "\033[4m"

ICON_MONEY = "\U0001F4B0"
ICON_WARN  = "\U000026A0"
ICON_CHECK = "\U00002705"
ICON_CHART = "\U0001F4CA"
ICON_SAVE  = "\U0001F4BE"
ICON_CLOUD = "\U00002601"
ICON_BOLT  = "\U000026A1"

# Your Azure subscription ID
SUB_ID = "your-subscription-id-here"  # <-- Change this to your actual subscription ID

# Alert threshold in USD - change this to whatever you want
LIMIT= 50.0

# Prints the dashboard with the current time 
def print_header():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{BOLD}{CYAN}Cost Monitor - {now}{RESET}")
    print(f"\n{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}{CYAN}Azure Cost Management Dashboard{RESET}  {DIM}|{RESET}  {YELLOW}{now}{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"   {NEON}{ICON_BOLT}  Sub   :{RESET} {WHITE}{SUB_ID}{RESET}")
    print(f"   {NEON}{ICON_MONEY} Limit  :{RESET} {WHITE}${LIMIT:.2f}{RESET}\n")

 # Retrieves Azure credentials using Azure CLI and initializes the Cost Management client
def get_client():
    credential = AzureCliCredential()
    client = CostManagementClient(credential)
    return client   
 
def get_costs(client):
    today = datetime.now(timezone.utc)
    start = (today - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end   = today.strftime("%Y-%m-%dT%H:%M:%SZ")

    scope      = f"/subscriptions/{SUB_ID}"
    parameters = {
        "type": "ActualCost",
        "timeframe": "Custom",
        "timePeriod": {"from": start, "to": end},
        "dataset": {
            "granularity": "None",
            "aggregation": {
                "totalCost": {"name": "Cost", "function": "Sum"}
            },
            "grouping": [{"type": "Dimension", "name": "ServiceName"}]
        }
    }

    try:
        result = client.query.usage(scope, parameters)
        return result
    except Exception as e:
        print(f"{RED}Error fetching costs: {e}{RESET}")
        return None

def print_costs(result):
    if not result or not result.rows:
        print(f"{YELLOW}{ICON_WARN} No cost data found for the last 30 days.{RESET}\n")
        return

    total = 0.0
    print(f"{BOLD}{CYAN}{ICON_CHART} Cost Breakdown  {DIM}| Last 30 Days{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}\n")
    for row in result.rows:
        cost    = float(row[0])
        service = str(row[1])
        total  += cost
        print(f"  {NEON}{ICON_BOLT} {service:<35}{RESET} {WHITE}${cost:.2f}{RESET}")
    print(f"\n{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"  {NEON}{ICON_MONEY} Total :{RESET} {WHITE}${total:.2f} USD{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}\n")
    if total > LIMIT:
        print(f"  {RED}{BOLD}{ICON_WARN} ALERT: ${total:.2f} exceeds limit of ${LIMIT:.2f}!{RESET}\n")
    else:
        print(f"  {NEON}{ICON_CHECK} Spend is within limit.{RESET}\n")
def save_report(result):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cost_report_{now}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Azure Cost Report - {now}\n")
        f.write(f"Subscription: {SUB_ID}\n")
        f.write(f"Limit: ${LIMIT} USD\n")
        f.write("="*55 + "\n\n")
        
        if not result or not result.rows:
            f.write("No cost data available. \n")
        else:
            total = 0.0
            for row in result.rows:
                cost = float(row[0])
                service = str(row[1])
                f.write(f"{service:<40} ${cost:.2f}\n")
                total += cost
            f.write("\n" + "="*55 + "\n")
            f.write(f"Total Cost (Last 30 Days): ${total:.2f}\n")
    print(f" {NEON}{ICON_SAVE} Report saved to {WHITE}{filename}{RESET}\n")
    # Optionally, you could also save the report in CSV format for easier analysis in Excel or other tools.

def main():
    print_header()
    client = get_client()
    result = get_costs(client)
    print_costs(result)
    save_report(result)

if __name__ == "__main__":
    main()
