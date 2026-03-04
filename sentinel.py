import urllib.request
import sys # New import to handle system exit
from datetime import datetime

TARGET_URL = "https://www.google.com" 

def run_health_check():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = urllib.request.urlopen(TARGET_URL)
        status = response.getcode()
        
        if status == 200:
            print(f"[{now}] SUCCESS: {TARGET_URL} is online.")
        else:
            print(f"[{now}] WARNING: Status {status}")
            sys.exit(1) # This "breaks" the cloud build so you get alerted!
            
    except Exception as e:
        print(f"[{now}] FAILED: {e}")
        sys.exit(1) # This "breaks" the cloud build

if __name__ == "__main__":
    run_health_check()
