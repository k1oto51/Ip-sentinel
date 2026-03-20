import requests

# === CONFIGURATION ===
# Register at https://www.abuseipdb.com/ to get your free API Key.
# Insert your key between the quotes below:
API_KEY = "YOUR_API_KEY_HERE" 
# =====================

def check_ip_reputation():
    """
    Queries the AbuseIPDB API to check the reputation of a given IP address.
    This is a basic tool for SOC Analysts to triage suspicious activity.
    """
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("[-] Error: API Key is missing!")
        print("[!] Please open ip_sentinel.py and replace the placeholder with your actual key.")
        return

    target_ip = input("Enter the IP address to investigate: ").strip()
    
    # AbuseIPDB API Endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    params = {
        'ipAddress': target_ip,
        'maxAgeInDays': '90' # Check reports from the last 3 months
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }

    print(f"\n[*] Fetching reputation data for: {target_ip}...")

    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()['data']
            
            print("-" * 40)
            print(f"REPORT FOR: {target_ip}")
            print(f"Country: {data.get('countryCode', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Abuse Confidence Score: {data.get('abuseConfidenceScore')}%")
            print(f"Total Reports: {data.get('totalReports')}")
            print("-" * 40)
            
            # Simple Logic for Triage
            score = data.get('abuseConfidenceScore', 0)
            if score > 25:
                print("ALERT: This IP has a high probability of malicious activity!")
            else:
                print("CLEAN: No significant abuse history found for this IP.")
        
        elif response.status_code == 401:
            print("[-] Error 401: Unauthorized. Please check your API Key.")
        else:
            print(f"[-] API Error: Received status code {response.status_code}")

    except Exception as e:
        print(f"[-] A system error occurred: {e}")

if __name__ == "__main__":
    check_ip_reputation()