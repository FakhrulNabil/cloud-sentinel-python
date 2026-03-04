import urllib.request
from datetime import datetime

# The site we want to monitor
TARGET_URL = "https://www.google.com" 

def run_health_check():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Try to open the URL
        response = urllib.request.urlopen(TARGET_URL)
        status = response.getcode()
        
        if status == 200:
            result = f"[{now}] SUCCESS: {TARGET_URL} is online."
        else:
            result = f"[{now}] WARNING: {TARGET_URL} returned status {status}."
            
    except Exception as e:
        result = f"[{now}] FAILED: {TARGET_URL} is unreachable. Error: {e}"

    print(result)
    
    # Save the result to a log file
    with open("status_log.txt", "a") as f:
        f.write(result + "\n")

if __name__ == "__main__":
    run_health_check()